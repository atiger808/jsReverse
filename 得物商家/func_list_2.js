// @File   :func_list_2.js
// @Time   :2026/1/29 14:24
// @Author :dayue
// @Email  :ole211@qq.com


const func_list_2 = {
    21627:function(n,s,e){Promise.all([e.e(827),e.e(675)]).then(e.bind(e,3225))},
    1048: function(g) {
            (function() {
                var A = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
                  , e = {
                    rotl: function(u, i) {
                        return u << i | u >>> 32 - i
                    },
                    rotr: function(u, i) {
                        return u << 32 - i | u >>> i
                    },
                    endian: function(u) {
                        if (u.constructor == Number)
                            return e.rotl(u, 8) & 16711935 | e.rotl(u, 24) & 4278255360;
                        for (var i = 0; i < u.length; i++)
                            u[i] = e.endian(u[i]);
                        return u
                    },
                    randomBytes: function(u) {
                        for (var i = []; u > 0; u--)
                            i.push(Math.floor(Math.random() * 256));
                        return i
                    },
                    bytesToWords: function(u) {
                        for (var i = [], a = 0, l = 0; a < u.length; a++,
                        l += 8)
                            i[l >>> 5] |= u[a] << 24 - l % 32;
                        return i
                    },
                    wordsToBytes: function(u) {
                        for (var i = [], a = 0; a < u.length * 32; a += 8)
                            i.push(u[a >>> 5] >>> 24 - a % 32 & 255);
                        return i
                    },
                    bytesToHex: function(u) {
                        for (var i = [], a = 0; a < u.length; a++)
                            i.push((u[a] >>> 4).toString(16)),
                            i.push((u[a] & 15).toString(16));
                        return i.join("")
                    },
                    hexToBytes: function(u) {
                        for (var i = [], a = 0; a < u.length; a += 2)
                            i.push(parseInt(u.substr(a, 2), 16));
                        return i
                    },
                    bytesToBase64: function(u) {
                        for (var i = [], a = 0; a < u.length; a += 3)
                            for (var l = u[a] << 16 | u[a + 1] << 8 | u[a + 2], c = 0; c < 4; c++)
                                a * 8 + c * 6 <= u.length * 8 ? i.push(A.charAt(l >>> 6 * (3 - c) & 63)) : i.push("=");
                        return i.join("")
                    },
                    base64ToBytes: function(u) {
                        u = u.replace(/[^A-Z0-9+\/]/ig, "");
                        for (var i = [], a = 0, l = 0; a < u.length; l = ++a % 4)
                            l != 0 && i.push((A.indexOf(u.charAt(a - 1)) & Math.pow(2, -2 * l + 8) - 1) << l * 2 | A.indexOf(u.charAt(a)) >>> 6 - l * 2);
                        return i
                    }
                };
                g.exports = e
            }
            )()
        },

    6636: function(g) {
            var A = {
                utf8: {
                    stringToBytes: function(e) {
                        return A.bin.stringToBytes(unescape(encodeURIComponent(e)))
                    },
                    bytesToString: function(e) {
                        return decodeURIComponent(escape(A.bin.bytesToString(e)))
                    }
                },
                bin: {
                    stringToBytes: function(e) {
                        for (var u = [], i = 0; i < e.length; i++)
                            u.push(e.charCodeAt(i) & 255);
                        return u
                    },
                    bytesToString: function(e) {
                        for (var u = [], i = 0; i < e.length; i++)
                            u.push(String.fromCharCode(e[i]));
                        return u.join("")
                    }
                }
            };
            g.exports = A
        },

    84331: function(g) {
            g.exports = function(u) {
                return u != null && (A(u) || e(u) || !!u._isBuffer)
            }
            ;
            function A(u) {
                return !!u.constructor && typeof u.constructor.isBuffer == "function" && u.constructor.isBuffer(u)
            }
            function e(u) {
                return typeof u.readFloatLE == "function" && typeof u.slice == "function" && A(u.slice(0, 0))
            }
        },

}

module.exports = func_list_2;