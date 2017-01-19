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

html = opener.open(full_url).read()
print(html)
