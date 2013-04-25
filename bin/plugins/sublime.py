# coding: utf-8
import os
import json
import base

def setting_sublime():
  subl_setting_path = base.read_json(base.return_path("init.json"))["editor"]["GoSublimeSetting"]
  subl_setting = base.read_json(subl_setting_path)
  subl_setting["env"]["GOPATH"] = os.getcwd()
  base.write_json(subl_setting, subl_setting_path)