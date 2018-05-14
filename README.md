# wepy weui 框架代码片段


[Github,欢迎star,欢迎issues](https://github.com/wleven/wepy-snippets)

![feature X](https://raw.githubusercontent.com/wleven/wepy-snippets/master/images/1.png)

![feature X](https://raw.githubusercontent.com/wleven/wepy-snippets/master/images/2.png)




## 说明
* `wepy weui`代码片段
* vscode 插件搜索 `wepy snippets`
* 代码片段关键词 `wepy`
* 将 `wpy` 文件格式设置为 `vue,vue-html,html`
* 支持 `javascript,typescript`




## NodeJs 构建
模块化构建代码片段 `npm run build`


## Python 构建
现在 snippets 目录中的代码片段配置由 snippets-src 中的定义的源文件经过 `make_snippets.py` 脚本生成。
也可以直接在此项目根目录运行 `make_snippets.sh` 生成。

`snippets-src` 中的代码片段配置已经尽可能被简化了。
例如 `wepy.page` 的配置如下：

```json
  "wepy.page": {
    "description": "快速添加页面代码"
  }
```

最后生成的配置会自动补充上所需要的字段。
1. `prefix` 会直接使用对应配置的 `key` 
2. `scope` 统一在 `make_snippets.py` 脚本中配置。
3. `body` 中如果没有指定字段则自动查找  `includes/wepy.page.<ext>` 的文件内容包含进来。 也可以指定其他文件。原来的指定字符串，或者数组的方式依然 OK（只是对于比较长的补全代码，建议写在单独的文件中）

更多具体细节见 `make_snippets.py` 脚本文件。

