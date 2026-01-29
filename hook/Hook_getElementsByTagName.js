// @File   :Hook_getElementsByTagName.js
// @Time   :2024/7/5 16:29
// @Author :dayue
// @Email  :ole211@qq.com

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
