from __future__ import with_statement
import os

import app

app = app.CMDApp('userscript2bookmarklet')
app.addArg(['s', '-source'], 'javascript inside <source> container', arglist = str, mandatory = True)
app.addArg(['n', '-name'], 'name of finished link/bookmarklet', arglist = str)
app.parseArgs()

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
with open(app.arglist('s')[0], 'r') as f:
    # remove newlines & quotes and escape "'"
    for line in f.readlines():
        jssource += line.strip() \
                        .replace('"', '\\\'') \
                        .replace('\'', '\\\'')

# 1 cmd in booklet can only be ~ 80 chars
jLen = 80
jPrefix = 'j += '
jssource = lHull % (';'.join([(jPrefix + '\'' + jssource[k : k + jLen - 2] + '\'') for k in range(0, 
                                                                                                  len(jssource), 
                                                                                                  jLen - 2)]) + ';')
jssource = ''.join([line.strip() for line in jssource.strip().split('\n')])
blsource = blHull % (jssource, jssource)
blsource = '\n'.join([line.strip() for line in blsource.strip().split('\n')])

print(blsource)

outfile = (app.arglist('n')[0] + '.url') if app.gotArg('n') else os.path.basename(app.arglist('s')[0]).split('.')[0] + '.url'
with open(outfile, 'w') as f:
    f.write(blsource)
