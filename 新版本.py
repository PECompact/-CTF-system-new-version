# coding=gbk
from __future__ import print_function
from urllib.parse import quote, unquote
import sys
import time as t
import easygui as e
import hashlib
import base64
import time
class NAME():
    def __init__(self):
        self.card_name = "Sure"
        self.card_psd = "0000"
        self.card_Integral = "unknown"

        self.card1_name = "PECompact"
        self.card1_psd = "qazwsx"
        self.card1_Integral = 90

        self.card2_name = "Zero two"
        self.card2_psd = "0000"
        self.card2_Integral = "unknown"

        self.card3_name = "薛梓文"
        self.card3_psd = "0000"
        self.card3_Integral = "unknown"

        self.card4_name = "李昊霖"
        self.card4_psd = "0000"
        self.card4_Integral = "unknown"

        self.card5_name = "李卓阳"
        self.card5_psd = "0000"
        self.card5_Integral = "unknown"

        self.card6_name = "汪恩皓宇"
        self.card6_psd = "0000"
        self.card6_Integral = "unknown"

        self.card7_name = "张光泽"
        self.card7_psd = "0000"
        self.card7_Integral = "unknown"

        self.new_name = {}#"q"
        self.new_psd = {}#"q"
        self.new_Integral = "unknown"

        self.name = f"name1(developer): {self.card1_name}\nname2: {self.card2_name}\nname3: {self.card3_name}\nname4: {self.card4_name}\nname5: {self.card5_name}\nname6: {self.card6_name}\nname7: {self.card7_name}\nteacher: {self.card_name}"
Name = NAME()
class CODE():
    def __init__(self):
        self.l = 0
        self.i = 0
        self.f = 0
        self.b = 0
        self.con = False
        self.q = 30
        self.a = 3369
        self.psd2 = 123456789
        self.psd3 = 0
        self.new_member = 0
        self.new_Member = ""
        self.vi = "1.0:更新登录系统（简易）\n1.2：更新可多人员登录\n1.2.1：修复无法正常登陆的bug\n1.4：更新了登陆菜单\n1.5：修改至全英文\n1.6：优化了登录界面\n1.7：更新了智能检测未知错误功能\n1.8：加强了密码登陆的准确性\n1.9：修复了管理员验证后无法正常退出循环的bug\n2.0：增加了查看以往版本更新信息功能\n2.1：修复了失败验证管理员密码后再次验证成功无法正常退出的bug\n2.2：修复了第三次验证第一层密码成功时无法正常进入系统的bug\n2.3：更新了返回登录界面的功能\n2.4：修复了输入非整数时报错的bug\n2.5：新增'工具'服务\n2.6：优化程序算法\n2.7：修复无法正常编译运行的bug\n2.8：修复管理员密码错误问题\n2.9：优化异常处理内容\n3.0：修复已知问题，提高程序稳定性"

    # 进行MD5加密
    def md5(self,s):
        # new_id = e.enterbox(msg="new_ID", title="'Hack' systems")
        original = s
        md = hashlib.md5()
        s = s.encode(encoding='utf-8')
        md.update(s)
        e.msgbox('Original:' + original, title="'CTF' systems")
        e.msgbox('Md5 Encryption:' + md.hexdigest(), title="'CTF' systems")
    # 进行sh1加密
    def sh1(self,s):
        original = s
        sh = hashlib.sha1()
        s = s.encode(encoding='utf-8')
        e.msgbox('Original:' + original, title="'CTF' systems")
        e.msgbox('SH1 Encryption:' + sh.hexdigest(), title="'CTF' systems")
    # 将字符串转换为base64编码格式
    def strToB64(self,s):
        encode = base64.b64encode(s.encode("utf-8"))
        e.msgbox('Original:' + s, title="'CTF' systems")
        e.msgbox('Base64 encode:' + str(encode), title="'CTF' systems")
    # 将base64编码格式转化为正常的字符类型
    def b64ToStr(self,s):
        decode = base64.b64decode(str(s))
        e.msgbox('Base64:' + s, title="'CTF' systems")
        e.msgbox('Base64 decode:' + str(decode), title="'CTF' systems")
    # 将字符串转为b32编码格式
    def strToB32(self,s):
        encode = base64.b32encode(s.encode("utf-8"))
        e.msgbox('Original:' + s, title="'CTF' systems")
        e.msgbox('Base32 encode:' + str(encode), title="'CTF' systems")
    # 将base32编码格式转化为正常的字符类型
    def b32ToStr(self,s):
        decode = base64.b32decode(str(s))
        e.msgbox('Base32:' + s, title="'CTF' systems")
        e.msgbox('Base32 decode:' + str(decode), title="'CTF' systems")
    # 将字符串转为base16编码格式
    def strToB16(self,s):
        encode = base64.b16encode(s.encode("utf-8"))
        e.msgbox('Original:' + s, title="'CTF' systems")
        e.msgbox('Base16 encode:' + str(encode), title="'CTF' systems")
    # 将base16编码格式转化为正常的字符类型
    def b16ToStr(self,s):
        decode = base64.b16decode(str(s))
        e.msgbox('Base16:' + s, title="'CTF' systems")
        e.msgbox('Base16 decode:' + str(decode), title="'CTF' systems")
    # 将二进制转化为十进制
    def binToDec(self,s):
        result = int(s, 2)
        e.msgbox('Binary :' + str(s), title="'CTF' systems")
        e.msgbox('Decimal :' + str(result), title="'CTF' systems")
    # 将八进制转化为十进制
    def octToDec(self,s):
        result = int(s, 8)
        e.msgbox('Octal :' + str(s) + s, title="'CTF' systems")
        e.msgbox('Decimal :' + str(result), title="'CTF' systems")
    # 将十六进制转化为十进制
    def hexToDec(self,s):
        result = int(s, 16)
        e.msgbox('Hex :' + str(s) + s, title="'CTF' systems")
        e.msgbox('Decimal :' + str(result), title="'CTF' systems")
    # 将十进制转化为二进制
    def decToBin(self,s):
        s = int(s)
        result = bin(s)
        e.msgbox('Decimal:' + str(s), title="'CTF' systems")
        e.msgbox('Binary:' + str(result), title="'CTF' systems")
    # 将十进制转化为八进制
    def decToOct(self,s):
        s = int(s)
        result = oct(s)
        e.msgbox('Decimal :' + str(s), title="'CTF' systems")
        e.msgbox('Octal :' + str(result), title="'CTF' systems")
    # 将十进制转化为十六进制
    def decToHex(self,s):
        s = int(s)
        result = hex(s)
        e.msgbox('Decimal :' + str(s), title="'CTF' systems")
        e.msgbox('Hex :' + str(result), title="'CTF' systems")
    # 进行url编码
    def url_encode(self,s):
        encode = quote(s)
        e.msgbox('Original:' + s, title="'CTF' systems")
        e.msgbox('URL encode:' + encode, title="'CTF' systems")
    # 进行url编码
    def url_decode(self,s):
        decode = unquote(s)
        e.msgbox('URL encode:' + s, title="'CTF' systems")
        e.msgbox('URL decode:' + decode, title="'CTF' systems")
    # 将字母转化为对应的ASCII
    def lettToASCII(self,s):
        e.msgbox('Letters:' + s, title="'CTF' systems")
        result = ''
        for i in s:
            result = result + str(ord(i)) + ' '
        e.msgbox('ASCII  :' + result, title="'CTF' systems")
    # 将ASCII转化为对应的字母以及字符
    def asciiToLett(self,s):
        list = s.split(' ')
        result = ''
        e.msgbox('ASCII    :' + s, title="'CTF' systems")
        for i in list:
            i = int(i)
            result = result + chr(i)
        e.msgbox('Letters  :' + result, title="'CTF' systems")
    def gly(self):  # 跳出多次循环(管理员验证)
        while True:
            try:
                print("··········锁定屏幕超过3次，请联系管理员··········")
                self.psd3 = int(input("请输入管理员密码\t"))
            except ValueError:
                print("输入有误，不能为非数字")
            except BaseException as e:
                print("出现异常")
                print(repr(e))
            if self.psd3 == self.psd2:  # 管理员密码
                return
