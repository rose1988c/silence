---
title: JavaScript日期处理类库 - Moment.js
date: 2013-01-29 13:45:47
categories: JavaScript
tags: JavaScript
---

[Moment.js](http://momentjs.com/) 是一个简单易用的轻量级JavaScript日期处理类库，提供了日期格式化、日期解析等功能。它支持在浏览器和NodeJS两种环境中运行。此类库能够将给定的任意日期转换成多种不同的格式，具有强大的日期计算功能，同时也内置了能显示多样的日期形式的函数。另外，它也支持多种语言，你可以任意新增一种新的语言包。

> A 5kb javascript date library
> for parsing, validating, manipulating, and formatting dates. 

## Formatting dates

    moment().format('MMMM Do YYYY, h:mm:ss a');
    moment().format('dddd');
    moment().format("MMM Do YY");
    moment().format('YYYY [escaped] YYYY');
    moment().format();

<!-- more -->


## Timeago

    moment("20111031", "YYYYMMDD").fromNow();
    moment("20120620", "YYYYMMDD").fromNow();
    moment().startOf('day').fromNow();
    moment().endOf('day').fromNow();
    moment().startOf('hour').fromNow();

## Calendar Time

    moment().subtract('days', 10).calendar();
    moment().subtract('days', 6).calendar();
    moment().subtract('days', 3).calendar();
    moment().subtract('days', 1).calendar();
    moment().calendar();
    moment().add('days', 1).calendar();
    moment().add('days', 3).calendar();
    moment().add('days', 10).calendar();

## Internationalization

    moment().format('L');
    moment().format('LL');
    moment().format('LLL');
    moment().format('LLLL');