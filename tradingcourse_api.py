import requests

#定义测试类

class register_test():
    #定义属性，一般是定义在类的初始化方法中
    def __init__(self):
        self.url ="https://apiform.acy.cloud/v1/trading-course"
        self.heads = {"origin": "https://acy.com.au"}
        self.userinfo={}
        self.userinfo={
            "affilate_url": "none",
            "agent_contact": "2",
            "code": "1111",
            "country_code": "61",
            "email": "du@gmail.com",
            "email_lang": "English",
            "first_name": "xinyi",
            "last_name": "xi",
            "lead_source": "",
            "live_cache": "null",
            "others_content": "Fake",
            "phone": "0477390742",
            "refer": "N/A",
            "origin":"https://acy.com.au",
            "request_host": "acy.com.au",
            "signup_page_url": "https://acy.com.au/en/education/trading-course"

        }
    def registertest(self):
        #发送接口请求
        s = requests.session()
        response = s.post(self.url , data=self.userinfo,headers=self.heads).json()
        print(response)
if __name__ == '__main__':
    regisobj = register_test()
    regisobj.registertest()