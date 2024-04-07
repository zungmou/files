// ==UserScript==
// @name         雪球标点符号复位
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  
// @author       Dylan
// @match        https://xueqiu.com/*/*
// @icon         https://www.google.com/s2/favicons?domain=xueqiu.com
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    const location = window.location.href

    if (/https:\/\/xueqiu.com\/\d+\/\d+/.test(location)) {
        for (const hchar of document.querySelectorAll('h-char')) {
            hchar.replaceWith(hchar.textContent)
        }
    }
})();