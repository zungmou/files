// ==UserScript==
// @name         Evernote 外链自动点击
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  
// @author       Dylan
// @match        https://www.evernote.com/OutboundRedirect.action?dest=*
// @icon         https://www.google.com/s2/favicons?domain=evernote.com
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    // Your code here...
    setTimeout("document.getElementById('continueToDest').click();", 500);
})();