print("*****webscraping*****")
import re,urllib
import urllib.request
sites=['http://google.com','http://youtube.com']
for s in sites :
  print(s)
  u=urllib.request.urlopen(s)
  text=u.read()
  print(text)
  #title=re.findall("<title>.*</title>",str(text),re.IGNORECASE)
  #print(title[0])
