import configparser
import sys

def getCfg(section,key):
  conf = configparser.ConfigParser()
  print(sys.path[0])
  conf.read(sys.path[0]+"/conf/conf.cfg", encoding='utf-8')
  conf.sections()
  debug = conf.get(section,key)
  return debug