// @File   :web_pack_dewu.js
// @Time   :2026/1/29 11:47
// @Author :dayue
// @Email  :ole211@qq.com

const func_list_2 = require('./func_list_2')

const jsdom = require('jsdom');
const CryptoJS = require("crypto-js");

const {JSDOM} = jsdom;

const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`, {url: "https://seller.poizon.com/hk"});


window = dom.window
self = window

document = window.document

!(function () {
        var S = func_list_2
            , E = {};

        function r(n) {
            var s = E[n];
            if (s !== void 0)
                return s.exports;
            var e = E[n] = {
                id: n,
                loaded: !1,
                exports: {}
            };
            console.log("n: ", n)
            return S[n].call(e.exports, e, e.exports, r),
                e.loaded = !0,
                e.exports
        }

        window.loader_xxx = r
        r.m = S,
            r.c = E,
            function () {
                var n = typeof Symbol == "function" ? Symbol("webpack queues") : "__webpack_queues__"
                    , s = typeof Symbol == "function" ? Symbol("webpack exports") : "__webpack_exports__"
                    , e = typeof Symbol == "function" ? Symbol("webpack error") : "__webpack_error__"
                    , a = function (i) {
                    i && !i.d && (i.d = 1,
                        i.forEach(function (t) {
                            t.r--
                        }),
                        i.forEach(function (t) {
                            t.r-- ? t.r++ : t()
                        }))
                }
                    , f = function (i) {
                    return i.map(function (t) {
                        if (t !== null && typeof t == "object") {
                            if (t[n])
                                return t;
                            if (t.then) {
                                var u = [];
                                u.d = 0,
                                    t.then(function (c) {
                                        o[s] = c,
                                            a(u)
                                    }, function (c) {
                                        o[e] = c,
                                            a(u)
                                    });
                                var o = {};
                                return o[n] = function (c) {
                                    c(u)
                                }
                                    ,
                                    o
                            }
                        }
                        var _ = {};
                        return _[n] = function () {
                        }
                            ,
                            _[s] = t,
                            _
                    })
                };
                r.a = function (i, t, u) {
                    var o;
                    u && ((o = []).d = 1);
                    var _ = new Set, c = i.exports, d, l, g, b = new Promise(function (v, p) {
                            g = p,
                                l = v
                        }
                    );
                    b[s] = c,
                        b[n] = function (v) {
                            o && v(o),
                                _.forEach(v),
                                b.catch(function () {
                                })
                        }
                        ,
                        i.exports = b,
                        t(function (v) {
                            d = f(v);
                            var p, w = function () {
                                return d.map(function (h) {
                                    if (h[e])
                                        throw h[e];
                                    return h[s]
                                })
                            }, m = new Promise(function (h) {
                                    p = function () {
                                        h(w)
                                    }
                                        ,
                                        p.r = 0;
                                    var x = function (y) {
                                        y !== o && !_.has(y) && (_.add(y),
                                        y && !y.d && (p.r++,
                                            y.push(p)))
                                    };
                                    d.map(function (y) {
                                        y[n](x)
                                    })
                                }
                            );
                            return p.r ? m : w()
                        }, function (v) {
                            v ? g(b[e] = v) : l(c),
                                a(o)
                        }),
                    o && (o.d = 0)
                }
            }(),
            function () {
                r.n = function (n) {
                    var s = n && n.__esModule ? function () {
                                return n.default
                            }
                            : function () {
                                return n
                            }
                    ;
                    return r.d(s, {
                        a: s
                    }),
                        s
                }
            }(),
            function () {
                var n = Object.getPrototypeOf ? function (e) {
                        return Object.getPrototypeOf(e)
                    }
                    : function (e) {
                        return e.__proto__
                    }
                    , s;
                r.t = function (e, a) {
                    if (a & 1 && (e = this(e)),
                    a & 8 || typeof e == "object" && e && (a & 4 && e.__esModule || a & 16 && typeof e.then == "function"))
                        return e;
                    var f = Object.create(null);
                    r.r(f);
                    var i = {};
                    s = s || [null, n({}), n([]), n(n)];
                    for (var t = a & 2 && e; typeof t == "object" && !~s.indexOf(t); t = n(t))
                        Object.getOwnPropertyNames(t).forEach(function (u) {
                            i[u] = function () {
                                return e[u]
                            }
                        });
                    return i.default = function () {
                        return e
                    }
                        ,
                        r.d(f, i),
                        f
                }
            }(),
            function () {
                r.d = function (n, s) {
                    for (var e in s)
                        r.o(s, e) && !r.o(n, e) && Object.defineProperty(n, e, {
                            enumerable: !0,
                            get: s[e]
                        })
                }
            }(),
            function () {
                r.f = {},
                    r.e = function (n) {
                        return Promise.all(Object.keys(r.f).reduce(function (s, e) {
                            return r.f[e](n, s),
                                s
                        }, []))
                    }
            }(),
            function () {
                r.u = function (n) {
                    return "" + ({
                        42: "src__pages__demo__button-auth__index",
                        55: "src__pages__login__track__config",
                        226: "src__pages__login__config__index",
                        349: "src__pages__login__property__index",
                        499: "src__pages__login__track__index",
                        717: "layouts__index",
                        858: "src__pages__index",
                        939: "src__pages__login__index"
                    }[n] || n) + "." + {
                        42: "f7071241",
                        55: "a2a90184",
                        70: "ac902b8a",
                        108: "c422659a",
                        156: "fc56f577",
                        226: "a1b815ea",
                        349: "5808e76c",
                        418: "35d39bac",
                        424: "10463bc3",
                        464: "b73b2faa",
                        499: "417046b8",
                        656: "e834bc5f",
                        675: "315cb2d1",
                        717: "9ba5a034",
                        749: "d60c5454",
                        827: "8eaf8d8c",
                        858: "edeed5c2",
                        907: "4674be0c",
                        939: "4f8b2d88"
                    }[n] + ".async.js"
                }
            }(),
            function () {
                r.miniCssF = function (n) {
                    return "" + ({
                        349: "src__pages__login__property__index",
                        717: "layouts__index",
                        939: "src__pages__login__index"
                    }[n] || n) + "." + {
                        349: "e2eb4445",
                        464: "29cb8e58",
                        675: "4f60ffdc",
                        717: "3bd4bfd6",
                        939: "6ae805f7"
                    }[n] + ".chunk.css"
                }
            }(),
            function () {
                r.g = function () {
                    if (typeof globalThis == "object")
                        return globalThis;
                    try {
                        return this || new Function("return this")()
                    } catch (n) {
                        if (typeof window == "object")
                            return window
                    }
                }()
            }(),
            function () {
                r.o = function (n, s) {
                    return Object.prototype.hasOwnProperty.call(n, s)
                }
            }(),
            function () {
                var n = {}
                    , s = "@global/global-platform:";
                r.l = function (e, a, f, i) {
                    if (n[e]) {
                        n[e].push(a);
                        return
                    }
                    var t, u;
                    if (f !== void 0)
                        for (var o = document.getElementsByTagName("script"), _ = 0; _ < o.length; _++) {
                            var c = o[_];
                            if (c.getAttribute("src") == e || c.getAttribute("data-webpack") == s + f) {
                                t = c;
                                break
                            }
                        }
                    t || (u = !0,
                        t = document.createElement("script"),
                        t.charset = "utf-8",
                        t.timeout = 120,
                    r.nc && t.setAttribute("nonce", r.nc),
                        t.setAttribute("data-webpack", s + f),
                        t.src = e),
                        n[e] = [a];
                    var d = function (g, b) {
                        t.onerror = t.onload = null,
                            clearTimeout(l);
                        var v = n[e];
                        if (delete n[e],
                        t.parentNode && t.parentNode.removeChild(t),
                        v && v.forEach(function (p) {
                            return p(b)
                        }),
                            g)
                            return g(b)
                    }
                        , l = setTimeout(d.bind(null, void 0, {
                        type: "timeout",
                        target: t
                    }), 12e4);
                    t.onerror = d.bind(null, t.onerror),
                        t.onload = d.bind(null, t.onload),
                    u && document.head.appendChild(t)
                }
            }(),
            function () {
                r.r = function (n) {
                    typeof Symbol != "undefined" && Symbol.toStringTag && Object.defineProperty(n, Symbol.toStringTag, {
                        value: "Module"
                    }),
                        Object.defineProperty(n, "__esModule", {
                            value: !0
                        })
                }
            }(),
            function () {
                r.nmd = function (n) {
                    return n.paths = [],
                    n.children || (n.children = []),
                        n
                }
            }(),
            function () {
                var n = {}
                    , s = {};
                r.f.remotes = function (e, a) {
                    r.o(n, e) && n[e].forEach(function (f) {
                        var i = r.R;
                        i || (i = []);
                        var t = s[f];
                        if (!(i.indexOf(t) >= 0)) {
                            if (i.push(t),
                                t.p)
                                return a.push(t.p);
                            var u = function (l) {
                                l || (l = new Error("Container missing")),
                                typeof l.message == "string" && (l.message += `
