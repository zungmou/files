// ==UserScript==
// @name         雪球截图优化
// @namespace    http://tampermonkey.net/
// @version      2024-03-26
// @description  
// @author       Dylan
// @match        https://xueqiu.com/*/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=xueqiu.com
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    var parent = document.querySelector('article.article__bd');
    var child = document.querySelector('div.article__author');
    var referenceNode = document.querySelector('h1.article__bd__title');

    parent.insertBefore(child, referenceNode);
    parent.style.padding = '.5em';

    document.querySelector('div.container.article__container').style.width = '660px';
})();