Code = CODE()
class CARD():
    def __init__(self):
        #个人中心
        self.n1 = {"你的名字:": Name.card1_name, "你的密码:": Name.card1_psd}
        self.n2 = {"你的名字:": Name.card2_name, "你的密码:": Name.card2_psd}
        self.n3 = {"你的名字:": Name.card3_name, "你的密码:": Name.card3_psd}
        self.n4 = {"你的名字:": Name.card4_name, "你的密码:": Name.card4_psd}
        self.n5 = {"你的名字:": Name.card5_name, "你的密码:": Name.card5_psd}
        self.n6 = {"你的名字:": Name.card6_name, "你的密码:": Name.card6_psd}
        self.n7 = {"你的名字:": Name.card7_name, "你的密码:": Name.card7_psd}
        self.n = {"你的名字:": Name.card_name, "你的密码:": Name.card_psd}
        self.n_new = {"你的名字:": Name.new_name, "你的密码:": Name.new_psd}

    def card1(self):  # 用户信息
        e.msgbox("登陆成功", title="'CTF' systems", ok_button="OK")
        while True:  # 服务
            b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                            choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
            if b == "成员":  # 成员信息
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "积分":  # 积分
                e.msgbox(Name.card1_Integral, title="'CTF' systems")
            elif b == "版本信息":  # 版本信息
                e.msgbox(Code.vi, title="'CTF' systems")
            elif b == "解码,编码工具":  # 解码编码工具
                tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                             "conversion of number systems", "ASCII"))
                if tools == "MD5 encryption":  # MD5加密
                    Code.md5(e.enterbox(msg="original:"))
                elif tools == "sh1 encryption":  # shi加密
                    Code.sh1(e.enterbox(msg="original:"))
                elif tools == "The family of the Base":  # Base
                    base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                       choices=("base64", "base32", "base16"))
                    if base == "base64":  # base64编,解码
                        Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base64 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base64 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base32":  # base32编，解码
                        Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base32 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base32 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base16":  # base16编，解码
                        Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base16 == "encode":  # base16编码
                            Code.strToB16(e.enterbox(msg=""))
                        elif Base16 == "decode":  # base16解码
                            Code.b16ToStr(e.enterbox(msg=""))
                elif tools == "conv6ersion of number systems":  # 进制转换
                    systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                          choices=("二进制转化为十进制", "八进制转化为十进制",
                                                   "十六进制转化为十进制", "十进制转化为二进制",
                                                   "十进制转化为八进制", "十进制转化为十六进制"))
                    if systems == "二进制转化为十进制":
                        Code.binToDec(e.enterbox(msg="输入整数"))
                    elif systems == "八进制转化为十进制":
                        Code.octToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十六进制转化为十进制":
                        Code.hexToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为二进制":
                        Code.decToBin(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为八进制":
                        Code.decToOct(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为十六进制":
                        Code.decToHex(e.enterbox(msg="输入整数"))
                elif tools == "url":  # url
                    url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("encode", "decode"))
                    if url == "encode":  # url解码
                        Code.url_encode(e.enterbox(msg=""))
                    elif url == "decode":  # url编码
                        Code.url_decode(e.enterbox(msg=""))
                elif tools == "ASCII":  # ASCII
                    ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                        choices=("encode", "decode"))
                    if ASCII == "encode":  # ASCII解码
                        Code.lettToASCII(e.enterbox(msg=""))
                    elif ASCII == "decode":  # ASCII编码
                        Code.asciiToLett(e.enterbox(msg=""))
            elif b == "个人中心":  # 个人中心
                e.msgbox(self.n1, title="'CTF' systems", ok_button="OK")
            elif b == "返回登录界面":  # 返回登录界面
                Quit1 = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit1 == "yes":
                    return
                elif Quit1 == "no":
                    continue
            elif b == "退出":  # 退出
                Quit = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit == "yes":
                    sys.exit()
                elif Quit == "no":
                    continue
    def card2(self):  # 用户信息
        e.msgbox("登陆成功", title="'CTF' systems", ok_button="OK")
        while True:  # 服务
            b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                            choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
            if b == "成员":  # 成员信息
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "积分":  # 积分
                e.msgbox(Name.card2_Integral, title="'CTF' systems")
            elif b == "版本信息":  # 版本信息
                e.msgbox(Code.vi, title="'CTF' systems")
            elif b == "解码,编码工具":  # 解码编码工具
                tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                             "conversion of number systems", "ASCII"))
                if tools == "MD5 encryption":  # MD5加密
                    Code.md5(e.enterbox(msg="original:"))
                elif tools == "sh1 encryption":  # shi加密
                    Code.sh1(e.enterbox(msg="original:"))
                elif tools == "The family of the Base":  # Base
                    base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                       choices=("base64", "base32", "base16"))
                    if base == "base64":  # base64编,解码
                        Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base64 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base64 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base32":  # base32编，解码
                        Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base32 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base32 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base16":  # base16编，解码
                        Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base16 == "encode":  # base16编码
                            Code.strToB16(e.enterbox(msg=""))
                        elif Base16 == "decode":  # base16解码
                            Code.b16ToStr(e.enterbox(msg=""))
                elif tools == "conversion of number systems":  # 进制转换
                    systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                          choices=("二进制转化为十进制", "八进制转化为十进制",
                                                   "十六进制转化为十进制", "十进制转化为二进制",
                                                   "十进制转化为八进制", "十进制转化为十六进制"))
                    if systems == "二进制转化为十进制":
                        Code.binToDec(e.enterbox(msg="输入整数"))
                    elif systems == "八进制转化为十进制":
                        Code.octToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十六进制转化为十进制":
                        Code.hexToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为二进制":
                        Code.decToBin(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为八进制":
                        Code.decToOct(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为十六进制":
                        Code.decToHex(e.enterbox(msg="输入整数"))
                elif tools == "url":  # url
                    url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("encode", "decode"))
                    if url == "encode":  # url解码
                        Code.url_encode(e.enterbox(msg=""))
                    elif url == "decode":  # url编码
                        Code.url_decode(e.enterbox(msg=""))
                elif tools == "ASCII":  # ASCII
                    ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                        choices=("encode", "decode"))
                    if ASCII == "encode":  # ASCII解码
                        Code.lettToASCII(e.enterbox(msg=""))
                    elif ASCII == "decode":  # ASCII编码
                        Code.asciiToLett(e.enterbox(msg=""))
            elif b == "个人中心":  # 个人中心
                e.msgbox(self.n2, title="'CTF' systems", ok_button="OK")
            elif b == "返回登录界面":  # 返回登录界面
                Quit1 = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit1 == "yes":
                    return
                elif Quit1 == "no":
                    continue
            elif b == "退出":  # 退出
                Quit = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit == "yes":
                    sys.exit()
                elif Quit == "no":
                    continue
    def card3(self):  # 用户信息
        e.msgbox("登陆成功", title="'CTF' systems", ok_button="OK")
        while True:  # 服务
            b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                            choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
            if b == "成员":  # 成员信息
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "积分":  # 积分
                e.msgbox(Name.card3_Integral, title="'CTF' systems")
            elif b == "版本信息":  # 版本信息
                e.msgbox(Code.vi, title="'CTF' systems")
            elif b == "解码,编码工具":  # 解码编码工具
                tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                             "conversion of number systems", "ASCII"))
                if tools == "MD5 encryption":  # MD5加密
                    Code.md5(e.enterbox(msg="original:"))
                elif tools == "sh1 encryption":  # shi加密
                    Code.sh1(e.enterbox(msg="original:"))
                elif tools == "The family of the Base":  # Base
                    base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                       choices=("base64", "base32", "base16"))
                    if base == "base64":  # base64编,解码
                        Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base64 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base64 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base32":  # base32编，解码
                        Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base32 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base32 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base16":  # base16编，解码
                        Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base16 == "encode":  # base16编码
                            Code.strToB16(e.enterbox(msg=""))
                        elif Base16 == "decode":  # base16解码
                            Code.b16ToStr(e.enterbox(msg=""))
                elif tools == "conversion of number systems":  # 进制转换
                    systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                          choices=("二进制转化为十进制", "八进制转化为十进制",
                                                   "十六进制转化为十进制", "十进制转化为二进制",
                                                   "十进制转化为八进制", "十进制转化为十六进制"))
                    if systems == "二进制转化为十进制":
                        Code.binToDec(e.enterbox(msg="输入整数"))
                    elif systems == "八进制转化为十进制":
                        Code.octToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十六进制转化为十进制":
                        Code.hexToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为二进制":
                        Code.decToBin(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为八进制":
                        Code.decToOct(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为十六进制":
                        Code.decToHex(e.enterbox(msg="输入整数"))
                elif tools == "url":  # url
                    url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("encode", "decode"))
                    if url == "encode":  # url解码
                        Code.url_encode(e.enterbox(msg=""))
                    elif url == "decode":  # url编码
                        Code.url_decode(e.enterbox(msg=""))
                elif tools == "ASCII":  # ASCII
                    ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                        choices=("encode", "decode"))
                    if ASCII == "encode":  # ASCII解码
                        Code.lettToASCII(e.enterbox(msg=""))
                    elif ASCII == "decode":  # ASCII编码
                        Code.asciiToLett(e.enterbox(msg=""))
            elif b == "个人中心":  # 个人中心
                e.msgbox(self.n3, title="'CTF' systems", ok_button="OK")
            elif b == "返回登录界面":  # 返回登录界面
                Quit1 = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit1 == "yes":
                    return
                elif Quit1 == "no":
                    continue
            elif b == "退出":  # 退出
                Quit = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit == "yes":
                    sys.exit()
                elif Quit == "no":
                    continue
    def card4(self):  # 用户信息
        e.msgbox("登陆成功", title="'CTF' systems", ok_button="OK")
        while True:  # 服务
            b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                            choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
            if b == "成员":  # 成员信息
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "积分":  # 积分
                e.msgbox(Name.card4_Integral, title="'CTF' systems")
            elif b == "版本信息":  # 版本信息
                e.msgbox(Code.vi, title="'CTF' systems")
            elif b == "解码,编码工具":  # 解码编码工具
                tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                             "conversion of number systems", "ASCII"))
                if tools == "MD5 encryption":  # MD5加密
                    Code.md5(e.enterbox(msg="original:"))
                elif tools == "sh1 encryption":  # shi加密
                    Code.sh1(e.enterbox(msg="original:"))
                elif tools == "The family of the Base":  # Base
                    base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                       choices=("base64", "base32", "base16"))
                    if base == "base64":  # base64编,解码
                        Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base64 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base64 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base32":  # base32编，解码
                        Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base32 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base32 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base16":  # base16编，解码
                        Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base16 == "encode":  # base16编码
                            Code.strToB16(e.enterbox(msg=""))
                        elif Base16 == "decode":  # base16解码
                            Code.b16ToStr(e.enterbox(msg=""))
                elif tools == "conversion of number systems":  # 进制转换
                    systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                          choices=("二进制转化为十进制", "八进制转化为十进制",
                                                   "十六进制转化为十进制", "十进制转化为二进制",
                                                   "十进制转化为八进制", "十进制转化为十六进制"))
                    if systems == "二进制转化为十进制":
                        Code.binToDec(e.enterbox(msg="输入整数"))
                    elif systems == "八进制转化为十进制":
                        Code.octToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十六进制转化为十进制":
                        Code.hexToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为二进制":
                        Code.decToBin(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为八进制":
                        Code.decToOct(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为十六进制":
                        Code.decToHex(e.enterbox(msg="输入整数"))
                elif tools == "url":  # url
                    url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("encode", "decode"))
                    if url == "encode":  # url解码
                        Code.url_encode(e.enterbox(msg=""))
                    elif url == "decode":  # url编码
                        Code.url_decode(e.enterbox(msg=""))
                elif tools == "ASCII":  # ASCII
                    ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                        choices=("encode", "decode"))
                    if ASCII == "encode":  # ASCII解码
                        Code.lettToASCII(e.enterbox(msg=""))
                    elif ASCII == "decode":  # ASCII编码
                        Code.asciiToLett(e.enterbox(msg=""))
            elif b == "个人中心":  # 个人中心
                e.msgbox(self.n4, title="'CTF' systems", ok_button="OK")
            elif b == "返回登录界面":  # 返回登录界面
                Quit1 = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit1 == "yes":
                    return
                elif Quit1 == "no":
                    continue
            elif b == "退出":  # 退出
                Quit = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit == "yes":
                    sys.exit()
                elif Quit == "no":
                    continue
    def card5(self):  # 用户信息
        e.msgbox("登陆成功", title="'CTF' systems", ok_button="OK")
        while True:  # 服务
            b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                            choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
            if b == "成员":  # 成员信息
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "积分":  # 积分
                e.msgbox(Name.card5_Integral, title="'CTF' systems")
            elif b == "版本信息":  # 版本信息
                e.msgbox(Code.vi, title="'CTF' systems")
            elif b == "解码,编码工具":  # 解码编码工具
                tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                             "conversion of number systems", "ASCII"))
                if tools == "MD5 encryption":  # MD5加密
                    Code.md5(e.enterbox(msg="original:"))
                elif tools == "sh1 encryption":  # shi加密
                    Code.sh1(e.enterbox(msg="original:"))
                elif tools == "The family of the Base":  # Base
                    base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                       choices=("base64", "base32", "base16"))
                    if base == "base64":  # base64编,解码
                        Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base64 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base64 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base32":  # base32编，解码
                        Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base32 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base32 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base16":  # base16编，解码
                        Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base16 == "encode":  # base16编码
                            Code.strToB16(e.enterbox(msg=""))
                        elif Base16 == "decode":  # base16解码
                            Code.b16ToStr(e.enterbox(msg=""))
                elif tools == "conversion of number systems":  # 进制转换
                    systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                          choices=("二进制转化为十进制", "八进制转化为十进制",
                                                   "十六进制转化为十进制", "十进制转化为二进制",
                                                   "十进制转化为八进制", "十进制转化为十六进制"))
                    if systems == "二进制转化为十进制":
                        Code.binToDec(e.enterbox(msg="输入整数"))
                    elif systems == "八进制转化为十进制":
                        Code.octToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十六进制转化为十进制":
                        Code.hexToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为二进制":
                        Code.decToBin(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为八进制":
                        Code.decToOct(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为十六进制":
                        Code.decToHex(e.enterbox(msg="输入整数"))
                elif tools == "url":  # url
                    url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("encode", "decode"))
                    if url == "encode":  # url解码
                        Code.url_encode(e.enterbox(msg=""))
                    elif url == "decode":  # url编码
                        Code.url_decode(e.enterbox(msg=""))
                elif tools == "ASCII":  # ASCII
                    ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                        choices=("encode", "decode"))
                    if ASCII == "encode":  # ASCII解码
                        Code.lettToASCII(e.enterbox(msg=""))
                    elif ASCII == "decode":  # ASCII编码
                        Code.asciiToLett(e.enterbox(msg=""))
            elif b == "个人中心":  # 个人中心
                e.msgbox(self.n5, title="'CTF' systems", ok_button="OK")
            elif b == "返回登录界面":  # 返回登录界面
                Quit1 = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit1 == "yes":
                    return
                elif Quit1 == "no":
                    continue
            elif b == "退出":  # 退出
                Quit = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit == "yes":
                    sys.exit()
                elif Quit == "no":
                    continue
    def card6(self):  # 用户信息
        e.msgbox("登陆成功", title="'CTF' systems", ok_button="OK")
        while True:  # 服务
            b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                            choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
            if b == "成员":  # 成员信息
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "积分":  # 积分
                e.msgbox(Name.card6_Integral, title="'CTF' systems")
            elif b == "版本信息":  # 版本信息
                e.msgbox(Code.vi, title="'CTF' systems")
            elif b == "解码,编码工具":  # 解码编码工具
                tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                             "conversion of number systems", "ASCII"))
                if tools == "MD5 encryption":  # MD5加密
                    Code.md5(e.enterbox(msg="original:"))
                elif tools == "sh1 encryption":  # shi加密
                    Code.sh1(e.enterbox(msg="original:"))
                elif tools == "The family of the Base":  # Base
                    base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                       choices=("base64", "base32", "base16"))
                    if base == "base64":  # base64编,解码
                        Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base64 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base64 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base32":  # base32编，解码
                        Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base32 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base32 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base16":  # base16编，解码
                        Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base16 == "encode":  # base16编码
                            Code.strToB16(e.enterbox(msg=""))
                        elif Base16 == "decode":  # base16解码
                            Code.b16ToStr(e.enterbox(msg=""))
                elif tools == "conversion of number systems":  # 进制转换
                    systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                          choices=("二进制转化为十进制", "八进制转化为十进制",
                                                   "十六进制转化为十进制", "十进制转化为二进制",
                                                   "十进制转化为八进制", "十进制转化为十六进制"))
                    if systems == "二进制转化为十进制":
                        Code.binToDec(e.enterbox(msg="输入整数"))
                    elif systems == "八进制转化为十进制":
                        Code.octToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十六进制转化为十进制":
                        Code.hexToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为二进制":
                        Code.decToBin(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为八进制":
                        Code.decToOct(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为十六进制":
                        Code.decToHex(e.enterbox(msg="输入整数"))
                elif tools == "url":  # url
                    url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("encode", "decode"))
                    if url == "encode":  # url解码
                        Code.url_encode(e.enterbox(msg=""))
                    elif url == "decode":  # url编码
                        Code.url_decode(e.enterbox(msg=""))
                elif tools == "ASCII":  # ASCII
                    ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                        choices=("encode", "decode"))
                    if ASCII == "encode":  # ASCII解码
                        Code.lettToASCII(e.enterbox(msg=""))
                    elif ASCII == "decode":  # ASCII编码
                        Code.asciiToLett(e.enterbox(msg=""))
            elif b == "个人中心":  # 个人中心
                e.msgbox(self.n6, title="'CTF' systems", ok_button="OK")
            elif b == "返回登录界面":  # 返回登录界面
                Quit1 = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit1 == "yes":
                    return
                elif Quit1 == "no":
                    continue
            elif b == "退出":  # 退出
                Quit = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit == "yes":
                    sys.exit()
                elif Quit == "no":
                    continue
    def card7(self):  # 用户信息
        e.msgbox("登陆成功", title="'CTF' systems", ok_button="OK")
        while True:  # 服务
            b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                            choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
            if b == "成员":  # 成员信息
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "积分":  # 积分
                e.msgbox(Name.card7_Integral, title="'CTF' systems")
            elif b == "版本信息":  # 版本信息
                e.msgbox(Code.vi, title="'CTF' systems")
            elif b == "解码,编码工具":  # 解码编码工具
                tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                             "conversion of number systems", "ASCII"))
                if tools == "MD5 encryption":  # MD5加密
                    Code.md5(e.enterbox(msg="original:"))
                elif tools == "sh1 encryption":  # shi加密
                    Code.sh1(e.enterbox(msg="original:"))
                elif tools == "The family of the Base":  # Base
                    base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                       choices=("base64", "base32", "base16"))
                    if base == "base64":  # base64编,解码
                        Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base64 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base64 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base32":  # base32编，解码
                        Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base32 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base32 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base16":  # base16编，解码
                        Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base16 == "encode":  # base16编码
                            Code.strToB16(e.enterbox(msg=""))
                        elif Base16 == "decode":  # base16解码
                            Code.b16ToStr(e.enterbox(msg=""))
                elif tools == "conversion of number systems":  # 进制转换
                    systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                          choices=("二进制转化为十进制", "八进制转化为十进制",
                                                   "十六进制转化为十进制", "十进制转化为二进制",
                                                   "十进制转化为八进制", "十进制转化为十六进制"))
                    if systems == "二进制转化为十进制":
                        Code.binToDec(e.enterbox(msg="输入整数"))
                    elif systems == "八进制转化为十进制":
                        Code.octToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十六进制转化为十进制":
                        Code.hexToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为二进制":
                        Code.decToBin(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为八进制":
                        Code.decToOct(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为十六进制":
                        Code.decToHex(e.enterbox(msg="输入整数"))
                elif tools == "url":  # url
                    url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("encode", "decode"))
                    if url == "encode":  # url解码
                        Code.url_encode(e.enterbox(msg=""))
                    elif url == "decode":  # url编码
                        Code.url_decode(e.enterbox(msg=""))
                elif tools == "ASCII":  # ASCII
                    ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                        choices=("encode", "decode"))
                    if ASCII == "encode":  # ASCII解码
                        Code.lettToASCII(e.enterbox(msg=""))
                    elif ASCII == "decode":  # ASCII编码
                        Code.asciiToLett(e.enterbox(msg=""))
            elif b == "个人中心":  # 个人中心
                e.msgbox(self.n7, title="'CTF' systems", ok_button="OK")
            elif b == "返回登录界面":  # 返回登录界面
                Quit1 = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit1 == "yes":
                    return
                elif Quit1 == "no":
                    continue
            elif b == "退出":  # 退出
                Quit = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit == "yes":
                    sys.exit()
                elif Quit == "no":
                    continue
    def card(self):  # 用户信息
        e.msgbox("登陆成功", title="'CTF' systems", ok_button="OK")
        while True:  # 服务
            b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                            choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
            if b == "成员":  # 成员信息
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "积分":  # 积分
                e.msgbox(Name.card_Integral, title="'CTF' systems")
            elif b == "版本信息":  # 版本信息
                e.msgbox(Code.vi, title="'CTF' systems")
            elif b == "解码,编码工具":  # 解码编码工具
                tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                             "conversion of number systems", "ASCII"))
                if tools == "MD5 encryption":  # MD5加密
                    Code.md5(e.enterbox(msg="original:"))
                elif tools == "sh1 encryption":  # shi加密
                    Code.sh1(e.enterbox(msg="original:"))
                elif tools == "The family of the Base":  # Base
                    base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                       choices=("base64", "base32", "base16"))
                    if base == "base64":  # base64编,解码
                        Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base64 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base64 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base32":  # base32编，解码
                        Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base32 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base32 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base16":  # base16编，解码
                        Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base16 == "encode":  # base16编码
                            Code.strToB16(e.enterbox(msg=""))
                        elif Base16 == "decode":  # base16解码
                            Code.b16ToStr(e.enterbox(msg=""))
                elif tools == "conversion of number systems":  # 进制转换
                    systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                          choices=("二进制转化为十进制", "八进制转化为十进制",
                                                   "十六进制转化为十进制", "十进制转化为二进制",
                                                   "十进制转化为八进制", "十进制转化为十六进制"))
                    if systems == "二进制转化为十进制":
                        Code.binToDec(e.enterbox(msg="输入整数"))
                    elif systems == "八进制转化为十进制":
                        Code.octToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十六进制转化为十进制":
                        Code.hexToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为二进制":
                        Code.decToBin(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为八进制":
                        Code.decToOct(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为十六进制":
                        Code.decToHex(e.enterbox(msg="输入整数"))
                elif tools == "url":  # url
                    url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("encode", "decode"))
                    if url == "encode":  # url解码
                        Code.url_encode(e.enterbox(msg=""))
                    elif url == "decode":  # url编码
                        Code.url_decode(e.enterbox(msg=""))
                elif tools == "ASCII":  # ASCII
                    ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                        choices=("encode", "decode"))
                    if ASCII == "encode":  # ASCII解码
                        Code.lettToASCII(e.enterbox(msg=""))
                    elif ASCII == "decode":  # ASCII编码
                        Code.asciiToLett(e.enterbox(msg=""))
            elif b == "个人中心":  # 个人中心
                e.msgbox(self.n, title="'CTF' systems", ok_button="OK")
            elif b == "返回登录界面":  # 返回登录界面
                Quit1 = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit1 == "yes":
                    return
                elif Quit1 == "no":
                    continue
            elif b == "退出":  # 退出
                Quit = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit == "yes":
                    sys.exit()
                elif Quit == "no":
                    continue
    def card_new(self):
        e.msgbox("登陆成功", title="'CTF' systems", ok_button="OK")
        while True:  # 服务
            b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                            choices=("成员信息", "积分", "版本信息", "个人中心", "解码,编码工具", "返回登录界面", "退出"))
            if b == "成员信息":  # 成员信息
                if Code.new_member == 0:
                    e.msgbox("你没有创建一个团队", title="'CTF' systems")  # buttonbox
                    new_member = e.buttonbox("是否要创建吗?", title="'CTF' systems", choices=("yes", "no"))
                    if new_member == "yes":
                        Code.new_Member = [Name.new_name]
                        Code.new_member = 1
                    elif new_member == "no":
                        continue
                elif Code.new_member == 1:
                    e.msgbox(Code.new_Member, title="'CTF' systems")  # buttonbox

            elif b == "积分":  # 积分
                e.msgbox(Name.new_Integral, title="'CTF' systems")
            elif b == "版本信息":  # 版本信息
                e.msgbox(Code.vi, title="'CTF' systems")
            elif b == "解码,编码工具":  # 解码编码工具
                tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                             "conversion of number systems", "ASCII"))
                if tools == "MD5 encryption":  # MD5加密
                    Code.md5(e.enterbox(msg="original:"))
                elif tools == "sh1 encryption":  # shi加密
                    Code.sh1(e.enterbox(msg="original:"))
                elif tools == "The family of the Base":  # Base
                    base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                       choices=("base64", "base32", "base16"))
                    if base == "base64":  # base64编,解码
                        Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base64 == "encode":  # base64编码
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base64 == "decode":  # base64解码
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base32":  # base32编，解码
                        Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base32 == "encode":  # base64编码
                            Code.strToB32(e.enterbox(msg=""))
                        elif Base32 == "decode":  # base64解码
                            Code.b32ToStr(e.enterbox(msg=""))
                    elif base == "base16":  # base16编，解码
                        Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base16 == "encode":  # base16编码
                            Code.strToB16(e.enterbox(msg=""))
                        elif Base16 == "decode":  # base16解码
                            Code.b16ToStr(e.enterbox(msg=""))
                elif tools == "url":  # url
                    url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("encode", "decode"))
                    if url == "encode":  # url编,解码
                        Code.url_encode(e.enterbox(msg=""))
                    elif url == "decode":  # url编，解码
                        Code.url_decode(e.enterbox(msg=""))

                elif tools == "conversion of number systems":  # 进制转换
                    systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                          choices=("二进制转化为十进制", "八进制转化为十进制",
                                                   "十六进制转化为十进制", "十进制转化为二进制",
                                                   "十进制转化为八进制", "十进制转化为十六进制"))
                    if systems == "二进制转化为十进制":
                        Code.binToDec(e.enterbox(msg="输入整数"))
                    elif systems == "八进制转化为十进制":
                        Code.octToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十六进制转化为十进制":
                        Code.hexToDec(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为二进制":
                        Code.decToBin(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为八进制":
                        Code.decToOct(e.enterbox(msg="输入整数"))
                    elif systems == "十进制转化为十六进制":
                        Code.decToHex(e.enterbox(msg="输入整数"))
                elif tools == "ASCII":  # ASCII
                    ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                        choices=("encode", "decode"))
                    if ASCII == "encode":  # ASCII解码
                        Code.lettToASCII(e.enterbox(msg=""))
                    elif ASCII == "decode":  # ASCII编码
                        Code.asciiToLett(e.enterbox(msg=""))
            elif b == "个人中心":  # 个人中心
                e.msgbox(self.n_new, title="'CTF' systems", ok_button="OK")
            elif b == "返回登录界面":  # 返回登录界面
                Quit1 = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit1 == "yes":
                    return
                elif Quit1 == "no":
                    continue
            elif b == "退出":  # 退出
                Quit = e.buttonbox("你确定要这么做吗?", title="'CTF' systems", choices=("yes", "no"))
                if Quit == "yes":
                    sys.exit()
                elif Quit == "no":
                    continue
Card = CARD()
name_go = True
try:
    while True:
        try:
            if name_go:
                Code.b = int(input("~~~~~~~~~~欢迎来到CTF系统~~~~~~~~~~\n最后更新:\t2022.8.13\t开发人员:\tPECompact\n输入密码\n(只可输入三次)\t"))
        except ValueError:
            print("输入有误，不能为非数字")
        if name_go:
            while Code.b != Code.a:#【第一层密码】验证失败
                try:
                    if Code.con==False:
                        print("密码输入错误")
                    if name_go:
                        Code.b = int(input("~~~~~~~ 输入密码 ~~~~~~~\n(只可输入三次)\t"))
                        Code.con = False
                except ValueError:
                    print("输入有误，不能为非数字")
                Code.i = Code.i+1
                if Code.i == 2 and Code.b != Code.a:#【第一层密码】验证失败次数超过三次
                    if Code.con==False:
                        print("密码输入错误")
                    #init(autoreset=False)
                    Code.q = 30  #锁屏时间
                    Code.f = Code.f+1
                    if name_go:
                        name_go = False
                        print("出错3次以上，在30秒后可重新输入!")
                        Code.i = -1
                        for p in range(30):
                            t.sleep(1)
                            print("~~~~~~ 锁屏中 ~~~~~~(",Code.q,")")
                            Code.q = Code.q-1
                        Code.con = True
                        name_go = True

                if Code.f >= 3:#【锁屏】次数超过三次
                    Code.f = 0
                    Code.gly()
                    Code.con = True
            else:#【第一层密码】验证成功
                print("密码正确,加载中")
                while True:
                    w = e.buttonbox("登录成功(初始密码:0000)", title="'CTF' systems",choices=("ok", "新用户?创建一个!", "quit"))
                    if w == "quit":
                        sys.exit()
                    if w == "新用户?创建一个!":
                        Name.new_name = e.enterbox(msg="新的ID", title="'Hack' systems")
                        Name.new_psd = e.enterbox(msg="新的密码", title="'Hack' systems")
                        #new_name = e.enterbox(msg="你的昵称", title="'Hack' systems")
                        #new = [new_id, new_psd]
                        #card_new()
                    if w == "ok":
                        #e.msgbox("land successfully(initial password:0000)",title = "'CTF' systems",ok_button = "yes")
                        c = e.multpasswordbox("您的帐号···",title = "'Hack' systems",fields = ("ID","PASSWORD"))
                        #money = card1_mony
                        if c == [Name.card1_name,Name.card1_psd]:  # 密码正确
                            Card.card1()#执行函数
                        elif c == [Name.card2_name, Name.card2_psd]:  # 密码正确
                            Card.card2()#执行函数
                        elif c == [Name.card3_name, Name.card3_psd]:  # 密码正确
                            Card.card3()#执行函数
                        elif c == [Name.card4_name, Name.card4_psd]:  # 密码正确
                            Card.card4()#执行函数
                        elif c == [Name.card5_name, Name.card5_psd]:  # 密码正确
                            Card.card5()#执行函数
                        elif c == [Name.card6_name, Name.card6_psd]:  # 密码正确
                            Card.card6()#执行函数
                        elif c == [Name.card7_name, Name.card7_psd]:  # 密码正确
                            Card.card7()#执行函数
                        elif c == [Name.card_name, Name.card_psd]:  # 密码正确
                            Card.card()#执行函数
                        elif c == [Name.new_name,Name.new_psd]:  # 密码正确
                            if Code.new_member==0:
                                e.msgbox("你没有创建一个团队", title="'CTF' systems")  # buttonbox
                                new_member = e.buttonbox("是否创建?", title="'CTF' systems", choices=("yes", "no"))
                                if new_member == "yes":
                                    Code.new_Member = [Name.new_name]
                                    Code.member = 1
                                    Card.card_new()
                                elif new_member == "no":
                                    #Code.member = 0
                                    Card.card_new()
                            elif Code.new_member==1:
                                Card.card_new()
                            #Card.card_new()
                        elif c!=[Name.card1_name, Name.card1_psd] or [Name.card2_name, Name.card2_psd] or [Name.card3_name, Name.card3_psd] or [Name.card4_name, Name.card4_psd] or [Name.card5_name, Name.card5_psd] or [Name.card6_name, Name.card6_psd] or [Name.card7_name, Name.card7_psd] or [Name.card_name, Name.card_psd] or [Name.new_name,Name.new_psd]:
                            e.msgbox("输入错误或没有帐户", title="'CTF' systems", ok_button="OK")
                            #sys.exit()
                            Code.l = Code.l+1
                            if Code.l>=5:
                                e.msgbox("程序可能出现未知错误无法成功登录，可以联系开发者或重试!  \nQQ\t3139373615\n邮箱\t3139373615@qq.com\n电话号码\t13199827726", title="'CTF' systems", ok_button="OK")
                            continue

except BaseException as e:
    print("\n_已被关闭或出现异常_")
    print("程序可能已被关闭或出现未知错误无法成功运行，可以联系开发者或重试!  \nQQ\t3139373615\n邮箱\t3139373615@qq.com\n电话号码\t13199827726")
    print("报错代码：",repr(e))
    time.sleep(5)