# site-mirror-py

这是一个通用的爬虫, 整站下载工具, 可以下载包括页面, 图片, css样式及js文件的所有资源, 并存储到本地指定目录下. 

python版本: 3.7

## `我的更改`

- [x] 添加要删除的选择器，见 crawler/config.py中的selectors_to_remove
  - 示例值：`#idName`，`.className`，`div#idName`，`div.className`等
- [x] 访问频繁时的文本，见 crawler/config.py中的access_too_frequent_texts
- [x] 保存文件时若已存在就跳过


## 功能特性

1. 指定抓取深度(0为不限深度, 1为只抓取单页面)
2. 可以通过配置指定不下载图片, css, js或字体等资源
3. 设置黑名单以屏蔽指定链接的资源

完成后可以通过仓库中的`docker-compose.yml`启动一个nginx容器从本地访问.

注意: 本工具只能下载静态页面, 对于通过js动态加载的内容无能为力(比如bilibili), 一般只限于文章, 图片, 新闻资讯等网站.

## 使用方法

安装依赖

```
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

修改`main.py`入口程序, 主要是两个配置项

1. main_url: 目标网站主页
2. max_depth: 抓取深度

其他配置项见`crawler/config.py`.

## 扩展

同类的golang版本见

- [site-mirror-go github](https://github.com/generals-space/site-mirror-go)
- [site-mirror-go 码云](https://gitee.com/generals-space/site-mirror-go)

实现逻辑相同.

------

效果截图

![](./doc/src/screenshot.jpg)