// @File   :gaokao_encrypt.js
// @Time   :2026/1/27 14:50
// @Author :dayue
// @Email  :ole211@qq.com

// import CryptoJS from 'crypto-js'  此种写法python运行会报错，需要安装crypto-js库
const CryptoJS = require('crypto-js');

function str2md5(s) {
    return CryptoJS.MD5(s).toString()
}

function r(t) {
    return (r = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (t) {
                return typeof t
            }
            : function (t) {
                return t && "function" == typeof Symbol && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t
            }
    )(t)
}

function o(t) {
    t = function (t, e) {
        if ("object" != r(t) || !t)
            return t;
        var n;
        if (void 0 === (n = t[Symbol.toPrimitive]))
            return ("string" === e ? String : Number)(t);
        if ("object" != r(n = n.call(t, e || "default")))
            return n;
        throw new TypeError("@@toPrimitive must return a primitive value.")
    }(t, "string");
    return "symbol" == r(t) ? t : String(t)
}

function a(t, e) {
    var n, r = Object.keys(t);
    return Object.getOwnPropertySymbols && (n = Object.getOwnPropertySymbols(t),
    e && (n = n.filter((function (e) {
            return Object.getOwnPropertyDescriptor(t, e).enumerable
        }
    ))),
        r.push.apply(r, n)),
        r
}


function i(t, e, n) {
    (e = o(e)) in t ? Object.defineProperty(t, e, {
        value: n,
        enumerable: !0,
        configurable: !0,
        writable: !0
    }) : t[e] = n
}

function c(t) {
    for (var e = 1; e < arguments.length; e++) {
        var n = null != arguments[e] ? arguments[e] : {};
        e % 2 ? a(Object(n), !0).forEach((function (e) {
                i(t, e, n[e])
            }
        )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(t, Object.getOwnPropertyDescriptors(n)) : a(Object(n)).forEach((function (e) {
                Object.defineProperty(t, e, Object.getOwnPropertyDescriptor(n, e))
            }
        ))
    }
    return t
}

function ct(t) {
    var n, e = [];
    let c = 0;
    for (n in t)
        e[c] = n,
            c++;
    var o, r = e.sort(), a = {};
    for (o in r)
        a[r[o]] = t[r[o]];
    return a
}

function aesEncrypt(d) {

    var l = "XfqauTPSQHSpwJX6",
        t = CryptoJS.enc.Latin1.parse("CernetFIT4206Sun"),
        e = CryptoJS.enc.Latin1.parse(l),
        l = CryptoJS.AES.encrypt(d, t, {
            iv: e,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }).toString();
    return CryptoJS.enc.Base64.parse(l).toString()

}

function d(e) {
    var n, t = {
        appVersion: navigator.appVersion,
        platform: navigator.platform,
        userAgent: navigator.userAgent,
        appName: navigator.appName
    }, o = ct(t);
    let r = "";
    for (n in o)
        r += n + "=" + o[n] + "&";
    r = r.slice(0, r.length - 1);
    t = str2md5(r);
    var u, l = (new Date).getTime(), s = (e = c(c({}, e), {}, {
        time: parseInt(Number(l) / 1e3),
        mac: t
    }),
        ct(e));
    let d = "";
    for (u in s)
        d += u + "=" + s[u] + "&";
    d = d.slice(0, d.length - 1);
    return aesEncrypt(d)
    // l = "XfqauTPSQHSpwJX6",
    //     t = i.a.enc.Latin1.parse("CernetFIT4206Sun"),
    //     e = i.a.enc.Latin1.parse(l),
    //     l = i.a.AES.encrypt(d, t, {
    //         iv: e,
    //         mode: i.a.mode.CBC,
    //         padding: i.a.pad.Pkcs7
    //     }).toString();
    // return i.a.enc.Base64.parse(l).toString()
}


function b(t) {
    var {SIGN: t, str: n} = t
        , n = (n = decodeURI(n),
        CryptoJS.HmacSHA1(CryptoJS.enc.Utf8.parse(n), t));
    t = CryptoJS.enc.Base64.stringify(n).toString();
    return str2md5(t)
}


function encryptSign(ee) {
    return d(ee)
}


function encryptSignSafe(l) {
    var g = "D23ABC@#56"
    var tt = {
        SIGN: g,
        str: l.replace(/^\/|https?:\/\/\/?/, "")
    }
    return b(tt)
}

var ee = {
    "phone": "18669363693",
    "password": "qweasd12345678",
    "login_type": 8
}


var sign = encryptSign(ee)
console.log("sign: ", sign)


var l = "https://api.zjzw.cn/web/api/?login_regist_from=2&method=2&sign=5356b123e8e28bbc9c61dc62e71001714836bf9380d123199198416a99efd7302164c076406f40a18f261fd6f69fcd175686fcd1f59e1350cadc4454154e9b60eb3e17eb2fce585612e2936937d781f9d6c1e33d2cacccf198379b447269107c5232a70079c7e5b3415f0ab92fd59a77&uri=apigkcx/api/user/login"

var signsafe = encryptSignSafe(l)
console.log("signsafe: ", signsafe)

