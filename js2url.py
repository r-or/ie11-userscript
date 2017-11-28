from __future__ import with_statement
import sys, os

if len(sys.argv) != 2:
    print('Usage: python js2url.py <path to javascript source>')
    sys.exit()

lHull = '''
        javascript: (function(d) {
            var j = '';
            %s
            var body = d.getElementsByTagName('body')[0];
            var script = d.createElement('script');
            var node = d.createTextNode(j);
            script.type = 'text/javascript';
            script.appendChild(node);
            body.appendChild(script);
        }(window.document))
        '''
blHull = '''
        [{000214A0-0000-0000-C000-000000000046}]
        Prop3=19,15
        [InternetShortcut]
        URL=%s
        IDList=
        [Bookmarklet]
        ExtendedURL=%s
        '''

jssource = ''
with open(sys.argv[1], 'r') as f:
    # remove newlines & quotes and escape "'"
    for line in f.readlines():
        jssource += line.strip() \
                        .replace('"', '\\\'') \
                        .replace('\'', '\\\'')

# 1 cmd in booklet can only be ~ 80 chars
jPrefix = 'j += '
jLen = 80 - len(jPrefix) - 2
jssource = lHull % (';'.join([(jPrefix + '\'' + jssource[k : k + jLen] + '\'') for k in range(0, len(jssource), jLen)]) + ';')
jssource = ''.join([line.strip() for line in jssource.strip().split('\n')])
blsource = blHull % (jssource, jssource)
blsource = '\n'.join([line.strip() for line in blsource.strip().split('\n')])

outfile = os.path.basename(sys.argv[1]).split('.')[0] + '.url'
with open(outfile, 'w') as f:
    f.write(blsource)

print('Saved as "%s"!' % outfile)
