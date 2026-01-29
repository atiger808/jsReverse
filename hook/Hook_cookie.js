// @File   :Hook_cookie.js
// @Time   :2024/7/5 13:57
// @Author :dayue
// @Email  :ole211@qq.com

// hook  指定cookie赋值
(function () {
    'use strict';
    Object.defineProperty(document, 'cookie', {
        set: function (cookie) {
            if(cookie.indexOf("_pcc")!= -1){
                debugger;
            }
            return cookie;
        }
    });
})();

// 作者：无情哈拉少
// 链接：https://zhuanlan.zhihu.com/p/599587412
// 来源：知乎
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。