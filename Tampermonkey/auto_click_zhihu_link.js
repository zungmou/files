// ==UserScript==
// @name         知乎外链自动点击
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  
// @author       Dylan
// @match        https://www.zhihu.com/question/*
// @require      https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.min.js
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    function unlink() {
        $('a[href^="https://link.zhihu.com/?target="').each(function () {
            let href = $(this).attr('href');
            href = href.substr("https://link.zhihu.com/?target=".length);
            href = decodeURIComponent(href);
            $(this).attr('href', href);
        });
        window.setTimeout(unlink, 2000);
    }

    window.setTimeout(unlink, 2000);
})();