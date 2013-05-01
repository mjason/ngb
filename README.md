ngb - A project management tool for Golang
==========

**ngb** is a useful tool to manage the `src` directory of the `GOPATH`.

NOTE: Windows is not supported in the current version yet. Python 2.6~2.7 is required.


## Installation

```
git clone https://github.com/mjason/ngb.git
mv ngb ~/.ngb
# add `~/.ngb/bin` to your $PATH
```


## Usage

### Create a new project

```
ngb new blog
```

### Add dependencies

Edit `project.json`:

```
{
  "name": "blog",
  "packages":[
    "github.com/ziutek/kasia.go",
    "github.com/gorilla/mux"
  ]
}
```

### Install dependencies

```
$ ngb    # enter prompt
ngb> install
```


* Configure Sublime Text 2 to switch GOPATH automatically.

* Use `ngb install gocode` to install `gocode`.

* Install `GoSublime`

For Mac OS X users: type `subl mac` in prompt.

Linux support is currently under development.

Shell commands is also avalible in ngb.


## Changelog

* Released 0.1.2


## TODO

* Enhence support for Sublime Text 2.
