import urllib.request
import pdb

top_level_url = 'http://routerlogin.net/'
full_url = top_level_url + 'DEV_show_device.htm'

fancy = True

if fancy:


   password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
   username = 'admin'
   password = open('pwd.txt').readline()
   password = password.replace('\n', '')

   password_mgr.add_password(None, top_level_url, username, password)
   handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
   opener = urllib.request.build_opener(handler)

   # pdb.set_trace()

   html = opener.open(full_url).read()
   print(html)
   quit()

   urllib.request.install_opener(opener)

   with urllib.request.urlopen(full_url) as response:
      html = response.read()
      print(html)


else:

   with urllib.request.urlopen(dumb) as response:
      html = response.read()
      print(html)
