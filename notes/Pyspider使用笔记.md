
1. 安装 Python3
2. 安装虚拟环境 python3 -m .
3. 进入虚拟环境 source bin/activate
4. 安装 Pyspider pip install pyspider



# Scrapy 使用笔记

1. 工作管道
2. XPath
3. 文件读写
4. 数据存储
5. 文档阅读
6. Debug

## 0x06 Debug

启动 venv 环境
```shell
source bin/activate
```

在 VSCode 左边栏的 debug 区域，添加该 json 配置到 launch.json 里

```json
"version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Launch Scrapy Spider",
      "type": "python",
      "request": "launch",
      "module": "scrapy",
      "cwd": "${workspaceFolder}", // 注意路径
      "args": [
        "crawl", 
        "imdb"  // spider name
      ],
      "console": "integratedTerminal"
    }
  ]
```