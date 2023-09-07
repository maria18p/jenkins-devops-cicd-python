import fire

def hello(name=1):
  return "Calculated tax equals %s!" % name*0.17

if __name__ == '__main__':
  fire.Fire(hello)