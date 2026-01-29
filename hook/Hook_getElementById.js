(function () {
    getElementByIdCache = document.getElementById;
    document.getElementById = function (id) {
        console.info("Hook getElementById id => ", id);
        if (id === "spiderapi") {
            debugger;
        }
        return getElementByIdCache(id);
    };
})();


(function () {
    originalGetElementsByTagName = document.getElementsByTagName;
    document.getElementsByTagName = function (tagName) {
        if (tagName === "meta") {
            // 在这里插入您的调试代码
            console.log(".getElementsByTagName 调用了meta");
            debugger;
        }
        return originalGetElementsByTagName.apply(this, arguments);
    };
})();