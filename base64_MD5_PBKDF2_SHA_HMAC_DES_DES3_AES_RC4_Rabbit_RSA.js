// 常：https://github.com/travist/jsen见加密算法：
// //
// //
// //
// // 对称加密（加密解密密钥相同）：DES、3DES、AES、RC4、Rabbit
// // 非对称加密（区分公钥和私钥）：RSA、DSA、ECC
// // 消息摘要算法/签名算法：MD5、SHA、HMAC、PBKDF2
// // 常见编码算法：Base64
// //
// // JavaScript 加密解密模块
// // Crypto-JS
// // Crypto-JS 支持 MD5、SHA、RIPEMD-160、HMAC、PBKDF2、AES、DES、3DES（Triple DES）、Rabbit、RC4 等，不支持 RSA、ECC，是应用比较广的加密模块，使用命令 npm install crypto-js 安装。
// //
// // 参考资料：
// //
// // Crypto-JS 文档：https://cryptojs.gitbook.io/docs/
// // Crypto-JS Github：https://github.com/brix/crypto-js
// // Node-RSA
// // Node-RSA 对 RSA 算法提供了支持，使用命令 npm install node-rsa 安装。
// //
// // 参考资料：Node-RSA Github：https://github.com/rzcoder/node-rsa
// //
// // JSEncrypt
// // 参考资料：JSEncrypt 对 RSA 算法提供了更加全面的支持，使用命令 npm install jsencrypt 安装。
// //
// // JSEncrypt 文档：http://travistidwell.com/jsencrypt/
// // JSEncrypt Github

// npm 使用
// 初始化环境
//
// 新建一个文件夹 node-rsa-demo , 终端进入，运行下面命令初始化
//
// cd node-rsa-demo
// npm init # 一路回车即可
// npm install --save node-rsa
// 生成公钥私钥
//
// 在 node-rsa-demo 下新建一个文件 index.js 写上如下代码

// var CryptoJS = require('./test/crypto-js.min')
var CryptoJS = require('crypto-js')


// Base64
// 简介：Base64 是一种用 64 个字符来表示任意二进制数据的方法。
//
// 参考资料：
//
// Base64 百度百科：https://baike.baidu.com/item/base64/8545775
// Base64 维基百科：https://en.wikipedia.org/wiki/B

function base64Encode(text) {
    var srcs = CryptoJS.enc.Utf8.parse(text)
    var encodeData = CryptoJS.enc.Base64.stringify(srcs)
    return encodeData
}

function base64Decode(encodeData) {
    var srcs = CryptoJS.enc.Base64.parse(encodeData)
    var decodeData = srcs.toString(CryptoJS.enc.Utf8)
    return decodeData
}

// MD5
// 简介：全称 MD5 消息摘要算法（英文名称：MD5 Message-Digest Algorithm），又称哈希算法、散列算法，由美国密码学家罗纳德·李维斯特（Ronald Linn Rivest）设计，于 1992 年作为 RFC 1321 被公布，用以取代 MD4 算法。摘要算法是单向加密的，也就是说明文通过摘要算法加密之后，是不能解密的。摘要算法的第二个特点密文是固定长度的，它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。之所以叫摘要算法，它的算法就是提取明文重要的特征。所以，两个不同的明文，使用了摘要算法之后，有可能他们的密文是一样的，不过这个概率非常的低。
//
// 参考资料：
//
// RFC 1321：https://datatracker.ietf.org/doc/rfc1321/
// MD5 维基百科：https://en.wikipedia.org/wiki/M

function md5Encode(text) {
    return CryptoJS.MD5(text).toString()
}


// PBKDF2
// 简介：英文名称：Password-Based Key Derivation Function 2，PBKDF2 是 RSA 实验室的公钥加密标准（PKCS）系列的一部分，2017 年发布的 RFC 8018 （PKCS #5 v2.1）推荐使用 PBKDF2 进行密码散列。PBKDF2 将伪随机函数（例如 HMAC），把明文和一个盐值（salt）作为输入参数，然后进行重复运算，并最终产生密钥，如果重复的次数足够大，破解的成本就会变得很高。
//
// 参考资料：
//
// RFC 8018：https://datatracker.ietf.org/doc/rfc8018/
// PBKDF2 维基百科：https://en.wikipedia.org/wiki/P

function pbkdf2Encrypt(text, salt = '43215678') {
    // key 长度128， 10次重复运算
    var encryptedData = CryptoJS.PBKDF2(text, salt, {keySize: 128 / 32, iterations: 10})
    return encryptedData.toString()
}

