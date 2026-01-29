
// hook勾子
(function () {
    let stringfyCache = JSON.stringify;
    JSON.stringify = function (params) {
        console.log("Hook JSON.stringfy => ", params);

        return stringfyCache(params)
    }
})();