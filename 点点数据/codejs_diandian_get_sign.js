// @File   :codejs_diandian_get_sign.js
// @Time   :2024/12/30 16:07
// @Author :dayue
// @Email  :ole211@qq.com

const fs = require("fs")

const jsdom = require("jsdom");
const {JSDOM} = jsdom;

dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);

// 在这里，你可以运行你的JavaScript代码
window = dom.window;
document = dom.window.document


navigator = {
    vendor: "Google Inc.",
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    platform: "Win32",
    product: "Gecko",
    productSub: "20030107",
    vendorSub: "",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}



function readLocalJS(filePath) {
    return eval(fs.readFileSync(filePath) + "\r\n")
}

jsCode = readLocalJS('./codejs_diandian_webpack_func.js')
console.log("len: ", Object.keys(jsCode).length)

!function (e) {
    function n(data) {
        for (var n, c, l = data[0], d = data[1], f = data[2], i = 0, _ = []; i < l.length; i++)
            c = l[i],
            Object.prototype.hasOwnProperty.call(o, c) && o[c] && _.push(o[c][0]),
                o[c] = 0;
        for (n in d)
            Object.prototype.hasOwnProperty.call(d, n) && (e[n] = d[n]);
        for (m && m(data); _.length;)
            _.shift()();
        return r.push.apply(r, f || []),
            t()
    }

    function t() {
        for (var e, i = 0; i < r.length; i++) {
            for (var n = r[i], t = !0, c = 1; c < n.length; c++) {
                var d = n[c];
                0 !== o[d] && (t = !1)
            }
            t && (r.splice(i--, 1),
                e = l(l.s = n[0]))
        }
        return e
    }

    var c = {}
        , o = {
        188: 0
    }
        , r = [];

    function l(n) {
        if (c[n])
            return c[n].exports;
        var t = c[n] = {
            i: n,
            l: !1,
            exports: {}
        };
        return e[n].call(t.exports, t, t.exports, l),
            t.l = !0,
            t.exports
    }

    window._export_loader = l

    l.e = function (e) {
        var n = []
            , t = o[e];
        if (0 !== t)
            if (t)
                n.push(t[2]);
            else {
                var c = new Promise((function (n, c) {
                        t = o[e] = [n, c]
                    }
                ));
                n.push(t[2] = c);
                var r, script = document.createElement("script");
                script.charset = "utf-8",
                    script.timeout = 120,
                l.nc && script.setAttribute("nonce", l.nc),
                    script.src = function (e) {
                        return l.p + "" + ({
                            35: "commons/200a90f4~d0e14ce1",
                            36: "commons/lang.index~lang.sem~index~sem~01e7b97c",
                            37: "commons/3f9dde86~e1c77a85",
                            38: "commons/802d2e3c~01e7b97c",
                            39: "commons/lang.index~index~8c7c996f",
                            40: "commons/pages/_lang/index/pages/index~253ae210",
                            117: "pages/_lang/about-us/diandian~01e7b97c",
                            118: "pages/_lang/about-us~d4b76461",
                            119: "pages/_lang/about/protocolPolicy~ee095578",
                            120: "pages/_lang/account/index~3870caa0",
                            121: "pages/_lang/account/setting/controllist/:id-:market-:country~bf296fc3",
                            122: "pages/_lang/account/setting/controllist/index~cfa0ce50",
                            123: "pages/_lang/account/setting/wechart/:id-:market-:country~bf296fc3",
                            124: "pages/_lang/account/setting/wechart/index~01e7b97c",
                            125: "pages/_lang/findPwd~0c61b134",
                            126: "pages/_lang/intelligence/app~070191bc",
                            127: "pages/_lang/intelligence/aso-asa~070191bc",
                            128: "pages/_lang/intelligence/in-app-purchase~070191bc",
                            129: "pages/_lang/intelligence/marketing~070191bc",
                            130: "pages/_lang/intelligence/technology~070191bc",
                            131: "pages/_lang/intelligence/usage~070191bc",
                            132: "pages/_lang/intelligence/user~070191bc",
                            133: "pages/_lang/map/:tab-:page~e8c3d1e3",
                            134: "pages/_lang/news/:id~f247b1cc",
                            135: "pages/_lang/report/2023-1-mobilegame~eefba503",
                            136: "pages/_lang/report/2023-oversea-mobilegame~be5cf67e",
                            137: "pages/_lang/report/2024-aigc~cc0371e8",
                            138: "pages/_lang/report/2024-brazil~56239384",
                            139: "pages/_lang/report/:name~e1134331",
                            140: "pages/_lang/report/index~e1134331",
                            141: "pages/_lang/report/request_report~c82f0bb5",
                            142: "pages/_lang/reports/:id~f247b1cc",
                            143: "pages/_lang/search/:word~01e7b97c",
                            144: "pages/_lang/sem~3870caa0",
                            145: "pages/_lang/solutions/app~070191bc",
                            146: "pages/_lang/solutions/brand~070191bc",
                            147: "pages/_lang/solutions/enterprise~070191bc",
                            148: "pages/_lang/solutions/finance~070191bc",
                            149: "pages/_lang/solutions/game~070191bc",
                            150: "pages/_lang/solutions/growth~070191bc",
                            151: "pages/_lang/solutions/marketing~070191bc",
                            152: "pages/about-us~d4b76461",
                            153: "pages/aboutus~01e7b97c",
                            154: "pages/account/index~3870caa0",
                            155: "pages/account/setting/controllist/:id-:market-:country~bf296fc3",
                            156: "pages/account/setting/controllist/index~cfa0ce50",
                            157: "pages/account/setting/wechart/:id-:market-:country~bf296fc3",
                            158: "pages/account/setting/wechart/index~01e7b97c",
                            159: "pages/findPwd~0c61b134",
                            160: "pages/intelligence/app~070191bc",
                            161: "pages/intelligence/aso-asa~070191bc",
                            162: "pages/intelligence/in-app-purchase~070191bc",
                            163: "pages/intelligence/marketing~070191bc",
                            164: "pages/intelligence/technology~070191bc",
                            165: "pages/intelligence/usage~070191bc",
                            166: "pages/intelligence/user~070191bc",
                            167: "pages/map/:tab-:page~e8c3d1e3",
                            168: "pages/map/index~e8c3d1e3",
                            169: "pages/news/:id~f247b1cc",
                            170: "pages/protocolPolicy~ee095578",
                            171: "pages/report/2023-1-mobilegame~eefba503",
                            172: "pages/report/2023-oversea-mobilegame~be5cf67e",
                            173: "pages/report/2024-aigc~cc0371e8",
                            174: "pages/report/2024-brazil~56239384",
                            175: "pages/report/:name~e1134331",
                            176: "pages/report/index~e1134331",
                            177: "pages/report/request_report~c82f0bb5",
                            178: "pages/reports/:id~f247b1cc",
                            179: "pages/search/:word~01e7b97c",
                            180: "pages/sem~3870caa0",
                            181: "pages/solutions/app~070191bc",
                            182: "pages/solutions/brand~070191bc",
                            183: "pages/solutions/enterprise~070191bc",
                            184: "pages/solutions/finance~070191bc",
                            185: "pages/solutions/game~070191bc",
                            186: "pages/solutions/growth~070191bc",
                            187: "pages/solutions/marketing~070191bc",
                            189: "vendors~pdfjsWorker~331d6c2b"
                        }[e] || e) + "." + {
                            35: "251085f",
                            36: "6bb7f17",
                            37: "baab414",
                            38: "c925a4e",
                            39: "a245149",
                            40: "e6243d6",
                            117: "f12d222",
                            118: "d4cfae2",
                            119: "143e699",
                            120: "65f9aed",
                            121: "d911131",
                            122: "5d1999f",
                            123: "be341d0",
                            124: "027a03b",
                            125: "24d4827",
                            126: "b7d2b7c",
                            127: "7120c1e",
                            128: "10de389",
                            129: "409a5dd",
                            130: "89e49bf",
                            131: "8ada424",
                            132: "e755a42",
                            133: "e14554c",
                            134: "1bbf114",
                            135: "8b1bcab",
                            136: "febe7db",
                            137: "db79b1f",
                            138: "80b7de2",
                            139: "8834a5e",
                            140: "d066523",
                            141: "a46c607",
                            142: "9d34bfb",
                            143: "4369cbc",
                            144: "6f29203",
                            145: "93d2aaa",
                            146: "ac8d1b1",
                            147: "bd4abd0",
                            148: "d6902c4",
                            149: "3da390e",
                            150: "9c808a1",
                            151: "5318a38",
                            152: "28ce4eb",
                            153: "a3a3ee9",
                            154: "26d0046",
                            155: "5d85e2b",
                            156: "5b860d1",
                            157: "3c1cc30",
                            158: "30f6b22",
                            159: "7f76e49",
                            160: "8638632",
                            161: "c2b2850",
                            162: "d7450aa",
                            163: "6619ce0",
                            164: "00c08b2",
                            165: "2dd0b0f",
                            166: "27a14ad",
                            167: "c11c0ea",
                            168: "710050d",
                            169: "0f525d4",
                            170: "990c207",
                            171: "8b18a42",
                            172: "7aa855b",
                            173: "175dd1f",
                            174: "489ea4d",
                            175: "16a4592",
                            176: "6fd2f55",
                            177: "67ae3a8",
                            178: "9be297a",
                            179: "d3abb38",
                            180: "10d29c0",
                            181: "e41ea08",
                            182: "c903c36",
                            183: "c7d371f",
                            184: "4aa7c62",
                            185: "fa28d94",
                            186: "0f5cb60",
                            187: "eff9908",
                            189: "0f0c032"
                        }[e] + ".js"
                    }(e);
                var d = new Error;
                r = function (n) {
                    script.onerror = script.onload = null,
                        clearTimeout(f);
                    var t = o[e];
                    if (0 !== t) {
                        if (t) {
                            var c = n && ("load" === n.type ? "missing" : n.type)
                                , r = n && n.target && n.target.src;
                            d.message = "Loading chunk " + e + " failed.\n(" + c + ": " + r + ")",
                                d.name = "ChunkLoadError",
                                d.type = c,
                                d.request = r,
                                t[1](d)
                        }
                        o[e] = void 0
                    }
                }
                ;
                var f = setTimeout((function () {
                        r({
                            type: "timeout",
                            target: script
                        })
                    }
                ), 12e4);
                script.onerror = script.onload = r,
                    document.head.appendChild(script)
            }
        return Promise.all(n)
    }
        ,
        l.m = e,
        l.c = c,
        l.d = function (e, n, t) {
            l.o(e, n) || Object.defineProperty(e, n, {
                enumerable: !0,
                get: t
            })
        }
        ,
        l.r = function (e) {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                value: "Module"
            }),
                Object.defineProperty(e, "__esModule", {
                    value: !0
                })
        }
        ,
        l.t = function (e, n) {
            if (1 & n && (e = l(e)),
            8 & n)
                return e;
            if (4 & n && "object" == typeof e && e && e.__esModule)
                return e;
            var t = Object.create(null);
            if (l.r(t),
                Object.defineProperty(t, "default", {
                    enumerable: !0,
                    value: e
                }),
            2 & n && "string" != typeof e)
                for (var c in e)
                    l.d(t, c, function (n) {
                        return e[n]
                    }
                        .bind(null, c));
            return t
        }
        ,
        l.n = function (e) {
            var n = e && e.__esModule ? function () {
                        return e.default
                    }
                    : function () {
                        return e
                    }
            ;
            return l.d(n, "a", n),
                n
        }
        ,
        l.o = function (object, e) {
            return Object.prototype.hasOwnProperty.call(object, e)
        }
        ,
        l.p = "https://static.diandian.com/_common/",
        l.oe = function (e) {
            throw console.error(e),
                e
        }
    ;
    // var d = window.webpackJsonp = window.webpackJsonp || []
    //     , f = d.push.bind(d);
    // d.push = n,
    //     d = d.slice();
    // for (var i = 0; i < d.length; i++)
    //     n(d[i]);
    // var m = f;
    // t();
}(
    jsCode
);

