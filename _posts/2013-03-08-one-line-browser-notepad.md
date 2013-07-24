title: one-line-browser-notepad
date: 2013-02-01 17:05:28
tags: [Html5,Code]
categories: browser
---

## Introduction

Sometimes I just need to type garbage. Just to clear out my mind. Using editors to type such gibberish annoys me because it clutters my project workspace (I'm picky, I know).

So I do this. Since I live in the browser, I just open a new tab and type in the url tab.

    data:text/html, <html contenteditable>

Voila, browser notepad.

## Why it works?

You don't need to remember it. It's not rocket science. We are using the Data URI's format and telling the browser to render an html (try "javascript:alert('Bazinga');"). The content of said html is a simple html line with the html5 attribute contenteditable. This works only on modern browsers that understand this attribute. Click and type!

Reprint: [https://coderwall.com/p/lhsrcq](https://coderwall.com/p/lhsrcq)