// SHA
// 简介：全称安全哈希算法（英文名称：Secure Hash Algorithm），由美国国家安全局（NSA）所设计，主要适用于数字签名标准（Digital Signature Standard DSS）里面定义的数字签名算法（Digital Signature Algorithm DSA），SHA 通常指 SHA 家族的五个算法，分别是 SHA-1、SHA-224、SHA-256、SHA-384、SHA-512，后四者有时并称为 SHA-2，SHA 是比 MD5 更安全一点的摘要算法，MD5 的密文是 32 位，而 SHA-1 是 40 位，版本越强，密文越长，代价是速度越慢。
//
// 参考资料：
//
// RFC 3174：https://datatracker.ietf.org/doc/rfc3174/
// SHA 维基百科：https://en.wikipedia.org/wiki/S

function SHA1Encrypt(text) {
    return CryptoJS.SHA1(text).toString()
}

// HMAC
// 简介：全称散列消息认证码、密钥相关的哈希运算消息认证码（英文名称：Hash-based Message Authentication Code 或者 Keyed-hash Message Authentication Code），于 1996 年提出，1997 年作为 RFC 2104 被公布，HMAC 加密算法是一种安全的基于加密 Hash 函数和共享密钥的消息认证协议，它要求通信双方共享密钥 key、约定算法、对报文进行 Hash 运算，形成固定长度的认证码。通信双方通过认证码的校验来确定报文的合法性。
//
// 参考资料：
//
// RFC 2104：https://datatracker.ietf.org/doc/rfc2104/
// HMAC 维基百科：https://en.wikipedia.org/wiki/H

function HMACEncrypt(text, key = 'secret') {
    return CryptoJS.HmacMD5(text, key).toString()

}


// DES
// 简介：全称数据加密标准（英文名称：Data Encryption Standard），加密与解密使用同一密钥，属于对称加密算法，1977 年被美国联邦政府的国家标准局确定为联邦资料处理标准（FIPS），DES 是一个分组加密算法，使用 56 位的密钥（一般认为密钥是 64 位，但是密钥的每个第 8 位设置为奇偶校验位，所以实际上有效位只有 56 位），由于 56 位密钥长度相对较短，所以 DES 是不安全的，现在基本上已被更高级的加密标准 AES 取代。
//
// mode 支持：CBC，CFB，CTR，CTRGladman，ECB，OFB 等。
// padding 支持：ZeroPadding，NoPadding，AnsiX923，Iso10126，Iso97971，Pkcs7 等。
// 参考资料：
//
// RFC 4772：https://datatracker.ietf.org/doc/rfc4772/
// DES 维基百科：https://en.wikipedia.org/wiki/D

function desEncrypt(text, desKey = "6f726c64f2c2057", desIv = "0123456789ABCDEF") {
    // text  待加密对象
    // desKey 密钥
    // desIv 初始向量

    var key = CryptoJS.enc.Utf8.parse(desKey),
        iv = CryptoJS.enc.Utf8.parse(desIv),
        srcs = CryptoJS.enc.Utf8.parse(text),
        // CBC 加密模式， Pkcs7 填充方式
        encrypted = CryptoJS.DES.encrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    return encrypted.toString()
}


function desDecrypt(encryptedData, desKey = "6f726c64f2c2057", desIv = "0123456789ABCDEF") {
    var key = CryptoJS.enc.Utf8.parse(desKey),
        iv = CryptoJS.enc.Utf8.parse(desIv),
        srcs = encryptedData,
        // CBC 加密模式， Pkcs7 填充方式
        decrypted = CryptoJS.DES.decrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    console.log("key：" + key)
    console.log("iv：" + iv)
    return decrypted.toString(CryptoJS.enc.Utf8)
}

// 3DES
// 简介：全称三重数据加密算法（英文名称：Triple Data Encryption Standard、 Triple Data Encryption Algorithm、TDES、TDEA），是对称加密算法中的一种。70 年代初由 IBM 研发，后 1977 年被美国国家标准局采纳为数据加密标准，它相当于是对每个数据块应用三次 DES 加密算法。由于计算机运算能力的增强，原版 DES 密码的密钥长度变得容易被暴力破解；3DES 即是设计用来提供一种相对简单的方法，即通过增加 DES 的密钥长度来避免破解，所以严格来说 3DES 不是设计一种全新的块密码算法。
//
// mode 支持：CBC，CFB，CTR，CTRGladman，ECB，OFB 等。
// padding 支持：ZeroPadding，NoPadding，AnsiX923，Iso10126，Iso97971，Pkcs7 等。
// 参考资料：
//
// RFC 1851：https://datatracker.ietf.org/doc/rfc1851/
// 3DES 维基百科：https://en.wikipedia.org/wiki/T


