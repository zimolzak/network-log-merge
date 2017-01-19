import urllib.request
import pdb

top_level_url = 'http://routerlogin.net/'
full_url = top_level_url + 'DEV_show_device.htm'
username = 'admin'
password = open('pwd.txt').readline()
password = password.replace('\n', '')

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, top_level_url, username, password)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)

html = opener.open(full_url).read().decode("utf-8").splitlines()
#                            bytes -->   str       -->  list

for line in html:
   if line.startswith("var attach_device_list"):
      attach_device_list = line.replace('var attach_device_list="', '')
      attach_device_list = attach_device_list.replace('";', '').replace('\\', '')
      attach_array = attach_device_list.split(' @#$&*! ')
      print('\n'.join([e.replace(' ', '\t') for e in attach_array]))
