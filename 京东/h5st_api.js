// @File   :h5st_api.js
// @Time   :2025/10/11 14:43
// @Author :dayue
// @Email  :ole211@qq.com

const express = require('express');
const app = express();
const fs = require('fs');
const { get_h5st } = require('./h5st_JD_01');

ljc_log = console.log

// 支持 JSON 请求体解析
app.use(express.json());

ljc_log('启动服务...')

// 一个GET接口
app.get('/api/hello', (req, res) => {
    res.json({ message: 'Hello from Node.js backend!' })
})

// 一个POST接口
app.post('/api/data', (req, res) => {
    ljc_log('接受到数据：', req.body)
    res.json({status: 'success', result: get_h5st(req.body['params'])})
})

// 监听端口3000
const PORT = 3000
app.listen(PORT, () => {
    ljc_log(`Server is running at http://localhost:${PORT}`)
})