import fire
from requests import get
from json import loads


def countme(name):
    msg = get('http://localhost:5000/countme/{name}'.format(name=name))
    return msg.content
    
def listtea():
    teal = get('http://localhost:5000/listtea')
    tea=loads(teal.content)
    print tea
    print "total cups of tea =>",len(tea)
    return



if __name__ == '__main__':
   fire.Fire({
      'countme': countme,
      'listtea': listtea,
  })