n = window._export_loader
D = n(961)

r = n(3)
console.log(r)
console.log(r.state.u)

params = {
    "business": 1,
    "genre_id": "",
    "sub_genre": "",
    "word": "",
    "page": 2,
    "pagesize": 10
}

params = {
    "business": 2,
    "genre_id": "",
    "sub_genre": "",
    "word": "",
    "page": 3,
    "pagesize": 10
}

function get_sign(params) {
    e = "/app/v1/info/search"
    path = e.replace("/app", "")

    n = {
        "proxy": "/app",
        "target": "",
        "sort": "dd",
        "num": 10,
        "s": "05e4c7ea76ceedd58f7f4c599d8706bb",
        "k": "93d8d4e6b7c6dc6d",
        "l": "6574a4a806feb788",
        "d": 1
    }

    n = {
        "proxy": "/app",
        "target": "",
        "sort": "dd",
        "num": 10,
        "s": "554d80dc64eea78b705ab2f964034645",
        "k": "4a9b37a5ee42ad3d",
        "l": "8d97218d92d23f1a",
        "d": 1
    }

    n = {
    "proxy": "/app",
    "target": "",
    "sort": "dd",
    "num": 10,
    "s": "f54aeab281a40dbb558e239b1a3a3853",
    "k": "67dde041b755f2a9",
    "l": "aba7cbfcd54c7fe4",
    "d": 1
}

    o = Object(D.a)(params, path, {
        s: n.s,
        k: n.k,
        l: n.l,
        d: n.d,
        sort: n.sort,
        num: n.num
    }, 'get');
    return o

}

o = get_sign(params)

console.log("k: " + o)