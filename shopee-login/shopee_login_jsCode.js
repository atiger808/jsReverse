// @File   :shopee_login_jsCode.js
// @Time   :2026/1/30 11:43
// @Author :dayue
// @Email  :ole211@qq.com

const CryptoJS = require('crypto-js');

ShopAccount = "shop";

function generatePasswordHash(password, loginType) {
  const md5Hashed = CryptoJS.MD5(password).toString();

  if (loginType !== ShopAccount) {
    return md5Hashed;
  } else {
    return CryptoJS.SHA256(md5Hashed).toString();
  }
}


password = "qweasd11"
loginType = "shop"

console.log("result: ", generatePasswordHash(password, loginType))