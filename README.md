# wepy snippets README

## 预览

[wepy 框架代码片段](https://github.com/wleven/wepy-snippets)

![feature X](https://raw.githubusercontent.com/wleven/wepy-snippets/master/images/1.png)

![feature X](https://raw.githubusercontent.com/wleven/wepy-snippets/master/images/2.png)

## 说明

* vscode 插件搜索 `wepy snippets`
* 代码片段关键词 `wepy`
* 将 `wpy` 文件格式设置为 `vue,vue-html,html`
* 支持 `javascript,typescript`
* vsce publish


## 更新日志

* 增加 `wepy.repeat` 代替 `wepy.block`

  ```
  <repeat for="{{data}}" key="index" index="index" item="item">
  </repeat>
  ```
* 修复 `wepy.onShareAppMessage(){}`