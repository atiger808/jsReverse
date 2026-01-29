// @File   :jsCode.js
// @Time   :2026/1/28 15:18
// @Author :dayue
// @Email  :ole211@qq.com

const CryptoJS = require('crypto-js');
const JsEncrypt = require('jsencrypt');

function rr(e, t) {
    var n, i, a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split(""), r = [];
    if (t = t || a.length,
        e)
        for (n = 0; n < e; n++)
            r[n] = a[0 | Math.random() * t];
    else
        for (r[8] = r[13] = r[18] = r[23] = "-",
                 r[14] = "4",
                 n = 0; n < 36; n++)
            r[n] || (i = 0 | 16 * Math.random(),
                r[n] = a[19 == n ? 3 & i | 8 : i]);
    return r.join("")
}

var f = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCC3Lb0O4zgEakDfJ4XJO5zadXep9bQeWyJ6pa0e328PYQYZgLNP7eVrAP7mVZgG+8D4MicIcStTQnBxF8AEyJKrh/M/3WSSK2zDvrZn1paWf4SA8zFIn5cuYlcUH+WuxghQn3kKRUW2qtBY9eaGF5qntascctNgQTHmW3eqQzDBQIDAQAB"
    ,
    p = "MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBALROqKeWuu+G6z6V7lesaAIC8FWWJ8qYRRy4HbbakJBH+OEWfD+0/MmMnZ28aMiV3qDy34SLfddDxvWJo/SR8iL8bjeqOEQxenu8Ogec+290w4F8IW6Ips/kZ5pnkg/TUn1GATOSV+RbB90okuykbBEbGKaNqGczJ/lI7RpfNvCpAgMBAAECgYA9RzJYaoizmRXgGlJ7Z3Odo2QMolB5sRBj90rZ9yQEdQFndh3aBOeYk/qJPhwad5zG9GP0hvfIrhczIYkgOG2i1ZvBAFBP7IZiGJz5PxS9QOFPg926sI6Mv3nBIS0+U88IyzPL/fQWNvhc3b9Y95kYp4p0Wk4zzNe9HNNUMQHdUQJBAOwA6EoVSlxlpNivoAGrMynLlnHmZ7fEpXXQINUbhpX8+I3fazoWcRaYpfLmVKa82DJXHUe8URFX3oir3kAocVUCQQDDlahWFmYmtNYqLitJdIdltTcmQtAgHlfshdYnq6Gg8jSjwh40sXF8MgZfG03+sfdmKbSG3e+7Ihb/X5P/odIFAkEAlz3Rn0BbojDlXpPWN5uOMzesFxwv1Z3o50JU+B0mt9IhO1I1dklRecijeLFRCHW3GzOmqQUu8q1cCDwUNwtz7QJBAJ3BT8coR/q+b+QT20xjVnaeBT6yM2dEskyP4x2aXUMROY5Am9aKrWuseeEqh+2ApHld+EO0LZJ2O7B96kUNw/UCQHhXTTBHc2HkyU84U2+OAB2hJtJBmj+eGl0iqNfOq3JyiIemC/bV74sASLa+NN9CJRotBh9jzmzNpwEi24Y8KHE=";

function h(e) {
    var t = rr(16, 16)
        , n = CryptoJS.enc.Utf8.parse(t)
        , i = CryptoJS.enc.Utf8.parse(e)
        , r = CryptoJS.AES.encrypt(i, n, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    })
        , c = r.toString()
        , l = new JsEncrypt;
    l.setPublicKey(f);
    var u = l.encrypt(t);
    return {
        content: c,
        aesKey: u
    }
}


function m(e, t) {
    var n = new JsEncrypt;
    n.setPrivateKey(p);
    var i = n.decrypt(t)
        , r = CryptoJS.enc.Utf8.parse(i)
        , o = CryptoJS.AES.decrypt(e, r, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return JSON.parse(CryptoJS.enc.Utf8.stringify(o).toString())
}


data = {
    "aesKey": "sQ9TBg2oGDyMWXXLq1dZVtWKoidYtSO23H7akD1UUBc9POCm7wgp1l0VA4xgURKqXeg4ab8PC/NQEPOSlZ3s62uUTUV1MhNJTvmYg7s56SMHFdCZeskE50UMqPjl9eWPB4FTuQCjZ5IZe9+LfhRJR7DRUcE4i0VMoq/lHz6oVcI=",
    "content": "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"
}

function decrypt(data) {

    var t = data
        , n = t.content
        , i = t.aesKey;
    if (Object.prototype.hasOwnProperty.call(data, "aesKey") && i) {
        var a = m(n, i);
        console.log(a)
        return a
    }
}


result = decrypt(data)
console.log("result: ", result)


function encrypt(data) {
    var g = h(JSON.stringify(data));
    console.log("g: ", g)
    return g
}


data = {
    "noticeName": null,
    "pageNum": 3,
    "pageSize": 10,
    "tenderCategory": "6",
    "noticeType": null,
    "tenderClass": null
}

result = encrypt(data)
console.log("result: ", result)