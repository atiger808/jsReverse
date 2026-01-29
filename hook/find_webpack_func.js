const jsdom = require("jsdom");
const {JSDOM} = jsdom;

dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);

// 在这里，你可以运行你的JavaScript代码
window = dom.window;
document = dom.window.document

window = global

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


// webapck 列表函数找函数索引

laohe.m.forEach(function (element, index) {
    if (element.toString().indexOf("o.ec.encrypt") != -1) {
        console.log(index)
    }
})

window.code = '';
r = function (e) {
    if (r[e])
        return r[e].exports;
    var d = r[e] = {
        i: e,
        l: !1,
        exports: {}
    };
    console.log(e)

    window.code += e + ':' + o[e] + ',\r\n'
    return o[e].call(d.exports, d, d.exports, r),
        d.l = !0,
        d.exports
}


/*
 https://www.mytokencap.com/indextrending/1/
 */
total_count = 0
uniqueArr = []
arr = [];
window.code = '';
c = function c(a) {
    var n = t[a];
    if (void 0 !== n)
        return n.exports;
    var r = t[a] = {
        id: a,
        loaded: !1,
        exports: {}
    }
        , f = !0;
    try {
        e[a].call(r.exports, r, r.exports, c),
            f = !1
    } finally {
        f && delete t[a]
    }


    console.log(a)
    arr.push(a)
    total_count += 1
    uniqueArr = arr.reduce((prev, curr) => prev.includes(curr) ? prev : [...prev, curr], []);
    console.log("total_count: " + total_count + " uniqueArr: " + uniqueArr.length)

    window.code += a + ':' + e[a] + ',\r\n'

    return r.loaded = !0,
        r.exports
}


/*
https://www.hanghangcha.com/industry
 */
isNumeric = function (str) {
    return typeof (str) === "number";
};

total_count = 0;
uniqueArr = [];
arr = [];
window.code = '';
a = function a(e) {
    if (o[e])
        return o[e].exports;
    var t = o[e] = {
        i: e,
        l: !1,
        exports: {}
    };
    console.log(e)
    arr.push(e)
    total_count += 1
    uniqueArr = arr.reduce((prev, curr) => prev.includes(curr) ? prev : [...prev, curr], []);
    console.log("total_count: " + total_count + " uniqueArr: " + uniqueArr.length);
    if (isNumeric(e)) {
        window.code += e + ':' + n[e] + ',\r\n'
    } else {
        window.code += '"' + e + '"' + ':' + n[e] + ',\r\n'
    }


    return n[e].call(t.exports, t, t.exports, a),
        t.l = !0,
        t.exports
}

/*
https://help.steampowered.com/zh-tw/wizard/Login
 */
isNumeric = function (str) {
    return typeof (str) === "number";
};

total_count = 0;
uniqueArr = [];
arr = [];
window.code = '';
l = function l(a) {
    var e = r[a];
    if (void 0 !== e)
        return e.exports;
    var n = r[a] = {
        id: a,
        loaded: !1,
        exports: {}
    };

    console.log(a)
    arr.push(a)
    total_count += 1
    uniqueArr = arr.reduce((prev, curr) => prev.includes(curr) ? prev : [...prev, curr], []);
    console.log("total_count: " + total_count + " uniqueArr: " + uniqueArr.length);
    if (isNumeric(a)) {
        window.code += a + ':' + t[a] + ',\r\n'
    } else {
        window.code += '"' + a + '"' + ':' + t[a] + ',\r\n'
    }

    return t[a].call(n.exports, n, n.exports, l),
        n.loaded = !0,
        n.exports
}

/*
https://www.xiaohongshu.com/explore
 */
isNumeric = function (str) {
    return typeof (str) === "number";
};

total_count = 0;
uniqueArr = [];
arr = [];
window.code = '';
a = function a(e) {
    var t = u[e];
    if (void 0 !== t)
        return t.exports;
    var n = u[e] = {
        id: e,
        loaded: !1,
        exports: {}
    };

    console.log(e)
    arr.push(e)
    total_count += 1
    uniqueArr = arr.reduce((prev, curr) => prev.includes(curr) ? prev : [...prev, curr], []);
    console.log("total_count: " + total_count + " uniqueArr: " + uniqueArr.length);
    if (isNumeric(e)) {
        window.code += e + ':' + i[e] + ',\r\n'
    } else {
        window.code += '"' + e + '"' + ':' + i[e] + ',\r\n'
    }

    return i[e].call(n.exports, n, n.exports, a),
        n.loaded = !0,
        n.exports
}


