# coding: utf-8

import cmd
import sys
import os
import json
from string import Template
from plugins import sublime
from plugins import gocode

def return_path():
  return os.path.split(os.path.realpath(__file__))[0]

def read_file(path=""):
  file_ = open(path)
  text = file_.read()
  file_.close()
  return text

def read_json(path=""):
  json_text = read_file(path)
  return json.loads(json_text)

def write_file(w="", path=""):
  file_ = open(path, 'w')
  file_.write(w)
  file_.close()

def write_json(w, path=""):
  write_file(json.dumps(w), path)

def create(name=""):
  try:
    os.mkdir(name)
  except OSError:
    print "已存在此文件名"
    sys.exit(1)
  except:
    print "未知错误"
    sys.exit(1)

  os.mkdir("./" + name + "/bin")
  os.mkdir("./" + name + "/src")
  os.mkdir("./" + name + "/pkg")
  os.mkdir("./" + name + "/ngb")

  project_tempalte = Template(read_file(return_path() + "/project.json"))
  write_file(project_tempalte.substitute(name=name), "./" + name + "/project.json")
  print "创建完成, 请进入" + name + "运行ngb 进入控制台"

def install():
  pkg_list = read_json("./project.json")["packages"]
  temp_path = os.getenv("HOME") + "/.ngb"
  os.putenv("GOPATH", temp_path)
  try:
    for name in pkg_list:
      print "install " + name
      os.system("go get " + name)
      for path in os.listdir(temp_path + "/src"):
        os.symlink(temp_path+"/src/" + path, "./src/" + path)
  except:
    pass
  os.putenv("GOPATH",os.getcwd())
  for name in pkg_list:
    os.system("go install " + name)
  print "all is ok"


class Ngb(cmd.Cmd):
  def __init__(self):
    cmd.Cmd.__init__(self)
    self.do_hello(self)
    self.prompt = '=> '

  def do_hello(self, arg):
    os.putenv("GOPATH", os.getcwd())
    if read_json(return_path() + "/conf/init.json")["editor"]["GoSublimeSetting"] != "":
      sublime.setting_sublime()
    print "ngb is a tool for working with golang projects"
    print """Several tasks are available:
install   go get install project pkg
run       go run this project main.go"""

  def do_exit(self, arg):
    return True

  def do_subl(self, arg):
    if len(arg) != 0 and str(arg) == "mac":
      subl_json = read_json(return_path() + "/conf/init.json")
      subl_json["editor"]["GoSublimeSetting"] = os.getenv("HOME") + "/Library/Application Support/Sublime Text 2/Packages/User/GoSublime.sublime-settings"
      write_json(subl_json, return_path() + "/conf/init.json")
    else:
      subl_json = read_json(return_path() + "/conf/init.json")
      subl_json["editor"]["GoSublimeSetting"] = ""
      write_json(subl_json, return_path() + "/conf/init.json")

  def do_install(self, arg):
    print "install ...."
    install()

  def do_EOF(self, line):
    return True

  def do_run(self, arg):
    print "go run main.go"
    os.system("go run ./src/main.go")

  def do_test(self, arg):
    print "go run main.go"

  def do_g(self, arg):
    print len(arg)

  def default(self, line):
    os.system(line)

if __name__ == '__main__':
  if len(sys.argv) == 3 and sys.argv[1] == "new":
    create(sys.argv[2])
    sys.exit(1)
  elif len(sys.argv) == 3 and sys.argv[1] == "subl":
    setting(sys.argv[2])
    sys.exit(1)
  elif len(sys.argv) == 3 and sys.argv[1] == "code":
    gocode.install()
  a = Ngb()
  a.cmdloop()