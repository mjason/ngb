# ngb

一个用来管理go项目的工具，目前仅仅支持mac和linux，windows不支持。

## install

```
git clone https://github.com/mjason/ngb.git
mv ngb ~/.ngb
# 把~/.ngb/bin加入到你的path里面
```

## 使用

- 创建项目

```
ngb new blog
```

- 添加项目依赖

```
# 修改项目的project.json
{
  "name": "blog",
  "packages":[
    "github.com/ziutek/kasia.go",
    "github.com/gorilla/mux"
  ]
}
```

- 安装项目依赖
```
ngb
# 进入交互模式
install
```

开始的时候请进入交互模式，会自动设置gopath

===

# NEW

发布0.1版本