/*
https://fse.agilestudio.cn/search?keyword=%E9%AB%98%E5%B1%B1%E6%B5%81%E6%B0%B4
 */
isNumeric = function (str) {
    return typeof (str) === "number";
};

total_count = 0;
uniqueArr = [];
arr = [];
window.code = '';
o = function o(n) {
    if (t[n])
        return t[n].exports;
    var c = t[n] = {
        i: n,
        l: !1,
        exports: {}
    };


    console.log(n)
    arr.push(n)
    total_count += 1
    uniqueArr = arr.reduce((prev, curr) => prev.includes(curr) ? prev : [...prev, curr], []);
    console.log("total_count: " + total_count + " uniqueArr: " + uniqueArr.length);
    if (isNumeric(n)) {
        window.code += n + ':' + e[n] + ',\r\n'
    } else {
        window.code += '"' + n + '"' + ':' + e[n] + ',\r\n'
    }

    return e[n].call(c.exports, c, c.exports, o),
        c.l = !0,
        c.exports
}


c = function (a) {

    if (c[a])
        return c[a].exports;

    var f = c[a] = {
        id: a,
        loaded: !1,
        exports: {}
    }
        , r = !0;

    try {
        e[a].call(f.exports, f, f.exports, c),
            r = !1
    } finally {
        r && delete t[a]
    }

    console.log(a)
    arr.push(a)
    total_count += 1
    uniqueArr = arr.reduce((prev, curr) => prev.includes(curr) ? prev : [...prev, curr], []);
    console.log("total_count: " + total_count + " uniqueArr: " + uniqueArr.length)

    window.code += a + ':' + e[a] + ',\r\n'


    return f.loaded = !0,
        f.exports
}


/*
* https://jzsc.mohurd.gov.cn/data/company
* */

isNumeric = function (str) {
    return typeof (str) === "number";
};
total_count = 0;
uniqueArr = [];
arr = [];
window.code = '';

function s(e) {
    if (a[e])
        return a[e].exports;
    var n = a[e] = {
        i: e,
        l: !1,
        exports: {}
    };


    console.log(e)
    arr.push(e)
    total_count += 1
    uniqueArr = arr.reduce((prev, curr) => prev.includes(curr) ? prev : [...prev, curr], []);
    console.log("total_count: " + total_count + " uniqueArr: " + uniqueArr.length)

    if (isNumeric(e)) {
        window.code += e + ':' + t[e] + ',\r\n'
    } else {
        window.code += '"' + e + '"' + ':' + t[e] + ',\r\n'
    }

    return t[e].call(n.exports, n, n.exports, s),
        n.l = !0,
        n.exports
}


/*
* https://cdnmobibank.bankofbeijing.com.cn/cdn/mbank/FP/FP6/TFP6001.html?prdCode=230120088
* */

isNumeric = function (str) {
    return typeof (str) === "number";
};
total_count = 0;
uniqueArr = [];
arr = [];
window.code = '';
i = {};

r = function (e) {
    if (i[e])
        return i[e].exports;
    var t = i[e] = {
        i: e,
        l: !1,
        exports: {}
    };


    console.log(e)
    arr.push(e)
    total_count += 1
    uniqueArr = arr.reduce((prev, curr) => prev.includes(curr) ? prev : [...prev, curr], []);
    console.log("total_count: " + total_count + " uniqueArr: " + uniqueArr.length)

    if (isNumeric(e)) {
        window.code += e + ':' + n[e] + ',\r\n'
    } else {
        window.code += '"' + e + '"' + ':' + n[e] + ',\r\n'
    }


    return n[e].call(t.exports, t, t.exports, r),
        t.l = !0,
        t.exports
}



/*
* https://www.zhihu.com/
* */

isNumeric = function (str) {
    return typeof (str) === "number";
};
total_count = 0;
uniqueArr = [];
arr = [];
window.code = '';
function p(e) {
    var a = m[e];
    if (void 0 !== a)
        return a.exports;
    var c = m[e] = {
        id: e,
        loaded: !1,
        exports: {}
    };


    console.log(e)
    arr.push(e)
    total_count += 1
    uniqueArr = arr.reduce((prev, curr) => prev.includes(curr) ? prev : [...prev, curr], []);
    console.log("total_count: " + total_count + " uniqueArr: " + uniqueArr.length)

    if (isNumeric(e)) {
        window.code += e + ':' + u[e] + ',\r\n'
    } else {
        window.code += '"' + e + '"' + ':' + u[e] + ',\r\n'
    }

    return u[e].call(c.exports, c, c.exports, p),
        c.loaded = !0,
        c.exports
}

