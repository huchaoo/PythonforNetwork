def func_login(username,password):

    from urllib.request import urlopen
    from urllib.request import Request
    from urllib import parse
    from bs4 import BeautifulSoup

    req = Request("http://192.168.3.5/include/auth_action.php")

    postData = parse.urlencode([
        ("action", "login"),
        ("username", username),
        ("password", password),
        ("ac_id", "1"),
        ("user_ip", ""),
        ("nas_ip", ""),
        ("user_mac", ""),
        ("save_me", "0"),
        ("ajax", "1"),
    ])

    req.add_header("Origin", "http://192.168.3.5")
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36")
    resp = urlopen(req, data=postData.encode('utf-8')).read().decode("utf-8")

    if "login_ok" in resp:
        success_resp = urlopen("http://192.168.3.5/srun_portal_pc_succeed.php").read().decode("utf-8")
        soup = BeautifulSoup(success_resp, "html.parser")

        user_name = soup.find(id="user_name").string
        sum_bytes = soup.find_all(id="sum_bytes")[1].string
        sum_seconds = soup.find(id="sum_seconds").string

        print("登陆成功！")

        print("用户名：" + user_name)
        print("总共流量：" + sum_bytes)
        print("总共时间：" + sum_seconds)

        return 1;
    else:
        print("登录失败！")
        return 0;




func_login(username="222015602053038",password="{B}MTk5NzA3MDY=");


