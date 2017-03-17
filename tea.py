#!usr/bin/env/python
import fire
from requests import get
from json import loads

_url="35.164.228.234"
def mytea(name):
    global _url
    msg = get('http://{url}:5000/countme/{name}'.format(url=_url,name=name))
    return msg.content
    
def tealist():
    global _url
    teal = get('http://{url}:5000/listtea'.format(url=_url))
    tea=loads(teal.content)
    print tea
    print "total cups of tea =>",len(tea)
    return

def clear():
    global _url
    teal = get('http://{url}:5000/clear.format(url=_url)')
    print "list cleared"
    return



if __name__ == '__main__':
   fire.Fire({
      'mytea': mytea,
      'tealist':tealist,
      'clear':clear
  })