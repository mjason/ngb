# coding: utf-8

import cmd
import sys
import os
from string import Template
import json
import shutil

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
  project_file = open(os.getenv("HOME") + "/.ngb/bin/project.json")
  project_string = project_file.read()
  project_file.close()
  project_template = Template(project_string)
  project_string = project_template.substitute(name=name)
  project_file = open("./" + name + "/project.json", 'w')
  project_file.write(project_string)
  project_file.close()
  print "创建完成, 请进入" + name + "运行ngb 进入控制台"

def install():
  project_file = open("./project.json")
  project_string = project_file.read()
  project_file.close()
  project_data = json.loads(project_string)
  pkg_list = project_data["packages"]
  os.putenv("GOPATH", os.getenv("HOME") + "/.ngb")
  for name in pkg_list:
    print "install " + name
    os.system("go get " + name)
    for path in os.listdir(os.getenv("HOME") + "/.ngb/src"):
      os.symlink(os.getenv("HOME") + "/.ngb/src/" + path, "./src/" + path)
  print "all is ok"

class Ngb(cmd.Cmd):
  def __init__(self):
    cmd.Cmd.__init__(self)
    self.do_hello(self)
    self.prompt = '=> '

  def do_hello(self, arg):
    os.putenv("GOPATH", os.getcwd())
    print "ngb is a tool for working with golang projects"
    print """Several tasks are available:
install   go get install project pkg
run       go run this project main.go"""

  def do_exit(self, arg):
    return True

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
  a = Ngb()
  a.cmdloop()