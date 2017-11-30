from py.urls import app
from conf import conf


if __name__ == '__main__':
  #读取配置项debug配置
  debug= conf.getCfg("app","debug")
  host= conf.getCfg("app","ip")
  print(debug,host)

  app.jinja_env.auto_reload = debug
  app.run(port=8888,host=host,debug=debug)
