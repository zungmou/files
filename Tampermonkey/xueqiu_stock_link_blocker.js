// ==UserScript==
// @name         雪球屏蔽股票链接
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
        for (const anchor of document.querySelectorAll('a')) {
            if (anchor.classList.contains('xq_stock')) {
                anchor.replaceWith(anchor.textContent)
            }
        }
    }
})();