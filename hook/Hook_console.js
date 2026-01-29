
/*

Hook 是一种钩子技术，在系统没有调用函数之前，钩子程序就先得到控制权，这时钩子函数既可以加工处理（改变）该函数的执行行为，也可以强制结束消息的传递。简单来说，修改原有的 JS 代码就是 Hook。

Hook 技术之所以能够实现有两个条件：

客户端拥有JS的最高解释权，可以决定在任何时候注入JS，而服务器无法阻止或干预。服务端只能通过检测和混淆的手段，另 Hook 难度加大，但是无法直接阻止。

除了上面的必要条件之外，还有一个条件。就是 JS 是一种弱类型语言，同一个变量可以多次定义、根据需要进行不同的赋值，而这种情况如果在其他强类型语言中则可能会报错，导致代码无法执行。js 的这种特性，为我们 Hook 代码提供了便利。



1 Hook步骤：
1 寻找hook的点

2 编写hook逻辑

3 调试

注：最常用的是hook cookie response open 表单


 */


(function () {
    let consoleCache = console.log;
    console.log = function (msg) {
        consoleCache("Hook console.log =>", msg);
        if(msg === "value") {
            debugger;
        }
        consoleCache(msg);
    };
})();