while loading "` + t[1] + '" from ' + t[2]),
                                    r.m[f] = function () {
                                        throw l
                                    }
                                    ,
                                    t.p = 0
                            }
                                , o = function (l, g, b, v, p, w) {
                                try {
                                    var m = l(g, b);
                                    if (m && m.then) {
                                        var h = m.then(function (x) {
                                            return p(x, v)
                                        }, u);
                                        if (w)
                                            a.push(t.p = h);
                                        else
                                            return h
                                    } else
                                        return p(m, v, w)
                                } catch (x) {
                                    u(x)
                                }
                            }
                                , _ = function (l, g, b) {
                                return l ? o(r.I, t[0], 0, l, c, b) : u()
                            }
                                , c = function (l, g, b) {
                                return o(g.get, t[1], i, 0, d, b)
                            }
                                , d = function (l) {
                                t.p = 1,
                                    r.m[f] = function (g) {
                                        g.exports = l()
                                    }
                            };
                            o(r, t[2], 0, 0, _, 1)
                        }
                    })
                }
            }(),
            function () {
                r.S = {};
                var n = {}
                    , s = {};
                r.I = function (e, a) {
                    a || (a = []);
                    var f = s[e];
                    if (f || (f = s[e] = {}),
                        !(a.indexOf(f) >= 0)) {
                        if (a.push(f),
                            n[e])
                            return n[e];
                        r.o(r.S, e) || (r.S[e] = {});
                        var i = r.S[e]
                            , t = function (d) {
                            return typeof console != "undefined" && console.warn && console.warn(d)
                        }
                            , u = "@global/global-platform"
                            , o = function (d, l, g, b) {
                            var v = i[d] = i[d] || {}
                                , p = v[l];
                            (!p || !p.loaded && (!b != !p.eager ? b : u > p.from)) && (v[l] = {
                                get: g,
                                from: u,
                                eager: !!b
                            })
                        }
                            , _ = function (d) {
                            var l = function (p) {
                                t("Initialization of sharing external failed: " + p)
                            };
                            try {
                                var g = r(d);
                                if (!g)
                                    return;
                                var b = function (p) {
                                    return p && p.init && p.init(r.S[e], a)
                                };
                                if (g.then)
                                    return c.push(g.then(b, l));
                                var v = b(g);
                                if (v && v.then)
                                    return c.push(v.catch(l))
                            } catch (p) {
                                l(p)
                            }
                        }
                            , c = [];
                        switch (e) {
                        }
                        return c.length ? n[e] = Promise.all(c).then(function () {
                            return n[e] = 1
                        }) : n[e] = 1
                    }
                }
            }(),
            function () {
                r.p = "https://cdn-static.poizon.com/global-platform/"
            }(),
            function () {
                var n = function (f, i, t, u) {
                    var o = document.createElement("link");
                    o.rel = "stylesheet",
                        o.type = "text/css";
                    var _ = function (c) {
                        if (o.onerror = o.onload = null,
                        c.type === "load")
                            t();
                        else {
                            var d = c && (c.type === "load" ? "missing" : c.type)
                                , l = c && c.target && c.target.href || i
                                , g = new Error("Loading CSS chunk " + f + ` failed.
(` + l + ")");
                            g.code = "CSS_CHUNK_LOAD_FAILED",
                                g.type = d,
                                g.request = l,
                                o.parentNode.removeChild(o),
                                u(g)
                        }
                    };
                    return o.onerror = o.onload = _,
                        o.href = i,
                        document.head.appendChild(o),
                        o
                }
                    , s = function (f, i) {
                    for (var t = document.getElementsByTagName("link"), u = 0; u < t.length; u++) {
                        var o = t[u]
                            , _ = o.getAttribute("data-href") || o.getAttribute("href");
                        if (o.rel === "stylesheet" && (_ === f || _ === i))
                            return o
                    }
                    for (var c = document.getElementsByTagName("style"), u = 0; u < c.length; u++) {
                        var o = c[u]
                            , _ = o.getAttribute("data-href");
                        if (_ === f || _ === i)
                            return o
                    }
                }
                    , e = function (f) {
                    return new Promise(function (i, t) {
                            var u = r.miniCssF(f)
                                , o = r.p + u;
                            if (s(u, o))
                                return i();
                            n(f, o, i, t)
                        }
                    )
                }
                    , a = {
                    620: 0
                };
                r.f.miniCss = function (f, i) {
                    var t = {
                        349: 1,
                        464: 1,
                        675: 1,
                        717: 1,
                        939: 1
                    };
                    a[f] ? i.push(a[f]) : a[f] !== 0 && t[f] && i.push(a[f] = e(f).then(function () {
                        a[f] = 0
                    }, function (u) {
                        throw delete a[f],
                            u
                    }))
                }
            }(),
            function () {
                var n = {
                    620: 0
                };
                r.f.j = function (a, f) {
                    var i = r.o(n, a) ? n[a] : void 0;
                    if (i !== 0)
                        if (i)
                            f.push(i[2]);
                        else if (a != 939) {
                            var t = new Promise(function (c, d) {
                                    i = n[a] = [c, d]
                                }
                            );
                            f.push(i[2] = t);
                            var u = r.p + r.u(a)
                                , o = new Error
                                , _ = function (c) {
                                if (r.o(n, a) && (i = n[a],
                                i !== 0 && (n[a] = void 0),
                                    i)) {
                                    var d = c && (c.type === "load" ? "missing" : c.type)
                                        , l = c && c.target && c.target.src;
                                    o.message = "Loading chunk " + a + ` failed.
(` + d + ": " + l + ")",
                                        o.name = "ChunkLoadError",
                                        o.type = d,
                                        o.request = l,
                                        i[1](o)
                                }
                            };
                            r.l(u, _, "chunk-" + a, a)
                        } else
                            n[a] = 0
                }
                ;
                var s = function (a, f) {
                    var i = f[0], t = f[1], u = f[2], o, _, c = 0;
                    if (i.some(function (l) {
                        return n[l] !== 0
                    })) {
                        for (o in t)
                            r.o(t, o) && (r.m[o] = t[o]);
                        if (u)
                            var d = u(r)
                    }
                    for (a && a(f); c < i.length; c++)
                        _ = i[c],
                        r.o(n, _) && n[_] && n[_][0](),
                            n[_] = 0
                }
                    , e = self.webpackChunk_global_global_platform = self.webpackChunk_global_global_platform || [];
                e.forEach(s.bind(null, 0)),
                    e.push = s.bind(null, e.push.bind(e))
            }();
        // 注释掉这行！它触发了不需要的远程资源加载
        // var C = r(21627)
    }
)(
);

