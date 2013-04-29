import os

def install():
  temp_path = os.getenv("HOME") + "/.ngb"
  os.putenv("GOPATH", temp_path)
  os.putenv("GOBIN", temp_path + "/bin")
  os.system("go get -u github.com/nsf/gocode")
