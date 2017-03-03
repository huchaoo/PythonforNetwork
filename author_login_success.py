from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

resp = urlopen("http://192.168.3.5/srun_portal_pc_succeed.php").read().decode("utf-8")
soup = BeautifulSoup(resp,"html.parser")

p_success = soup.find("p").string
user_name = soup.find(id = "user_name").string
sum_bytes = soup.find_all(id = "sum_bytes")[1].string
sum_seconds = soup.find(id = "sum_seconds").string

print(p_success)
print(user_name)
print(sum_bytes)
print(sum_seconds)