//# sourceMappingURL=umi.7d875d66.js.map


function str2md5(s) {
    return CryptoJS.MD5(s).toString()
}


function wordsToBytes(u) {
    for (var i = [], a = 0; a < u.length * 32; a += 8)
        i.push(u[a >>> 5] >>> 24 - a % 32 & 255);
    return i
}


var u = window.loader_xxx(1048)
    , i = window.loader_xxx(6636).utf8
    , a = window.loader_xxx(84331)
    , l = window.loader_xxx(6636).bin
    , c = function (p, h) {
    p.constructor == String ? h && h.encoding === "binary" ? p = l.stringToBytes(p) : p = i.stringToBytes(p) : a(p) ? p = Array.prototype.slice.call(p, 0) : !Array.isArray(p) && p.constructor !== Uint8Array && (p = p.toString());
    for (var f = u.bytesToWords(p), v = p.length * 8, S = 1732584193, y = -271733879, w = -1732584194, E = 271733878, x = 0; x < f.length; x++)
        f[x] = (f[x] << 8 | f[x] >>> 24) & 16711935 | (f[x] << 24 | f[x] >>> 8) & 4278255360;
    f[v >>> 5] |= 128 << v % 32,
        f[(v + 64 >>> 9 << 4) + 14] = v;
    for (var T = c._ff, D = c._gg, F = c._hh, M = c._ii, x = 0; x < f.length; x += 16) {
        var N = S
            , $ = y
            , R = w
            , b = E;
        console.log(T)
        S = T(S, y, w, E, f[x + 0], 7, -680876936),
            E = T(E, S, y, w, f[x + 1], 12, -389564586),
            w = T(w, E, S, y, f[x + 2], 17, 606105819),
            y = T(y, w, E, S, f[x + 3], 22, -1044525330),
            S = T(S, y, w, E, f[x + 4], 7, -176418897),
            E = T(E, S, y, w, f[x + 5], 12, 1200080426),
            w = T(w, E, S, y, f[x + 6], 17, -1473231341),
            y = T(y, w, E, S, f[x + 7], 22, -45705983),
            S = T(S, y, w, E, f[x + 8], 7, 1770035416),
            E = T(E, S, y, w, f[x + 9], 12, -1958414417),
            w = T(w, E, S, y, f[x + 10], 17, -42063),
            y = T(y, w, E, S, f[x + 11], 22, -1990404162),
            S = T(S, y, w, E, f[x + 12], 7, 1804603682),
            E = T(E, S, y, w, f[x + 13], 12, -40341101),
            w = T(w, E, S, y, f[x + 14], 17, -1502002290),
            y = T(y, w, E, S, f[x + 15], 22, 1236535329),
            S = D(S, y, w, E, f[x + 1], 5, -165796510),
            E = D(E, S, y, w, f[x + 6], 9, -1069501632),
            w = D(w, E, S, y, f[x + 11], 14, 643717713),
            y = D(y, w, E, S, f[x + 0], 20, -373897302),
            S = D(S, y, w, E, f[x + 5], 5, -701558691),
            E = D(E, S, y, w, f[x + 10], 9, 38016083),
            w = D(w, E, S, y, f[x + 15], 14, -660478335),
            y = D(y, w, E, S, f[x + 4], 20, -405537848),
            S = D(S, y, w, E, f[x + 9], 5, 568446438),
            E = D(E, S, y, w, f[x + 14], 9, -1019803690),
            w = D(w, E, S, y, f[x + 3], 14, -187363961),
            y = D(y, w, E, S, f[x + 8], 20, 1163531501),
            S = D(S, y, w, E, f[x + 13], 5, -1444681467),
            E = D(E, S, y, w, f[x + 2], 9, -51403784),
            w = D(w, E, S, y, f[x + 7], 14, 1735328473),
            y = D(y, w, E, S, f[x + 12], 20, -1926607734),
            S = F(S, y, w, E, f[x + 5], 4, -378558),
            E = F(E, S, y, w, f[x + 8], 11, -2022574463),
            w = F(w, E, S, y, f[x + 11], 16, 1839030562),
            y = F(y, w, E, S, f[x + 14], 23, -35309556),
            S = F(S, y, w, E, f[x + 1], 4, -1530992060),
            E = F(E, S, y, w, f[x + 4], 11, 1272893353),
            w = F(w, E, S, y, f[x + 7], 16, -155497632),
            y = F(y, w, E, S, f[x + 10], 23, -1094730640),
            S = F(S, y, w, E, f[x + 13], 4, 681279174),
            E = F(E, S, y, w, f[x + 0], 11, -358537222),
            w = F(w, E, S, y, f[x + 3], 16, -722521979),
            y = F(y, w, E, S, f[x + 6], 23, 76029189),
            S = F(S, y, w, E, f[x + 9], 4, -640364487),
            E = F(E, S, y, w, f[x + 12], 11, -421815835),
            w = F(w, E, S, y, f[x + 15], 16, 530742520),
            y = F(y, w, E, S, f[x + 2], 23, -995338651),
            S = M(S, y, w, E, f[x + 0], 6, -198630844),
            E = M(E, S, y, w, f[x + 7], 10, 1126891415),
            w = M(w, E, S, y, f[x + 14], 15, -1416354905),
            y = M(y, w, E, S, f[x + 5], 21, -57434055),
            S = M(S, y, w, E, f[x + 12], 6, 1700485571),
            E = M(E, S, y, w, f[x + 3], 10, -1894986606),
            w = M(w, E, S, y, f[x + 10], 15, -1051523),
            y = M(y, w, E, S, f[x + 1], 21, -2054922799),
            S = M(S, y, w, E, f[x + 8], 6, 1873313359),
            E = M(E, S, y, w, f[x + 15], 10, -30611744),
            w = M(w, E, S, y, f[x + 6], 15, -1560198380),
            y = M(y, w, E, S, f[x + 13], 21, 1309151649),
            S = M(S, y, w, E, f[x + 4], 6, -145523070),
            E = M(E, S, y, w, f[x + 11], 10, -1120210379),
            w = M(w, E, S, y, f[x + 2], 15, 718787259),
            y = M(y, w, E, S, f[x + 9], 21, -343485551),
            S = S + N >>> 0,
            y = y + $ >>> 0,
            w = w + R >>> 0,
            E = E + b >>> 0
    }
    return u.endian([S, y, w, E])
};
c._ff = function (p, h, f, v, S, y, w) {
    var E = p + (h & f | ~h & v) + (S >>> 0) + w;
    return (E << y | E >>> 32 - y) + h
}
    ,
    c._gg = function (p, h, f, v, S, y, w) {
        var E = p + (h & v | f & ~v) + (S >>> 0) + w;
        return (E << y | E >>> 32 - y) + h
    }
    ,
    c._hh = function (p, h, f, v, S, y, w) {
        var E = p + (h ^ f ^ v) + (S >>> 0) + w;
        return (E << y | E >>> 32 - y) + h
    }
    ,
    c._ii = function (p, h, f, v, S, y, w) {
        var E = p + (f ^ (h | ~v)) + (S >>> 0) + w;
        return (E << y | E >>> 32 - y) + h
    }
    ,
    c._blocksize = 16,
    c._digestsize = 16;


