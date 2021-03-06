# ie11-userscript
This script converts a javascript userscript snippet to a so-called booklet for Internet Explorer 11.

If for whatever reason you still have to use IE11 you can add user scripts via "bookmarklets". Inspiration / more information: https://css-tricks.com/prefilling-forms-custom-bookmarklet/

Adding bookmarklets has a few catches:
* there is a limit of characters one javascript command can have inside the bookmarklet (somewhere above 80)
* there cannot be a newline inside the bookmarklet
* it's 2017 and IE11 is old... which limits what can be / how it can be done.

Those issues are now a thing of the past! (Well except the last one)

This script just takes a javascript source code file as input, converts it using the rules above and outputs the .url bookmarklet which then can be placed in the "Favourites" folder inside ones home folder. Then it appears on the Favourites bar in IE. Click it to apply the script on the page you're currently visiting!

An example:
js.js:
```javascript
console.log('installation seems to have worked, yay!');
var divs = document.getElementsByTagName('div');
for (var idx = 0; idx < divs.length; ++idx) {
  if (divs[idx].hasAttribute('class') && divs[idx].getAttribute('class').indexOf('ua-detected') >= 0) {
    console.log('found item... !PURGE!');
    divs[idx].parentNode.removeChild(divs[idx]);
  }
}
```
Conversion:
```
python js2url.py js.js
```

Output:
js.url:
```
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,15
[InternetShortcut]
URL=javascript:(function(d) {var jscript = '';jscript += 'console.log(\'installation seems to have worked, yay!\');';jscript += 'var divs = document.getElementsByTagName(\'div\');';jscript += 'for (var idx = 0; idx < divs.length; ++idx) {';jscript += 'if (divs[idx].hasAttribute(\'class\') && ';jscript += 'divs[idx].getAttribute(\'class\').indexOf(\'-detected\') > 0) {';jscript += 'console.log(\'found item... !PURGE!\');';jscript += 'divs[idx].parentNode.removeChild(divs[idx]);';jscript += '} else {';/*jscript += 'console.log(\'discarded item: \');console.log(divs[idx]);';*/jscript += '}';jscript += '}';var body = d.getElementsByTagName('body')[0];var script = d.createElement('script');var node = d.createTextNode(jscript);script.type = 'text/javascript';script.appendChild(node);body.appendChild(script);}(window.document))
IDList=
[Bookmarklet]
ExtendedURL=javascript:(function(d) {var jscript = '';jscript += 'console.log(\'installation seems to have worked, yay!\');';jscript += 'var divs = document.getElementsByTagName(\'div\');';jscript += 'for (var idx = 0; idx < divs.length; ++idx) {';jscript += 'if (divs[idx].hasAttribute(\'class\') && ';jscript += 'divs[idx].getAttribute(\'class\').indexOf(\'-detected\') > 0) {';jscript += 'console.log(\'found item... !PURGE!\');';jscript += 'divs[idx].parentNode.removeChild(divs[idx]);';jscript += '} else {';/*jscript += 'console.log(\'discarded item: \');console.log(divs[idx]);';*/jscript += '}';jscript += '}';var body = d.getElementsByTagName('body')[0];var script = d.createElement('script');var node = d.createTextNode(jscript);script.type = 'text/javascript';script.appendChild(node);body.appendChild(script);}(window.document))
```
