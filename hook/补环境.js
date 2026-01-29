// @File   :补环境.js
// @Time   :2024/7/8 15:11
// @Author :dayue
// @Email  :ole211@qq.com


// proxy代理声明
function proxy_watch(obj) {

   return new Proxy(obj, {
       get(target, p, receiver) {
           debugger;
           let val = Reflect.get(...arguments);
           console.log("get", target, "=获取属性>", p, "=值>", val);
           return val;
      },
       set(target, p, value, receiver) {
           debugger;
           console.log("set", target, "=设置属性>", p, "=值>", value);
           return Reflect.set(...arguments);
      }
  });
};
// 一、补充window环境
window = {}

window = this

Window = function Window() {

}

Object.setPrototypeOf(window, Window.prototype)

Window.prototype.setTimeout = function setTimeout(){

}

//二、补充 document
document = {
   referrer: ''
}

Document = function Document() {

}
Object.setPrototypeOf(document, Document.prototype)


Document.prototype.addEventListener = function () {

}

//三、补充 location
location = {
   href: 'https://mobile.pinduoduo.com/',
   protocol: 'https:',
}

Location = function Location() {

}

Object.setPrototypeOf(location, Location.prototype)

// 四、补充 navigator
navigator = {
   userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

Navigator = function Navigator() {

}
Object.setPrototypeOf(navigator, Navigator.prototype)

Navigator.prototype.hasOwnProperty = function () {
   return true
}

// 五、补充 screen
screen = {
   // width: 1728,
}

Screen = function Screen() {

}
Object.setPrototypeOf(screen, Screen.prototype)


// 六、补充 history对象
history = {}
History = function History() {

}
Object.setPrototypeOf(history, History.prototype)
History.prototype.back = function () {

}


// 代理对象设置
window = proxy_watch(window)
document = proxy_watch(document)
location = proxy_watch(location)
navigator = proxy_watch(navigator)