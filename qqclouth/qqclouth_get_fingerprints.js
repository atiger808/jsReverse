// @File   :qqclouth_get_fingerprints.js
// @Time   :2025/10/18 21:15
// @Author :dayue
// @Email  :ole211@qq.com


function cp(e) {
    e.then(void 0, (function () {
        }
    ))
}

function up(e, t) {
    e = [e[0] >>> 16, 65535 & e[0], e[1] >>> 16, 65535 & e[1]],
        t = [t[0] >>> 16, 65535 & t[0], t[1] >>> 16, 65535 & t[1]];
    var r = [0, 0, 0, 0];
    return r[3] += e[3] + t[3],
        r[2] += r[3] >>> 16,
        r[3] &= 65535,
        r[2] += e[2] + t[2],
        r[1] += r[2] >>> 16,
        r[2] &= 65535,
        r[1] += e[1] + t[1],
        r[0] += r[1] >>> 16,
        r[1] &= 65535,
        r[0] += e[0] + t[0],
        r[0] &= 65535,
        [r[0] << 16 | r[1], r[2] << 16 | r[3]]
}

function lp(e, t) {
    e = [e[0] >>> 16, 65535 & e[0], e[1] >>> 16, 65535 & e[1]],
        t = [t[0] >>> 16, 65535 & t[0], t[1] >>> 16, 65535 & t[1]];
    var r = [0, 0, 0, 0];
    return r[3] += e[3] * t[3],
        r[2] += r[3] >>> 16,
        r[3] &= 65535,
        r[2] += e[2] * t[3],
        r[1] += r[2] >>> 16,
        r[2] &= 65535,
        r[2] += e[3] * t[2],
        r[1] += r[2] >>> 16,
        r[2] &= 65535,
        r[1] += e[1] * t[3],
        r[0] += r[1] >>> 16,
        r[1] &= 65535,
        r[1] += e[2] * t[2],
        r[0] += r[1] >>> 16,
        r[1] &= 65535,
        r[1] += e[3] * t[1],
        r[0] += r[1] >>> 16,
        r[1] &= 65535,
        r[0] += e[0] * t[3] + e[1] * t[2] + e[2] * t[1] + e[3] * t[0],
        r[0] &= 65535,
        [r[0] << 16 | r[1], r[2] << 16 | r[3]]
}

function dp(e, t) {
    return 32 == (t %= 64) ? [e[1], e[0]] : t < 32 ? [e[0] << t | e[1] >>> 32 - t, e[1] << t | e[0] >>> 32 - t] : (t -= 32,
        [e[1] << t | e[0] >>> 32 - t, e[0] << t | e[1] >>> 32 - t])
}

function pp(e, t) {
    return 0 == (t %= 64) ? e : t < 32 ? [e[0] << t | e[1] >>> 32 - t, e[1] << t] : [e[1] << t - 32, 0]
}

function hp(e, t) {
    return [e[0] ^ t[0], e[1] ^ t[1]]
}

function fp(e) {
    return e = hp(e, [0, e[0] >>> 1]),
        e = hp(e = lp(e, [4283543511, 3981806797]), [0, e[0] >>> 1]),
        hp(e = lp(e, [3301882366, 444984403]), [0, e[0] >>> 1])
}

function vp(e) {
    return parseInt(e)
}

function mp(e) {
    return parseFloat(e)
}

function gp(e, t) {
    return "number" == typeof e && isNaN(e) ? t : e
}

function yp(e) {
    return e.reduce((function (e, t) {
            return e + (t ? 1 : 0)
        }
    ), 0)
}

function Ep(e) {
    return e && "object" == typeof e && "message" in e ? e : {
        message: e
    }
}

function bp(e, t, r) {
    var n = Object.keys(e).filter((function (e) {
            return !function (e, t) {
                for (var r = 0, n = e.length; r < n; ++r)
                    if (e[r] === t)
                        return !0;
                return !1
            }(r, e)
        }
    ))
        , i = sp(n, (function (r) {
            return function (e, t) {
                var r = new Promise((function (r) {
                        var n = Date.now();
                        ap(e.bind(null, t), (function () {
                                for (var e = [], t = 0; t < arguments.length; t++)
                                    e[t] = arguments[t];
                                var i = Date.now() - n;
                                if (!e[0])
                                    return r((function () {
                                            return {
                                                error: Ep(e[1]),
                                                duration: i
                                            }
                                        }
                                    ));
                                var o = e[1];
                                if (function (e) {
                                    return "function" != typeof e
                                }(o))
                                    return r((function () {
                                            return {
                                                value: o,
                                                duration: i
                                            }
                                        }
                                    ));
                                r((function () {
                                        return new Promise((function (e) {
                                                var t = Date.now();
                                                ap(o, (function () {
                                                        for (var r = [], n = 0; n < arguments.length; n++)
                                                            r[n] = arguments[n];
                                                        var o = i + Date.now() - t;
                                                        if (!r[0])
                                                            return e({
                                                                error: Ep(r[1]),
                                                                duration: o
                                                            });
                                                        e({
                                                            value: r[1],
                                                            duration: o
                                                        })
                                                    }
                                                ))
                                            }
                                        ))
                                    }
                                ))
                            }
                        ))
                    }
                ));
                return cp(r),
                    function () {
                        return r.then((function (e) {
                                return e()
                            }
                        ))
                    }
            }(e[r], t)
        }
    ));
    return cp(i),
        function () {
            return tp(this, void 0, void 0, (function () {
                    var e, t, r, o;
                    return rp(this, (function (a) {
                            switch (a.label) {
                                case 0:
                                    return [4, i];
                                case 1:
                                    return [4, sp(a.sent(), (function (e) {
                                            var t = e();
                                            return cp(t),
                                                t
                                        }
                                    ))];
                                case 2:
                                    return e = a.sent(),
                                        [4, Promise.all(e)];
                                case 3:
                                    for (t = a.sent(),
                                             r = {},
                                             o = 0; o < n.length; ++o)
                                        r[n[o]] = t[o];
                                    return [2, r]
                            }
                        }
                    ))
                }
            ))
        }
}

