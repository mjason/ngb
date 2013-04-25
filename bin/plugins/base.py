import json
import os

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

def return_path(name=""):
  return os.path.split(os.path.realpath(__file__))[0] + "/../conf/" + name