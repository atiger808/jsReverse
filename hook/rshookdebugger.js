
// JS Hook 与过 debugger

// JSON.parse()
(function () {
    var parse_ = JSON.parse;
    JSON.parse = function (arg) {
        console.log(arg)
        debugger;
        return parse_(arg)
    };
})();



// XMLHttpRequest(请求的参数)
(function () {
    var _open = window.XMLHttpRequest.prototype.open;
    window.XMLHttpRequest.prototype.open = function (method, url, async) {
        if (url.indexOf("参数名称") != -1){
            debugger;
        }
    }
    return _open.apply(this, arguments)
})();


// XMLHttpReques (header)
(function () {
    var _setRequestHeader = window.XMLHttpRequest.prototype.setRequestHeader;
    window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
        if (key == "header 的参数 key") {
            debugger;
        }
        // return open.apply(this, arguments)
        return _setRequestHeader.apply(this, arguments)
    }
})();


// Cookie
(function () {
    var cookieTemp = "";
    Object.defineProperty(document, "cookie", {
        set: function (val) {
            if (val.indexOf("cookie 关键字") != -1) {
                debugger;
            }
            console.log(val)
            cookieTemp = val;
            return val;
        },
        get: function () {
            return cookieTemp
        },
    });
})();


// eval
(function () {
    var _eval = eval;
    eval = function (val) {
        if (val.indexOf("debuuger") ==== -1) {
            _eval_cache(obj);
        }
    }
})();



// 方法置空（过debugger）
// 原理
function main() {
    debugger;
}

main = function () {

}



// 去除无限debugger-1
Function.prototype.__construct_back = Function.prototype.constructor;
Function.prototype.constructor = function () {
    if(arguments && typeof arguments[0] === "string"){
        // alert("new function: " + arguments[0])
        if("debugger" === arguments[0]){
            return
        }
    }
    return Function.prototype.__construct_back.apply(this, arguments)
}


// 去除无限debugger-2
var _constructor = constructor;
Function.prototype.constructor = function (s) {
    if (s == "debugger") {
        console.log(s)
        return null;
    }
    return _constructor(s)
}

// 去除无限debugger-3
let _Function = Function;
Function = function (s) {
    if (s == "debugger") {
        console.log(s)
        return null;
    }
    return _Function(s)
}