function tripleDesEncrypt(text, desKey = "", desIv = "") {
    var key = CryptoJS.enc.Utf8.parse(desKey),
        iv = CryptoJS.enc.Utf8.parse(desIv),
        srcs = CryptoJS.enc.Utf8.parse(text),
        // ECB 加密模式，Iso10126 填充方式
        encrypted = CryptoJS.TripleDES.encrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Iso10126
        });
    return encrypted.toString()
}

function tripleDesDescrypt(encryptedData, desKey="", desIv="") {
    var key = CryptoJS.enc.Utf8.parse(desKey),
        iv = CryptoJS.enc.Utf8.parse(desIv),
        srcs = encryptedData,
        // ECB 加密方式， Iso10126 填充方式
        descrypted = CryptoJS.TripleDES.decrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Iso10126
        });
    return descrypted.toString(CryptoJS.enc.Utf8)
}



// AES
// 简介：全称高级加密标准（英文名称：Advanced Encryption Standard），在密码学中又称 Rijndael 加密法，由美国国家标准与技术研究院 （NIST）于 2001 年发布，并在 2002 年成为有效的标准，是美国联邦政府采用的一种区块加密标准。这个标准用来替代原先的 DES，已经被多方分析且广为全世界所使用，它本身只有一个密钥，即用来实现加密，也用于解密。
//
// mode 支持：CBC，CFB，CTR，CTRGladman，ECB，OFB 等。
// padding 支持：ZeroPadding，NoPadding，AnsiX923，Iso10126，Iso97971，Pkcs7 等。
// 参考资料：
//
// RFC 3268：https://datatracker.ietf.org/doc/rfc3268/
// AES 维基百科：https://en.wikipedia.org/wiki/A


function AESEncrypt(text, aesKey="", aesIv="") {
    // aesKey 密钥， 16倍数
    // aesIv 偏移量， 16倍数
    var key = CryptoJS.enc.Utf8.parse(aesKey),
        iv = CryptoJS.enc.Utf8.parse(aesIv),
        srcs = CryptoJS.enc.Utf8.parse(text),
        // CBC 加密方式， Pkcs7 填充方式
        encrypted = CryptoJS.AES.encrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    return encrypted.toString();
}

function AESDecrypt(encryptedData, aesKey="", aesIv="") {
    var key = CryptoJS.enc.Utf8.parse(aesKey),
        iv = CryptoJS.enc.Utf8.parse(aesIv),
        srcs = encryptedData,
        // CBC 加密方式， Pkcs7 填充方式
        decrypted = CryptoJS.AES.decrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    return decrypted.toString(CryptoJS.enc.Utf8);
}


// RC4
// 简介：英文名称：Rivest Cipher 4，也称为 ARC4 或 ARCFOUR，是一种流加密算法，密钥长度可变。它加解密使用相同的密钥，因此也属于对称加密算法。RC4 是有线等效加密（WEP）中采用的加密算法，也曾经是 TLS 可采用的算法之一，该算法的速度可以达到 DES 加密的 10 倍左右，且具有很高级别的非线性，虽然它在软件方面的简单性和速度非常出色，但在 RC4 中发现了多个漏洞，它特别容易受到攻击，RC4 作为一种老旧的验证和加密算法易于受到黑客攻击，现在逐渐不推荐使用了。
//
// 参考资料：
//
// RFC 7465：https://datatracker.ietf.org/doc/rfc7465/
// RC4 维基百科：https://en.wikipedia.org/wiki/R


function RC4Encrypt(text, key="") {
    return CryptoJS.RC4.encrypt(text, key).toString();
}

function RC4Decrypt(encryptedData, key="") {
    return CryptoJS.RC4.decrypt(encryptedData, key).toString(CryptoJS.enc.Utf8);
}


// Rabbit
// 简介：Rabbit 加密算法是一个高性能的流密码加密方式，2003 年首次被提出，它从 128 位密钥和 64 位初始向量（iv）创建一个密钥流。
//
// 参考资料：
//
// RFC 4503：https://datatracker.ietf.org/doc/rfc4503/
// Rabbit 维基百科：https://en.wikipedia.org/wiki/R

function rabbitEncrypt(text, key="") {
    return CryptoJS.Rabbit.encrypt(text, key).toString();
}

function rabbitDecrypt(encryptedData, key="") {
    return CryptoJS.Rabbit.decrypt(encryptedData, key).toString(CryptoJS.enc.Utf8);
}


