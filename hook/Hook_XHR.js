
(function () {
    let openCache = window.XMLHttpRequest.prototype.open;
    window.XMLHttpRequest.prototype.open = function (method, url) {
        console.log("Hook xhr method => %s, url => %s", method, url);
        if (url.indexOf("value") !== -1) {
            debugger;
        }
        return openCache.apply(this, arguments);
    };
})();
