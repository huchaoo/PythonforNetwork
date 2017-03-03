# post

from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request("http://192.168.3.5/include/auth_action.php")

postData = parse.urlencode([
    ("action", "login"),
    ("username" ,"222015602053038"),
    ("password", "{B}MTk5NzA3MDY="),
    ("ac_id", "1"),
    ("user_ip", ""),
    ("nas_ip", ""),
    ("user_mac", ""),
    ("save_me", "0"),
    ("ajax", "1"),
])

req.add_header("Origin","http://192.168.3.5")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36")
resp = urlopen(req,data = postData.encode('utf-8'))

print(resp.read().decode("utf-8"))
