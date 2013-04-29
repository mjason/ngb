# ngb
===

在写golang的时候，一个大问题在于，随着使用时间gopath的src目录会十分庞大，而分目录的时候，问题也是很多的，特别是在国内的环境，go get的速度实在太慢了。再者，当把项目提交版本控制的时候，需要在项目说明项目依赖的第三包，十分麻烦。ngb就是为了解决这些问题而创建。
目前这个版本不支持windows，系统需要有python2.6~2.7的版本，不支持python3

## install

```
git clone https://github.com/mjason/ngb.git
mv ngb ~/.ngb
# 把~/.ngb/bin加入到你的path里面
```

## 使用

* 创建项目

```
ngb new blog
```

* 添加项目依赖

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

* 安装项目依赖

```
ngb
# 进入交互模式
install
```


* 配置sublime2 编辑器，使其自动切换GOPATH

* 使用ngb install gocode 进行安装gocode

* 安装GoSublime

mac 进入交互模式后直接输入subl mac
linux 还没有实现



shell里面的命令可以都可以在ngb都可以使用


# NEW
===

发布0.1.2版本

# todo
- 优化对sublime的支持