function Cp() {
    var e = window
        , t = navigator;
    return yp(["MSCSSMatrix" in e, "msSetImmediate" in e, "msIndexedDB" in e, "msMaxTouchPoints" in t, "msPointerEnabled" in t]) >= 4
}

function Zp(e) {
    return function (e, t) {
        t = t || 0;
        var r, n = (e = e || "").length % 16, i = e.length - n, o = [0, t], a = [0, t], s = [0, 0], c = [0, 0],
            u = [2277735313, 289559509], l = [1291169091, 658871167];
        for (r = 0; r < i; r += 16)
            s = [255 & e.charCodeAt(r + 4) | (255 & e.charCodeAt(r + 5)) << 8 | (255 & e.charCodeAt(r + 6)) << 16 | (255 & e.charCodeAt(r + 7)) << 24, 255 & e.charCodeAt(r) | (255 & e.charCodeAt(r + 1)) << 8 | (255 & e.charCodeAt(r + 2)) << 16 | (255 & e.charCodeAt(r + 3)) << 24],
                c = [255 & e.charCodeAt(r + 12) | (255 & e.charCodeAt(r + 13)) << 8 | (255 & e.charCodeAt(r + 14)) << 16 | (255 & e.charCodeAt(r + 15)) << 24, 255 & e.charCodeAt(r + 8) | (255 & e.charCodeAt(r + 9)) << 8 | (255 & e.charCodeAt(r + 10)) << 16 | (255 & e.charCodeAt(r + 11)) << 24],
                s = dp(s = lp(s, u), 31),
                o = up(o = dp(o = hp(o, s = lp(s, l)), 27), a),
                o = up(lp(o, [0, 5]), [0, 1390208809]),
                c = dp(c = lp(c, l), 33),
                a = up(a = dp(a = hp(a, c = lp(c, u)), 31), o),
                a = up(lp(a, [0, 5]), [0, 944331445]);
        switch (s = [0, 0],
            c = [0, 0],
            n) {
            case 15:
                c = hp(c, pp([0, e.charCodeAt(r + 14)], 48));
            case 14:
                c = hp(c, pp([0, e.charCodeAt(r + 13)], 40));
            case 13:
                c = hp(c, pp([0, e.charCodeAt(r + 12)], 32));
            case 12:
                c = hp(c, pp([0, e.charCodeAt(r + 11)], 24));
            case 11:
                c = hp(c, pp([0, e.charCodeAt(r + 10)], 16));
            case 10:
                c = hp(c, pp([0, e.charCodeAt(r + 9)], 8));
            case 9:
                c = lp(c = hp(c, [0, e.charCodeAt(r + 8)]), l),
                    a = hp(a, c = lp(c = dp(c, 33), u));
            case 8:
                s = hp(s, pp([0, e.charCodeAt(r + 7)], 56));
            case 7:
                s = hp(s, pp([0, e.charCodeAt(r + 6)], 48));
            case 6:
                s = hp(s, pp([0, e.charCodeAt(r + 5)], 40));
            case 5:
                s = hp(s, pp([0, e.charCodeAt(r + 4)], 32));
            case 4:
                s = hp(s, pp([0, e.charCodeAt(r + 3)], 24));
            case 3:
                s = hp(s, pp([0, e.charCodeAt(r + 2)], 16));
            case 2:
                s = hp(s, pp([0, e.charCodeAt(r + 1)], 8));
            case 1:
                s = lp(s = hp(s, [0, e.charCodeAt(r)]), u),
                    o = hp(o, s = lp(s = dp(s, 31), l))
        }
        return o = up(o = hp(o, [0, e.length]), a = hp(a, [0, e.length])),
            a = up(a, o),
            o = up(o = fp(o), a = fp(a)),
            a = up(a, o),
        ("00000000" + (o[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (o[1] >>> 0).toString(16)).slice(-8) + ("00000000" + (a[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (a[1] >>> 0).toString(16)).slice(-8)
    }(function (e) {
        for (var t = "", r = 0, n = Object.keys(e).sort(); r < n.length; r++) {
            var i = n[r]
                , o = e[i]
                , a = o.error ? "error" : JSON.stringify(o.value);
            t += "".concat(t ? "|" : "").concat(i.replace(/([:|\\])/g, "\\$1"), ":").concat(a)
        }
        return t
    }(e))
}

a = {
    x64hash128: function (e, t) {
        t = t || 0;
        for (var r = (e = e || "").length % 16, n = e.length - r, i = [0, t], o = [0, t], a = [0, 0], s = [0, 0], c = [2277735313, 289559509], u = [1291169091, 658871167], l = 0; l < n; l += 16)
            a = [255 & e.charCodeAt(l + 4) | (255 & e.charCodeAt(l + 5)) << 8 | (255 & e.charCodeAt(l + 6)) << 16 | (255 & e.charCodeAt(l + 7)) << 24, 255 & e.charCodeAt(l) | (255 & e.charCodeAt(l + 1)) << 8 | (255 & e.charCodeAt(l + 2)) << 16 | (255 & e.charCodeAt(l + 3)) << 24],
                s = [255 & e.charCodeAt(l + 12) | (255 & e.charCodeAt(l + 13)) << 8 | (255 & e.charCodeAt(l + 14)) << 16 | (255 & e.charCodeAt(l + 15)) << 24, 255 & e.charCodeAt(l + 8) | (255 & e.charCodeAt(l + 9)) << 8 | (255 & e.charCodeAt(l + 10)) << 16 | (255 & e.charCodeAt(l + 11)) << 24],
                a = this.x64Multiply(a, c),
                a = this.x64Rotl(a, 31),
                a = this.x64Multiply(a, u),
                i = this.x64Xor(i, a),
                i = this.x64Rotl(i, 27),
                i = this.x64Add(i, o),
                i = this.x64Add(this.x64Multiply(i, [0, 5]), [0, 1390208809]),
                s = this.x64Multiply(s, u),
                s = this.x64Rotl(s, 33),
                s = this.x64Multiply(s, c),
                o = this.x64Xor(o, s),
                o = this.x64Rotl(o, 31),
                o = this.x64Add(o, i),
                o = this.x64Add(this.x64Multiply(o, [0, 5]), [0, 944331445]);
        switch (a = [0, 0],
            s = [0, 0],
            r) {
            case 15:
                s = this.x64Xor(s, this.x64LeftShift([0, e.charCodeAt(l + 14)], 48));
            case 14:
                s = this.x64Xor(s, this.x64LeftShift([0, e.charCodeAt(l + 13)], 40));
            case 13:
                s = this.x64Xor(s, this.x64LeftShift([0, e.charCodeAt(l + 12)], 32));
            case 12:
                s = this.x64Xor(s, this.x64LeftShift([0, e.charCodeAt(l + 11)], 24));
            case 11:
                s = this.x64Xor(s, this.x64LeftShift([0, e.charCodeAt(l + 10)], 16));
            case 10:
                s = this.x64Xor(s, this.x64LeftShift([0, e.charCodeAt(l + 9)], 8));
            case 9:
                s = this.x64Xor(s, [0, e.charCodeAt(l + 8)]),
                    s = this.x64Multiply(s, u),
                    s = this.x64Rotl(s, 33),
                    s = this.x64Multiply(s, c),
                    o = this.x64Xor(o, s);
            case 8:
                a = this.x64Xor(a, this.x64LeftShift([0, e.charCodeAt(l + 7)], 56));
            case 7:
                a = this.x64Xor(a, this.x64LeftShift([0, e.charCodeAt(l + 6)], 48));
            case 6:
                a = this.x64Xor(a, this.x64LeftShift([0, e.charCodeAt(l + 5)], 40));
            case 5:
                a = this.x64Xor(a, this.x64LeftShift([0, e.charCodeAt(l + 4)], 32));
            case 4:
                a = this.x64Xor(a, this.x64LeftShift([0, e.charCodeAt(l + 3)], 24));
            case 3:
                a = this.x64Xor(a, this.x64LeftShift([0, e.charCodeAt(l + 2)], 16));
            case 2:
                a = this.x64Xor(a, this.x64LeftShift([0, e.charCodeAt(l + 1)], 8));
            case 1:
                a = this.x64Xor(a, [0, e.charCodeAt(l)]),
                    a = this.x64Multiply(a, c),
                    a = this.x64Rotl(a, 31),
                    a = this.x64Multiply(a, u),
                    i = this.x64Xor(i, a)
        }
        return i = this.x64Xor(i, [0, e.length]),
            o = this.x64Xor(o, [0, e.length]),
            i = this.x64Add(i, o),
            o = this.x64Add(o, i),
            i = this.x64Fmix(i),
            o = this.x64Fmix(o),
            i = this.x64Add(i, o),
            o = this.x64Add(o, i),
        ("00000000" + (i[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (i[1] >>> 0).toString(16)).slice(-8) + ("00000000" + (o[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (o[1] >>> 0).toString(16)).slice(-8)
    },
    x64Multiply: function (e, t) {
        e = [e[0] >>> 16, 65535 & e[0], e[1] >>> 16, 65535 & e[1]],
            t = [t[0] >>> 16, 65535 & t[0], t[1] >>> 16, 65535 & t[1]];
        var r = [0, 0, 0, 0];
        return r[3] += e[3] * t[3],
            r[2] += r[3] >>> 16,
            r[3] &= 65535,
            r[2] += e[2] * t[3],
            r[1] += r[2] >>> 16,
            r[2] &= 65535,
            r[2] += e[3] * t[2],
            r[1] += r[2] >>> 16,
            r[2] &= 65535,
            r[1] += e[1] * t[3],
            r[0] += r[1] >>> 16,
            r[1] &= 65535,
            r[1] += e[2] * t[2],
            r[0] += r[1] >>> 16,
            r[1] &= 65535,
            r[1] += e[3] * t[1],
            r[0] += r[1] >>> 16,
            r[1] &= 65535,
            r[0] += e[0] * t[3] + e[1] * t[2] + e[2] * t[1] + e[3] * t[0],
            r[0] &= 65535,
            [r[0] << 16 | r[1], r[2] << 16 | r[3]]
    },
    x64Rotl: function (e, t) {
        return 32 == (t %= 64) ? [e[1], e[0]] : t < 32 ? [e[0] << t | e[1] >>> 32 - t, e[1] << t | e[0] >>> 32 - t] : (t -= 32,
            [e[1] << t | e[0] >>> 32 - t, e[0] << t | e[1] >>> 32 - t])
    },
    x64LeftShift: function (e, t) {
        return 0 == (t %= 64) ? e : t < 32 ? [e[0] << t | e[1] >>> 32 - t, e[1] << t] : [e[1] << t - 32, 0]
    },
    x64Xor: function (e, t) {
        return [e[0] ^ t[0], e[1] ^ t[1]]
    },
    x64Fmix: function (e) {
        return e = this.x64Xor(e, [0, e[0] >>> 1]),
            e = this.x64Multiply(e, [4283543511, 3981806797]),
            e = this.x64Xor(e, [0, e[0] >>> 1]),
            e = this.x64Multiply(e, [3301882366, 444984403]),
            this.x64Xor(e, [0, e[0] >>> 1])
    },
    x64Add: function (e, t) {
        e = [e[0] >>> 16, 65535 & e[0], e[1] >>> 16, 65535 & e[1]],
            t = [t[0] >>> 16, 65535 & t[0], t[1] >>> 16, 65535 & t[1]];
        var r = [0, 0, 0, 0];
        return r[3] += e[3] + t[3],
            r[2] += r[3] >>> 16,
            r[3] &= 65535,
            r[2] += e[2] + t[2],
            r[1] += r[2] >>> 16,
            r[2] &= 65535,
            r[1] += e[1] + t[1],
            r[0] += r[1] >>> 16,
            r[1] &= 65535,
            r[0] += e[0] + t[0],
            r[0] &= 65535,
            [r[0] << 16 | r[1], r[2] << 16 | r[3]]
    },

}

t1 = [
    {
        "key": "user_agent",
        "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    },
    {
        "key": "language",
        "value": "zh-CN"
    },
    {
        "key": "resolution",
        "value": [
            1920,
            1080
        ]
    },
    {
        "key": "available_resolution",
        "value": [
            1920,
            1040
        ]
    },
    {
        "key": "timezone_offset",
        "value": -480
    },
    {
        "key": "navigator_platform",
        "value": "Win32"
    },
    {
        "key": "regular_plugins",
        "value": [
            "PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf",
            "Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf",
            "Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf",
            "Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf",
            "WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"
        ]
    },
    {
        "key": "adblock",
        "value": false
    },
    {
        "key": "touch_support",
        "value": [
            0,
            false,
            false
        ]
    },
    {
        "key": "js_fonts",
        "value": [
            "Arial",
            "Arial Black",
            "Arial Narrow",
            "Calibri",
            "Cambria",
            "Cambria Math",
            "Comic Sans MS",
            "Consolas",
            "Courier",
            "Courier New",
            "Georgia",
            "Helvetica",
            "Impact",
            "Lucida Console",
            "Lucida Sans Unicode",
            "Microsoft Sans Serif",
            "MS Gothic",
            "MS PGothic",
            "MS Sans Serif",
            "MS Serif",
            "Palatino Linotype",
            "Segoe Print",
            "Segoe Script",
            "Segoe UI",
            "Segoe UI Light",
            "Segoe UI Semibold",
            "Segoe UI Symbol",
            "Tahoma",
            "Times",
            "Times New Roman",
            "Trebuchet MS",
            "Verdana",
            "Wingdings",
            "Wingdings 2",
            "Wingdings 3"
        ]
    }
]

t2 = [
    {
        "key": "language",
        "value": "zh-CN"
    },
    {
        "key": "resolution",
        "value": [
            1920,
            1080
        ]
    },
    {
        "key": "available_resolution",
        "value": [
            1920,
            1040
        ]
    },
    {
        "key": "timezone_offset",
        "value": -480
    },
    {
        "key": "navigator_platform",
        "value": "Win32"
    },
    {
        "key": "regular_plugins",
        "value": [
            "PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf",
            "Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf",
            "Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf",
            "Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf",
            "WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"
        ]
    },
    {
        "key": "adblock",
        "value": false
    },
    {
        "key": "touch_support",
        "value": [
            0,
            false,
            false
        ]
    },
    {
        "key": "js_fonts",
        "value": [
            "Arial",
            "Arial Black",
            "Arial Narrow",
            "Calibri",
            "Cambria",
            "Cambria Math",
            "Comic Sans MS",
            "Consolas",
            "Courier",
            "Courier New",
            "Georgia",
            "Helvetica",
            "Impact",
            "Lucida Console",
            "Lucida Sans Unicode",
            "Microsoft Sans Serif",
            "MS Gothic",
            "MS PGothic",
            "MS Sans Serif",
            "MS Serif",
            "Palatino Linotype",
            "Segoe Print",
            "Segoe Script",
            "Segoe UI",
            "Segoe UI Light",
            "Segoe UI Semibold",
            "Segoe UI Symbol",
            "Tahoma",
            "Times",
            "Times New Roman",
            "Trebuchet MS",
            "Verdana",
            "Wingdings",
            "Wingdings 2",
            "Wingdings 3"
        ]
    }
]

i3 = {
    "visitorId": "",
    "components": {
        "fonts": {
            "value": [
                "Calibri",
                "Franklin Gothic",
                "MS UI Gothic",
                "MT Extra",
                "Marlett",
                "Segoe UI Light",
                "SimHei"
            ],
            "duration": 35
        },
        "dom_blockers": {
            "duration": 20
        },
        "font_preferences": {
            "value": {
                "default": 161.296875,
                "apple": 161.296875,
                "serif": 136,
                "sans": 161.296875,
                "mono": 119,
                "min": 10.09375,
                "system": 161.296875
            },
            "duration": 23
        },
        "audio": {
            "value": 124.04347527516074,
            "duration": 4
        },
        "screen_frame": {
            "value": [
                0,
                0,
                40,
                0
            ],
            "duration": 0
        },
        "os_cpu": {
            "duration": 0
        },
        "languages": {
            "value": [
                [
                    "zh-CN"
                ]
            ],
            "duration": 0
        },
        "device_memory": {
            "value": 8,
            "duration": 0
        },
        "screen_resolution": {
            "value": [
                1920,
                1080
            ],
            "duration": 0
        },
        "hardware_concurrency": {
            "value": 8,
            "duration": 0
        },
        "timezone": {
            "value": "Asia/Shanghai",
            "duration": 1
        },
        "indexed_db": {
            "value": true,
            "duration": 0
        },
        "open_database": {
            "value": false,
            "duration": 0
        },
        "platform": {
            "value": "Win32",
            "duration": 0
        },
        "plugins": {
            "value": [
                {
                    "name": "PDF Viewer",
                    "description": "Portable Document Format",
                    "mimeTypes": [
                        {
                            "type": "application/pdf",
                            "suffixes": "pdf"
                        },
                        {
                            "type": "text/pdf",
                            "suffixes": "pdf"
                        }
                    ]
                },
                {
                    "name": "Chrome PDF Viewer",
                    "description": "Portable Document Format",
                    "mimeTypes": [
                        {
                            "type": "application/pdf",
                            "suffixes": "pdf"
                        },
                        {
                            "type": "text/pdf",
                            "suffixes": "pdf"
                        }
                    ]
                },
                {
                    "name": "Chromium PDF Viewer",
                    "description": "Portable Document Format",
                    "mimeTypes": [
                        {
                            "type": "application/pdf",
                            "suffixes": "pdf"
                        },
                        {
                            "type": "text/pdf",
                            "suffixes": "pdf"
                        }
                    ]
                },
                {
                    "name": "Microsoft Edge PDF Viewer",
                    "description": "Portable Document Format",
                    "mimeTypes": [
                        {
                            "type": "application/pdf",
                            "suffixes": "pdf"
                        },
                        {
                            "type": "text/pdf",
                            "suffixes": "pdf"
                        }
                    ]
                },
                {
                    "name": "WebKit built-in PDF",
                    "description": "Portable Document Format",
                    "mimeTypes": [
                        {
                            "type": "application/pdf",
                            "suffixes": "pdf"
                        },
                        {
                            "type": "text/pdf",
                            "suffixes": "pdf"
                        }
                    ]
                }
            ],
            "duration": 0
        },
        "canvas": {
            "value": {
                "winding": true,
                "geometry": "data:image/png;base64,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",
                "text": "data:image/png;base64,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"
            },
            "duration": 65
        },
        "touch_support": {
            "value": {
                "maxTouchPoints": 0,
                "touchEvent": false,
                "touchStart": false
            },
            "duration": 0
        },
        "vendor_flavors": {
            "value": [
                "chrome"
            ],
            "duration": 0
        },
        "color_gamut": {
            "value": "srgb",
            "duration": 0
        },
        "inverted_colors": {
            "duration": 0
        },
        "forced_colors": {
            "value": false,
            "duration": 0
        },
        "monochrome": {
            "value": 0,
            "duration": 0
        },
        "contrast": {
            "value": 0,
            "duration": 0
        },
        "reduced_motion": {
            "value": true,
            "duration": 0
        },
        "hdr": {
            "value": false,
            "duration": 1
        },
        "math": {
            "value": {
                "acos": 1.4473588658278522,
                "acosh": 709.889355822726,
                "acoshPf": 355.291251501643,
                "asin": 0.12343746096704435,
                "asinh": 0.881373587019543,
                "asinhPf": 0.8813735870195429,
                "atanh": 0.5493061443340548,
                "atanhPf": 0.5493061443340548,
                "atan": 0.4636476090008061,
                "sin": 0.8178819121159085,
                "sinh": 1.1752011936438014,
                "sinhPf": 2.534342107873324,
                "cos": -0.8390715290095377,
                "cosh": 1.5430806348152437,
                "coshPf": 1.5430806348152437,
                "tan": -1.4214488238747245,
                "tanh": 0.7615941559557649,
                "tanhPf": 0.7615941559557649,
                "exp": 2.718281828459045,
                "expm1": 1.718281828459045,
                "expm1Pf": 1.718281828459045,
                "log1p": 2.3978952727983707,
                "log1pPf": 2.3978952727983707,
                "powPI": 1.9275814160560206e-50
            },
            "duration": 0
        },
        "video_card": {
            "value": {
                "vendor": "Google Inc. (NVIDIA)",
                "renderer": "ANGLE (NVIDIA, NVIDIA GeForce GTX 750 Ti (0x00001380) Direct3D11 vs_5_0 ps_5_0, D3D11)"
            },
            "duration": 12
        },
        "pdf_viewer_enabled": {
            "value": true,
            "duration": 1
        }
    },
    "version": "3.4.2"
}
i3.visitorId = Zp(i3.components)

components = {
    "fonts": {
        "value": [
            "Calibri",
            "Franklin Gothic",
            "MS UI Gothic",
            "MT Extra",
            "Marlett",
            "Segoe UI Light",
            "SimHei"
        ],
        "duration": 4343
    },
    "dom_blockers": {
        "duration": 4333
    },
    "font_preferences": {
        "value": {
            "default": 161.296875,
            "apple": 161.296875,
            "serif": 136,
            "sans": 161.296875,
            "mono": 119,
            "min": 10.09375,
            "system": 161.296875
        },
        "duration": 4446
    },
    "audio": {
        "value": 124.04347527516074,
        "duration": 6
    },
    "screen_frame": {
        "value": [
            0,
            0,
            40,
            0
        ],
        "duration": 1
    },
    "os_cpu": {
        "duration": 0
    },
    "languages": {
        "value": [
            [
                "zh-CN"
            ]
        ],
        "duration": 1
    },
    "device_memory": {
        "value": 8,
        "duration": 0
    },
    "screen_resolution": {
        "value": [
            1920,
            1080
        ],
        "duration": 0
    },
    "hardware_concurrency": {
        "value": 8,
        "duration": 0
    },
    "timezone": {
        "value": "Asia/Shanghai",
        "duration": 0
    },
    "indexed_db": {
        "value": true,
        "duration": 1
    },
    "open_database": {
        "value": false,
        "duration": 0
    },
    "platform": {
        "value": "Win32",
        "duration": 0
    },
    "plugins": {
        "value": [
            {
                "name": "PDF Viewer",
                "description": "Portable Document Format",
                "mimeTypes": [
                    {
                        "type": "application/pdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text/pdf",
                        "suffixes": "pdf"
                    }
                ]
            },
            {
                "name": "Chrome PDF Viewer",
                "description": "Portable Document Format",
                "mimeTypes": [
                    {
                        "type": "application/pdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text/pdf",
                        "suffixes": "pdf"
                    }
                ]
            },
            {
                "name": "Chromium PDF Viewer",
                "description": "Portable Document Format",
                "mimeTypes": [
                    {
                        "type": "application/pdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text/pdf",
                        "suffixes": "pdf"
                    }
                ]
            },
            {
                "name": "Microsoft Edge PDF Viewer",
                "description": "Portable Document Format",
                "mimeTypes": [
                    {
                        "type": "application/pdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text/pdf",
                        "suffixes": "pdf"
                    }
                ]
            },
            {
                "name": "WebKit built-in PDF",
                "description": "Portable Document Format",
                "mimeTypes": [
                    {
                        "type": "application/pdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text/pdf",
                        "suffixes": "pdf"
                    }
                ]
            }
        ],
        "duration": 0
    },
    "canvas": {
        "value": {
            "winding": true,
            "geometry": "data:image/png;base64,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",
            "text": "data:image/png;base64,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"
        },
        "duration": 53
    },
    "touch_support": {
        "value": {
            "maxTouchPoints": 0,
            "touchEvent": false,
            "touchStart": false
        },
        "duration": 1
    },
    "vendor_flavors": {
        "value": [
            "chrome"
        ],
        "duration": 0
    },
    "color_gamut": {
        "value": "srgb",
        "duration": 0
    },
    "inverted_colors": {
        "duration": 0
    },
    "forced_colors": {
        "value": false,
        "duration": 1
    },
    "monochrome": {
        "value": 0,
        "duration": 0
    },
    "contrast": {
        "value": 0,
        "duration": 0
    },
    "reduced_motion": {
        "value": true,
        "duration": 0
    },
    "hdr": {
        "value": false,
        "duration": 0
    },
    "math": {
        "value": {
            "acos": 1.4473588658278522,
            "acosh": 709.889355822726,
            "acoshPf": 355.291251501643,
            "asin": 0.12343746096704435,
            "asinh": 0.881373587019543,
            "asinhPf": 0.8813735870195429,
            "atanh": 0.5493061443340548,
            "atanhPf": 0.5493061443340548,
            "atan": 0.4636476090008061,
            "sin": 0.8178819121159085,
            "sinh": 1.1752011936438014,
            "sinhPf": 2.534342107873324,
            "cos": -0.8390715290095377,
            "cosh": 1.5430806348152437,
            "coshPf": 1.5430806348152437,
            "tan": -1.4214488238747245,
            "tanh": 0.7615941559557649,
            "tanhPf": 0.7615941559557649,
            "exp": 2.718281828459045,
            "expm1": 1.718281828459045,
            "expm1Pf": 1.718281828459045,
            "log1p": 2.3978952727983707,
            "log1pPf": 2.3978952727983707,
            "powPI": 1.9275814160560206e-50
        },
        "duration": 1
    },
    "video_card": {
        "value": {
            "vendor": "Google Inc. (NVIDIA)",
            "renderer": "ANGLE (NVIDIA, NVIDIA GeForce GTX 750 Ti (0x00001380) Direct3D11 vs_5_0 ps_5_0, D3D11)"
        },
        "duration": 26
    },
    "pdf_viewer_enabled": {
        "value": true,
        "duration": 0
    }
}


o = {
    "fonts": {
        "value": [
            "Calibri",
            "Franklin Gothic",
            "MS UI Gothic",
            "MT Extra",
            "Marlett",
            "Segoe UI Light",
            "SimHei"
        ],
        "duration": 40
    },
    "dom_blockers": {
        "duration": 27
    },
    "font_preferences": {
        "value": {
            "default": 161.296875,
            "apple": 161.296875,
            "serif": 136,
            "sans": 161.296875,
            "mono": 119,
            "min": 10.09375,
            "system": 161.296875
        },
        "duration": 31
    },
    "audio": {
        "value": 124.04347527516074,
        "duration": 8
    },
    "screen_frame": {
        "value": [
            0,
            0,
            40,
            0
        ],
        "duration": 1
    },
    "os_cpu": {
        "duration": 0
    },
    "languages": {
        "value": [
            [
                "zh-CN"
            ]
        ],
        "duration": 0
    },
    "device_memory": {
        "value": 8,
        "duration": 0
    },
    "screen_resolution": {
        "value": [
            1920,
            1080
        ],
        "duration": 0
    },
    "hardware_concurrency": {
        "value": 8,
        "duration": 0
    },
    "timezone": {
        "value": "Asia/Shanghai",
        "duration": 0
    },
    "indexed_db": {
        "value": true,
        "duration": 1
    },
    "open_database": {
        "value": false,
        "duration": 0
    },
    "platform": {
        "value": "Win32",
        "duration": 0
    },
    "plugins": {
        "value": [
            {
                "name": "PDF Viewer",
                "description": "Portable Document Format",
                "mimeTypes": [
                    {
                        "type": "application/pdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text/pdf",
                        "suffixes": "pdf"
                    }
                ]
            },
            {
                "name": "Chrome PDF Viewer",
                "description": "Portable Document Format",
                "mimeTypes": [
                    {
                        "type": "application/pdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text/pdf",
                        "suffixes": "pdf"
                    }
                ]
            },
            {
                "name": "Chromium PDF Viewer",
                "description": "Portable Document Format",
                "mimeTypes": [
                    {
                        "type": "application/pdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text/pdf",
                        "suffixes": "pdf"
                    }
                ]
            },
            {
                "name": "Microsoft Edge PDF Viewer",
                "description": "Portable Document Format",
                "mimeTypes": [
                    {
                        "type": "application/pdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text/pdf",
                        "suffixes": "pdf"
                    }
                ]
            },
            {
                "name": "WebKit built-in PDF",
                "description": "Portable Document Format",
                "mimeTypes": [
                    {
                        "type": "application/pdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text/pdf",
                        "suffixes": "pdf"
                    }
                ]
            }
        ],
        "duration": 0
    },
    "canvas": {
        "value": {
            "winding": true,
            "geometry": "data:image/png;base64,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",
            "text": "data:image/png;base64,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"
        },
        "duration": 37
    },
    "touch_support": {
        "value": {
            "maxTouchPoints": 0,
            "touchEvent": false,
            "touchStart": false
        },
        "duration": 1
    },
    "vendor_flavors": {
        "value": [
            "chrome"
        ],
        "duration": 0
    },
    "color_gamut": {
        "value": "srgb",
        "duration": 0
    },
    "inverted_colors": {
        "duration": 0
    },
    "forced_colors": {
        "value": false,
        "duration": 0
    },
    "monochrome": {
        "value": 0,
        "duration": 1
    },
    "contrast": {
        "value": 0,
        "duration": 0
    },
    "reduced_motion": {
        "value": true,
        "duration": 0
    },
    "hdr": {
        "value": false,
        "duration": 0
    },
    "math": {
        "value": {
            "acos": 1.4473588658278522,
            "acosh": 709.889355822726,
            "acoshPf": 355.291251501643,
            "asin": 0.12343746096704435,
            "asinh": 0.881373587019543,
            "asinhPf": 0.8813735870195429,
            "atanh": 0.5493061443340548,
            "atanhPf": 0.5493061443340548,
            "atan": 0.4636476090008061,
            "sin": 0.8178819121159085,
            "sinh": 1.1752011936438014,
            "sinhPf": 2.534342107873324,
            "cos": -0.8390715290095377,
            "cosh": 1.5430806348152437,
            "coshPf": 1.5430806348152437,
            "tan": -1.4214488238747245,
            "tanh": 0.7615941559557649,
            "tanhPf": 0.7615941559557649,
            "exp": 2.718281828459045,
            "expm1": 1.718281828459045,
            "expm1Pf": 1.718281828459045,
            "log1p": 2.3978952727983707,
            "log1pPf": 2.3978952727983707,
            "powPI": 1.9275814160560206e-50
        },
        "duration": 1
    },
    "video_card": {
        "value": {
            "vendor": "Google Inc. (NVIDIA)",
            "renderer": "ANGLE (NVIDIA, NVIDIA GeForce GTX 750 Ti (0x00001380) Direct3D11 vs_5_0 ps_5_0, D3D11)"
        },
        "duration": 58
    },
    "pdf_viewer_enabled": {
        "value": true,
        "duration": 0
    }
}

av3 = function (e) {
    var t;
    return {
        get visitorId() {
            return void 0 === t && (t = Zp(this.components)),
                t
        },
        set visitorId(e) {
            t = e
        },
        components: e,
        version: "3.4.2"
    }
}(o)

console.log("av3: ", av3)


function rh(e) {
    var t = {};
    return e && e.forEach((e => {
            void 0 !== e.value && (t[e.key] = e.value)
        }
    )),
        JSON.stringify(t)
}

function getSign(t) {
    var n = [];
    t.forEach((function (e) {
            var t = e.value;
            void 0 !== e.value.join && (t = e.value.join(";")),
                n.push(t)
        }
    ));
    return a.x64hash128(n.join("~~~"), 31)
}


// 74f3e7962c5693581fc8aa09ef395d6d
r1 = getSign(t1)

// c3b0cd1f024a33fa6067b9773eb5d01e
r2 = getSign(t2)


console.log("r1: ", r1)
console.log("r2: ", r2)

f1 = {
    components: rh(t1),
    fingerprint: r1,
    version: "fingerprint-v1"
}

console.log("f1: ", f1)

f2 = {
    components: rh(t2),
    fingerprint: r2,
    version: "fingerprint-v1-sans-ua"
}

// 3bcc3bc21651f72cf741a61dcabcc514
visitorId = Zp(components)
console.log("visitorId: ", visitorId)

visitorId = Zp(i3.components)
console.log("visitorId: ", visitorId)

i = i3
f3 = {
    components: (t = i.components,
        r = {},
    t && Object.entries(t).forEach((e => {
            var [t, n] = e
                , i = n.value;
            void 0 !== i && (r[t] = i)
        }
    )),
        JSON.stringify(r)),
    fingerprint: i.visitorId,
    version: "fingerprint-v2"
}
console.log("f2: ", f2)

console.log("f3: ", f3)


