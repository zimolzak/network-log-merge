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

def un_javascript(s):
   """Input string assignment code, return what's between the double
   quotes.
   """
   assert s.count('"') == 2
   s = s[s.index('"') + 1 : ] # delete everything up to 1st quote
   return s[:s.index('"')]

attach_array = []
junk_lines = []
attach_dev_mac = []
deviceIP_name = []
for line in html:
   if line.startswith("var attach_device_list"):
      attach_device_list = line.replace('var attach_device_list="', '')
      attach_device_list = attach_device_list.replace(' @\#$\&*!";', '').replace('\\', '')
      attach_array = attach_device_list.split(' @#$&*! ')
   elif line.startswith("var attach_dev_mac"):
      attach_dev_mac.append(un_javascript(line))
   elif line.startswith("var deviceIP_name") and not line.startswith("var deviceIP_name_num"):
      deviceIP_name.append(un_javascript(line))
   elif line.startswith("var "):
      junk_lines.append(line)

merged = ([e.replace(' ', '\t') for e in attach_array] +
          [e.replace(' ', '\t__:__:__:__:__:__\t') for e in deviceIP_name])
merged.sort()

found_macs = []
for m in merged:
   mac = m.split()[1].lower()
   if mac in attach_dev_mac:
      found_macs.append(mac)
      attach_dev_mac.remove(mac)

#### print ####

print("\n".join(merged))
for e in attach_dev_mac:
   print("___.___._._\t" + e)
print("\n")

print("found macs\n====")
print('\n'.join(found_macs) + '\n')
print("junk lines\n====")
print("\n".join(junk_lines) + '\n')
