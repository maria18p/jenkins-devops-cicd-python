import fire

def hello(sum=100):
  return "Calculate tax %s!" % sum*0.17

if __name__ == '__main__':
  fire.Fire(hello)