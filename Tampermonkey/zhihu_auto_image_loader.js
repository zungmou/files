// ==UserScript==
// @name         自动加载知乎图片
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  
// @author       Dylan
// @match        https://zhuanlan.zhihu.com/p/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=zhihu.com
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    for (const img of document.querySelectorAll('img[data-original]')) {
        if (!img.attributes['src'].value.startsWith('http')) {
            img.attributes['src'].value = img.attributes['data-original'].value;
        }
    }
})();