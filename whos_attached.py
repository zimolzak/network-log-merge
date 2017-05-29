import urllib.request
import pdb
import urllib.error as uerror

top_level_url = 'http://www.routerlogin.net/'
full_url = top_level_url + 'DEV_show_device.htm'
username = 'admin'
password = open('pwd.txt').readline()
password = password.replace('\n', '')

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, top_level_url, username, password)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)


try:
   html = opener.open(full_url).read().decode("utf-8").splitlines()
   #                            bytes -->   str       -->  list
except uerror.HTTPError as h_error:
    print("Caught error '" + str(h_error) + "'. Quitting.")
    quit()

attach_array = []
junk_lines = []
attach_dev_mac = []
deviceIP_name = []
for line in html:
   if line.startswith("var attach_device_list"):
      #print(line)
      attach_device_list = line.replace('var attach_device_list="', '')
      attach_device_list = attach_device_list.replace(' @\#$\&*!";', '').replace('\\', '')
      attach_array = attach_device_list.split(' @#$&*! ')
   elif line.startswith("var attach_dev_mac"):
      attach_dev_mac.append(line)
   elif line.startswith("var deviceIP_name") and not line.startswith("var deviceIP_name_num"):
      deviceIP_name.append(line)
   elif line.startswith("var "):
      junk_lines.append(line)

print("attach_device_list\n====")
print('\n'.join([e.replace(' ', '\t') for e in attach_array]) + '\n')

print("attach_dev_mac\n====")
print('\n'.join(attach_dev_mac) + '\n')

print("deviceIP_name\n====")
print('\n'.join(deviceIP_name) + '\n')

print("junk lines\n====")
print("\n".join(junk_lines) + '\n')
