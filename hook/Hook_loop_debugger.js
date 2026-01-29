
(function () {
    let constructorCache = Function.prototype.constructor;
    Function.prototype.constructor = function (string) {
        if (string === "debugger") {
            console.log("Hook constructor debugger!");
            return function () {};
        }
        return constructorCache(string);
    };
})();

(function () {
    let setIntervalCache = setInterval;
    setInterval = function (func, delay) {
        if (func.toString().indexOf("debugger") !== -1) {
            console.log("Hook setInterval debugger!");
            return function () {};
        }
        return setIntervalCache(func, delay);
    };
})();


(function () {
    let setTimeoutCache = setTimeout;
    setTimeout = function (func, delay) {
        if (func.toString().indexOf("debugger") !== -1) {
            console.log("Hook setTimeout debugger!");
            return function () {};
        }
        return setTimeoutCache(func, delay);
    };
})();


(function () {
    let evalCache = window.eval;
    window.eval = function (string) {
        if (string.includes("debugger")) {
            console.log("Hook eval debugger!");
        }
        return evalCache(string.replace(/debugger\s*;?/g, ""));
    };
    window.eval.toString = function () {
        return evalCache.toString();
    };
})();


let _constructor = constructor;
Function.prototype.constructor = function(s){
  if (s == "debugger"){
    return null;
  }
  return _constructor(s);
}
setInterval = function(){}
for (let i = 1; i < 99999; i++)window.clearInterval(i);

// 作者：啊柒啊啊啊
// 链接：https://zhuanlan.zhihu.com/p/693796525
// 来源：知乎
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。