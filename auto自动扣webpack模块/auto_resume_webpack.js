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


isNumeric = function (str) {
    return typeof (str) === "number";
};
total_count = 0;
uniqueArr = [];
arr = [];
window.code = '';

function i(e) {
        if (n[e])
            return n[e].exports;
        var r = n[e] = {
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
            window.code += e + ':' + t[e] + ','
        } else {
            window.code += '"' + e + '"' + ':' + t[e] + ','
        }

        return t[e].call(r.exports, r, r.exports, i),
        r.l = !0,
        r.exports
    }




isNumeric = function (str) {
    return typeof (str) === "number";
};
total_count = 0;
uniqueArr = [];
arr = [];
window.code = '';


d = function (e) {
    var t = r[e];
    if (void 0 !== t)
        return t.exports;
    var a = r[e] = {
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
            window.code += e + ':' + l[e] + ','
        } else {
            window.code += '"' + e + '"' + ':' + l[e] + ','
        }


    return l[e].call(a.exports, a, a.exports, d),
        a.loaded = !0,
        a.exports
}