// RSA
// 简介：英文名称：Rivest-Shamir-Adleman，是 1977 年由罗纳德·李维斯特（Ron Rivest）、阿迪·萨莫尔（Adi Shamir）和伦纳德·阿德曼（Leonard Adleman）一起提出的，RSA 就是他们三人姓氏开头字母拼在一起组成的，RSA 加密算法是一种非对称加密算法。在公开密钥加密和电子商业中RSA被广泛使用。它被普遍认为是目前比较优秀的公钥方案之一。RSA是第一个能同时用于加密和数字签名的算法，它能够抵抗到目前为止已知的所有密码攻击。
//
// 参考资料：
//
// RSA 维基百科：https://en.wikipedia.org/wiki/R

// npm install --save node-rsa
var NodeRSA = require('node-rsa');


function rsaEncrypt(text, publicKey) {
    pubKey = new NodeRSA(publicKey, 'pkcs8-public');
    var encryptedData = pubKey.encrypt(text, 'base64');
    return encryptedData
}

function rsaDecrypt(encryptedData, privateKey) {
    priKey = new NodeRSA(privateKey, 'pkcs8-private');
    var decryptedData = priKey.decrypt(encryptedData, 'utf8');
    return decryptedData
}


var text = 'I love Python!'
var encodeData = base64Encode(text)
var decodeData = base64Decode(encodeData)
console.log(text)
console.log(encodeData)
console.log(decodeData)

console.log(md5Encode(text))
console.log(pbkdf2Encrypt(text))
console.log(SHA1Encrypt(text))
console.log(HMACEncrypt(text))

var text = 'I love Python!'  // 待加密对象
var desKey = '6f726c64f2c2057'  // 密钥
var desIv = '0123456789ABCDEF'  // 初始化向量
var encryptedData = desEncrypt(text, desKey = desKey, desIv = desIv)
var decryptedData = desDecrypt(encryptedData, desKey = desKey, desIv = desIv)
console.log("DES 加密字符串：", encryptedData)
console.log("DES 解密字符串：", decryptedData)


var text = 'I love Python!'  // 待加密对象
var desKey = '6f726c64f2c2057'  // 密钥
var desIv = '0123456789ABCDEF'  // 初始化向量
var encryptedData = tripleDesEncrypt(text, desKey = desKey, desIv = desIv)
var decryptedData = tripleDesDescrypt(encryptedData, desKey = desKey, desIv = desIv)
console.log("3DES 加密字符串：", encryptedData)
console.log("3DES 解密字符串：", decryptedData)


var text = 'I love Python!'  // 待加密对象
var aesKey = '6f726c64f2c2057c'  // 密钥, 16倍数
var aesIv =  '0123456789ABCDEF'  // 偏移量， 16倍数
var encryptedData = AESEncrypt(text, aesKey=aesKey, aesIv=aesIv)
var decryptedData = AESDecrypt(encryptedData, aesKey = aesKey, aesIv = aesIv)
console.log("AES 加密字符串：", encryptedData)
console.log("AES 解密字符串：", decryptedData)


var text = 'I love Python!'
var key = '6f726c64f2c2057c'
var encryptedData = RC4Encrypt(text, key=key)
var decryptedData = RC4Decrypt(encryptedData, key=key)
console.log("RC4 加密字符串：", encryptedData)
console.log("RC4 解密字符串：", decryptedData)

var text = "I love Python!"
var key = "6f726c64f2c2057"

var encryptedData = rabbitEncrypt(text, key=key)
var decryptedData = rabbitDecrypt(encryptedData, key=key)

console.log("Rabbit 加密字符串: ", encryptedData)
console.log("Rabbit 解密字符串: ", decryptedData)

// 生成512位秘钥
var key = new NodeRSA({b: 512});
// 导出公钥
var publicKey = key.exportKey('pkcs8-public');
// 导出私钥
var privateKey = key.exportKey('pkcs8-private');
var text = 'I love Python!'

var encryptedData = rsaEncrypt(text, publicKey)
var decryptedData = rsaDecrypt(encryptedData, privateKey)

console.log("key：\n", key)
console.log("公钥：\n", publicKey)
console.log("私钥：\n", privateKey)
console.log("RSA 加密字符串：", encryptedData)
console.log("RSA 解密字符串：", decryptedData)



var s = 'UVE6MjkxMDg5MjI2Mw=='
var s = 'aHR0cHM6Ly93d3cuZG91eWluLmNvbS8='
var s = 'aHR0cHM6Ly93d3cuZG91eWluLmNvbS9hd2VtZS92MS93ZWIvdXNlci9wcm9maWxlL290aGVyLw=='
var s = 'aHR0cHM6Ly93d3cuZG91eWluLmNvbS9hd2VtZS92MS93ZWIvdXNlci9wcm9maWxlL290aGVyLw=='
console.log('base64Decode：' + base64Decode(s))