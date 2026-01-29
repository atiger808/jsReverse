// @File   :dyslider.js
// @Time   :2024/12/18 17:36
// @Author :dayue
// @Email  :ole211@qq.com


function get_fp() {
    var e = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split("")
        , t = e.length
        , n = (new Date).getTime().toString(36)
        , o = [];
    o[8] = o[13] = o[18] = o[23] = "_",
        o[14] = "4";
    for (var i = 0, r = void 0; i < 36; i++) {
        o[i] || (r = 0 | Math.random() * t,
            o[i] = e[19 == i ? 3 & r | 8 : r])
    }
    return "verify_" + n + "_" + o.join("")
}


console.log(get_fp())