function w(p, h) {
    if (p == null)
        throw new Error("Illegal argument " + p);
    var f = wordsToBytes(c(p, h));
    return h && h.asBytes ? f : h && h.asString ? l.bytesToString(f) : u.bytesToHex(f)
}


function Pt(H, le = !1, ve = "048a9c4943398714b356a696503d2d36") {
    if (typeof le == "string" && typeof ve == "boolean") {
        const rt = le;
        le = ve,
            ve = rt
    }
    le && console.log("\u8F6C\u5316\u524Dparams=", H);
    const je = (rt, Ut) => Ut === null ? void 0 : Ut
        , Ye = rt => {
            if ([void 0, null, ""].includes(rt))
                return "";
            if (Object.prototype.toString.call(rt) === "[object Object]")
                return JSON.stringify(rt, je);
            if (Array.isArray(rt)) {
                let Ut = "";
                return rt.forEach((_t, dt) => {
                        Object.prototype.toString.call(_t) === "[object Object]" || Array.isArray(_t) ? Ut += JSON.stringify(_t, je) : [void 0, null].includes(_t) ? Ut += null : Ut += _t.toString(),
                        dt < rt.length - 1 && (Ut += ",")
                    }
                ),
                    Ut
            }
            return rt.toString()
        }
    ;
    let Qe = Object.keys(H).sort().reduce((rt, Ut) => H[Ut] === void 0 ? rt : rt + Ut + Ye(H[Ut]), "");
    return le && (console.log("\u8F6C\u5316\u540EparamsToken=", Qe),
        console.log("salt=", ve)),
    /[\u00A0\u3000]/g.test(Qe) && console.warn("\u9A8C\u7B7E\u8B66\u544A\uFF1A\u8BF7\u5148\u53BB\u9664\u975E\u6CD5\u5B57\u7B26\\u00A0\uFF0C\\u3000"),
        Qe += ve,
        w(Qe)
}


function getSign(data_rt, dt = false, le = "048a9c4943398714b356a696503d2d36") {
    return Pt(data_rt, dt, le)
}


function encodePassword(s) {
    return str2md5(s + "du")
}

function encodeAppPassword(s) {
    return str2md5(s)
}


ss = "qweasd111"

console.log(encodePassword(ss))


data_rt = {
    "areaCode": "+86",
    "mobile": "18636396636",
    "region": "HK",
    "password": "f12c2df9692ec56ccd6a7abadafd10a0",
    "appPassword": "832752e44215fb9f32e5471d7b03c56b",
    "userType": 2
}
dt = false
le = "048a9c4943398714b356a696503d2d36"

console.log(getSign(data_rt))

dom.window.close(); // 释放 jsdom 内部资源