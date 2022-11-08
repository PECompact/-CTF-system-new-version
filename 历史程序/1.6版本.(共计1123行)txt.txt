import sys
import time as t
import easygui as e
import hashlib
import base64
from urllib.parse import quote, unquote
l = 0
i = 0
f = 0
b = 0
q = 30
a = 3369
psd2 = 123456789
psd3 = 0
new_member = 0
vi = "1.0:更新登录系统（简易）\n1.2：更新可多人员登录\n1.2.1：修复无法正常登陆的bug\n1.4：更新了登陆菜单\n1.5：修改至全英文\n1.6：优化了登录界面\n1.7：更新了智能检测未知错误功能\n1.8：加强了密码登陆的准确性\n1.9：修复了管理员验证后无法正常退出循环的bug\n2.0：增加了查看以往版本更新信息功能\n2.1：修复了失败验证管理员密码后再次验证成功无法正常退出的bug\n2.2：修复了第三次验证第一层密码成功时无法正常进入系统的bug\n2.3：更新了返回登录界面的功能\n2.4：修复了输入非整数时报错的bug\n2.5：新增'工具'服务"


card_name = "Sure"
card_psd = "0000"
card_Integral = "unknown"

card1_name = "PECompact"
card1_psd = "qazwsx"
card1_Integral = 90

card2_name = "Zero two"
card2_psd = "0000"
card2_Integral = "unknown"

card3_name = "薛梓文"
card3_psd = "0000"
card3_Integral = "unknown"

card4_name = "李昊霖"
card4_psd = "0000"
card4_Integral = "unknown"

card5_name = "李卓阳"
card5_psd = "0000"
card5_Integral = "unknown"

card6_name = "汪恩皓宇"
card6_psd = "0000"
card6_Integral = "unknown"

card7_name = "张光泽"
card7_psd = "0000"
card7_Integral = "unknown"

new_id = "q"
new_psd = "q"
new_Integral = "unknown"

name = {'name1(developer)':card1_name,'name2':card2_name,'name3':card3_name,'name4':card4_name,'name5':card5_name,'name6':card6_name,'name7':card7_name,'teacher':card_name}
#name1 = {'teacher':card_name}
#name_end = name and name1
#Member = [card1_name,card2_name]
'''
def shuru():
    isinstance(b, str)'''


# 进行MD5加密
def md5(s):
    #new_id = e.enterbox(msg="new_ID", title="'Hack' systems")
    original = s
    md = hashlib.md5()
    s = s.encode(encoding='utf-8')
    md.update(s)
    e.msgbox('Original:' + original, title="'CTF' systems")
    e.msgbox('Md5 Encryption:' + md.hexdigest(), title="'CTF' systems")


# 进行sh1加密
def sh1(s):
    original = s
    sh = hashlib.sha1()
    s = s.encode(encoding='utf-8')
    e.msgbox('Original:' + original, title="'CTF' systems")
    e.msgbox('SH1 Encryption:' + sh.hexdigest(), title="'CTF' systems")

# 将字符串转换为base64编码格式
def strToB64(s):
    encode = base64.b64encode(s.encode("utf-8"))
    e.msgbox('Original:' + s, title="'CTF' systems")
    e.msgbox('Base64 encode:' + str(encode), title="'CTF' systems")

# 将base64编码格式转化为正常的字符类型
def b64ToStr(s):
    decode = base64.b64decode(str(s))
    e.msgbox('Base64:' + s, title="'CTF' systems")
    e.msgbox('Base64 decode:' + str(decode), title="'CTF' systems")

# 将字符串转为b32编码格式
def strToB32(s):
    encode = base64.b32encode(s.encode("utf-8"))
    e.msgbox('Original:' + s, title="'CTF' systems")
    e.msgbox('Base32 encode:' + str(encode), title="'CTF' systems")

# 将base32编码格式转化为正常的字符类型
def b32ToStr(s):
    decode = base64.b32decode(str(s))
    e.msgbox('Base32:' + s, title="'CTF' systems")
    e.msgbox('Base32 decode:' + str(decode), title="'CTF' systems")

# 将字符串转为base16编码格式
def strToB16(s):
    encode = base64.b16encode(s.encode("utf-8"))
    e.msgbox('Original:' + s, title="'CTF' systems")
    e.msgbox('Base16 encode:' + str(encode), title="'CTF' systems")

# 将base16编码格式转化为正常的字符类型
def b16ToStr(s):
    decode = base64.b16decode(str(s))
    e.msgbox('Base16:' + s, title="'CTF' systems")
    e.msgbox('Base16 decode:' + str(decode), title="'CTF' systems")

# 将二进制转化为十进制
def binToDec(s):
    result = int(s, 2)
    e.msgbox('Binary :' + str(s), title="'CTF' systems")
    e.msgbox('Decimal :' + str(result), title="'CTF' systems")

# 将八进制转化为十进制
def octToDec(s):
    result = int(s, 8)
    e.msgbox('Octal :' + str(s) + s, title="'CTF' systems")
    e.msgbox('Decimal :' + str(result), title="'CTF' systems")

# 将十六进制转化为十进制
def hexToDec(s):
    result = int(s, 16)
    e.msgbox('Hex :' + str(s) + s, title="'CTF' systems")
    e.msgbox('Decimal :' + str(result), title="'CTF' systems")

# 将十进制转化为二进制
def decToBin(s):
    s = int(s)
    result = bin(s)
    e.msgbox('Decimal:' + str(s), title="'CTF' systems")
    e.msgbox('Binary:' + str(result), title="'CTF' systems")

# 将十进制转化为八进制
def decToOct(s):
    s = int(s)
    result = oct(s)
    e.msgbox('Decimal :' + str(s), title="'CTF' systems")
    e.msgbox('Octal :' + str(result), title="'CTF' systems")

# 将十进制转化为十六进制
def decToHex(s):
    s = int(s)
    result = hex(s)
    e.msgbox('Decimal :' + str(s), title="'CTF' systems")
    e.msgbox('Hex :' + str(result), title="'CTF' systems")

# 进行url编码
def url_encode(s):
    encode = quote(s)
    e.msgbox('Original:' + s, title="'CTF' systems")
    e.msgbox('URL encode:' + encode, title="'CTF' systems")

# 进行url编码
def url_decode(s):
    decode = unquote(s)
    e.msgbox('URL encode:' + s, title="'CTF' systems")
    e.msgbox('URL decode:' + decode, title="'CTF' systems")

# 将字母转化为对应的ASCII
def lettToASCII(s):
    e.msgbox('Letters:' + s, title="'CTF' systems")
    result = ''
    for i in s:
        result = result + str(ord(i)) + ' '
    e.msgbox('ASCII  :' + result, title="'CTF' systems")

# 将ASCII转化为对应的字母以及字符
def asciiToLett(s):
    list = s.split(' ')
    result = ''
    e.msgbox('ASCII    :' + s, title="'CTF' systems")
    for i in list:
        i = int(i)
        result = result + chr(i)
    e.msgbox('Letters  :' + result, title="'CTF' systems")

def gly():#跳出多次循环(管理员验证)
    global psd3,psd2
    while True:
        try:
            print("··········锁定屏幕超过3次，请联系管理员··········")
            psd3 = int(input("请输入管理员密码\t"))
        except ValueError:
            print("输入有误，不能为非数字")
        except BaseException as e:
            print("出现异常")
            print(repr(e))
        if psd3 == psd2:  # 管理员密码
            return
        '''
        else:
            continue'''
def card1():#用户信息
    global card1_name,card1_Integral,card1_psd,name,vi
    n = {"你的名字:": card1_name, "你的密码:": card1_psd}
    Integral = card1_Integral  # 积分
    e.msgbox("登陆成功", title="'CTF' systems", ok_button="OK")
    while True:  # 服务
        b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                        choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
        if b == "成员":  # 成员信息
            e.msgbox(name, title="'CTF' systems")  # buttonbox
        elif b == "积分":  # 积分
            e.msgbox(Integral, title="'CTF' systems")
        elif b == "版本信息":  # 版本信息
            e.msgbox(vi, title="'CTF' systems")
        elif b == "解码,编码工具":  # 解码编码工具
            tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url", "conversion of number systems", "ASCII"))
            if tools == "MD5 encryption":  #MD5加密
                md5(e.enterbox(msg="original:"))
            elif tools == "sh1 encryption":  #shi加密
                sh1(e.enterbox(msg="original:"))
            elif tools == "The family of the Base":  #Base
                base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                   choices=("base64", "base32", "base16"))
                if base == "base64":  #base64编,解码
                    Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base64 == "encode":  #base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base64 == "decode":  #base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base32":  #base32编，解码
                    Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base32 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base32 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base16":  # base16编，解码
                    Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base16 == "encode":  # base16编码
                        strToB16(e.enterbox(msg=""))
                    elif Base16 == "decode":  # base16解码
                        b16ToStr(e.enterbox(msg=""))
            elif tools == "conversion of number systems":  #进制转换
                systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("二进制转化为十进制", "八进制转化为十进制",
                                                "十六进制转化为十进制","十进制转化为二进制",
                                                "十进制转化为八进制","十进制转化为十六进制"))
                if systems == "二进制转化为十进制":
                    binToDec(e.enterbox(msg="输入整数"))
                elif systems == "八进制转化为十进制":
                    octToDec(e.enterbox(msg="输入整数"))
                elif systems == "十六进制转化为十进制":
                    hexToDec(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为二进制":
                    decToBin(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为八进制":
                    decToOct(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为十六进制":
                    decToHex(e.enterbox(msg="输入整数"))
            elif tools == "url":  # url
                url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                   choices=("encode", "decode"))
                if url == "encode":  # url解码
                    url_encode(e.enterbox(msg=""))
                elif url == "decode":  # url编码
                    url_decode(e.enterbox(msg=""))
            elif tools == "ASCII":  # ASCII
                ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                   choices=("encode", "decode"))
                if ASCII == "encode":  # ASCII解码
                    lettToASCII(e.enterbox(msg=""))
                elif ASCII == "decode":  # ASCII编码
                    asciiToLett(e.enterbox(msg=""))
        elif b == "个人中心":  # 个人中心
            e.msgbox(n, title="'CTF' systems", ok_button="OK")
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
def card2():#用户信息
    global card2_name, card2_Integral, name, vi
    n = {"Your name:":card2_name,"Your password:":card2_psd}
    Integral = card2_Integral  # 积分
    e.msgbox("land successfully", title="'CTF' systems", ok_button="OK")
    while True:  # 服务
        b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                        choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
        if b == "成员":  # 成员信息
            e.msgbox(name, title="'CTF' systems")  # buttonbox
        elif b == "积分":  # 积分
            e.msgbox(Integral, title="'CTF' systems")
        elif b == "版本信息":  # 版本信息
            e.msgbox(vi, title="'CTF' systems")
        elif b == "解码,编码工具":  # 解码编码工具
            tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                         "conversion of number systems", "ASCII"))
            if tools == "MD5 encryption":  # MD5加密
                md5(e.enterbox(msg="original:"))
            elif tools == "sh1 encryption":  # shi加密
                sh1(e.enterbox(msg="original:"))
            elif tools == "The family of the Base":  # Base
                base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                   choices=("base64", "base32", "base16"))
                if base == "base64":  # base64编,解码
                    Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base64 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base64 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base32":  # base32编，解码
                    Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base32 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base32 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base16":  # base16编，解码
                    Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base16 == "encode":  # base16编码
                        strToB16(e.enterbox(msg=""))
                    elif Base16 == "decode":  # base16解码
                        b16ToStr(e.enterbox(msg=""))
            elif tools == "conversion of number systems":  # 进制转换
                systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("二进制转化为十进制", "八进制转化为十进制",
                                               "十六进制转化为十进制", "十进制转化为二进制",
                                               "十进制转化为八进制", "十进制转化为十六进制"))
                if systems == "二进制转化为十进制":
                    binToDec(e.enterbox(msg="输入整数"))
                elif systems == "八进制转化为十进制":
                    octToDec(e.enterbox(msg="输入整数"))
                elif systems == "十六进制转化为十进制":
                    hexToDec(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为二进制":
                    decToBin(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为八进制":
                    decToOct(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为十六进制":
                    decToHex(e.enterbox(msg="输入整数"))
            elif tools == "url":  # url
                url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                  choices=("encode", "decode"))
                if url == "encode":  # url解码
                    url_encode(e.enterbox(msg=""))
                elif url == "decode":  # url编码
                    url_decode(e.enterbox(msg=""))
            elif tools == "ASCII":  # ASCII
                ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("encode", "decode"))
                if ASCII == "encode":  # ASCII解码
                    lettToASCII(e.enterbox(msg=""))
                elif ASCII == "decode":  # ASCII编码
                    asciiToLett(e.enterbox(msg=""))
        elif b == "个人中心":  # 个人中心
            e.msgbox(n, title="'CTF' systems", ok_button="OK")
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
def card3():#用户信息
    global card3_name, card3_Integral, name, vi
    n = {"Your name:":card3_name,"Your password:":card3_psd}
    Integral = card3_Integral  # 积分
    e.msgbox("land successfully", title="'CTF' systems", ok_button="OK")
    while True:  # 服务
        b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                        choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
        if b == "成员":  # 成员信息
            e.msgbox(name, title="'CTF' systems")  # buttonbox
        elif b == "积分":  # 积分
            e.msgbox(Integral, title="'CTF' systems")
        elif b == "版本信息":  # 版本信息
            e.msgbox(vi, title="'CTF' systems")
        elif b == "解码,编码工具":  # 解码编码工具
            tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                         "conversion of number systems", "ASCII"))
            if tools == "MD5 encryption":  # MD5加密
                md5(e.enterbox(msg="original:"))
            elif tools == "sh1 encryption":  # shi加密
                sh1(e.enterbox(msg="original:"))
            elif tools == "The family of the Base":  # Base
                base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                   choices=("base64", "base32", "base16"))
                if base == "base64":  # base64编,解码
                    Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base64 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base64 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base32":  # base32编，解码
                    Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base32 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base32 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base16":  # base16编，解码
                    Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base16 == "encode":  # base16编码
                        strToB16(e.enterbox(msg=""))
                    elif Base16 == "decode":  # base16解码
                        b16ToStr(e.enterbox(msg=""))
            elif tools == "conversion of number systems":  # 进制转换
                systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("二进制转化为十进制", "八进制转化为十进制",
                                               "十六进制转化为十进制", "十进制转化为二进制",
                                               "十进制转化为八进制", "十进制转化为十六进制"))
                if systems == "二进制转化为十进制":
                    binToDec(e.enterbox(msg="输入整数"))
                elif systems == "八进制转化为十进制":
                    octToDec(e.enterbox(msg="输入整数"))
                elif systems == "十六进制转化为十进制":
                    hexToDec(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为二进制":
                    decToBin(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为八进制":
                    decToOct(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为十六进制":
                    decToHex(e.enterbox(msg="输入整数"))
            elif tools == "url":  # url
                url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                  choices=("encode", "decode"))
                if url == "encode":  # url解码
                    url_encode(e.enterbox(msg=""))
                elif url == "decode":  # url编码
                    url_decode(e.enterbox(msg=""))
            elif tools == "ASCII":  # ASCII
                ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("encode", "decode"))
                if ASCII == "encode":  # ASCII解码
                    lettToASCII(e.enterbox(msg=""))
                elif ASCII == "decode":  # ASCII编码
                    asciiToLett(e.enterbox(msg=""))
        elif b == "个人中心":  # 个人中心
            e.msgbox(n, title="'CTF' systems", ok_button="OK")
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
def card4():#用户信息
    global card4_name, card4_Integral, name, vi
    n = {"Your name:":card4_name,"Your password:":card4_psd}
    Integral = card4_Integral  # 积分
    e.msgbox("land successfully", title="'CTF' systems", ok_button="OK")
    while True:  # 服务
        b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                        choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
        if b == "成员":  # 成员信息
            e.msgbox(name, title="'CTF' systems")  # buttonbox
        elif b == "积分":  # 积分
            e.msgbox(Integral, title="'CTF' systems")
        elif b == "版本信息":  # 版本信息
            e.msgbox(vi, title="'CTF' systems")
        elif b == "解码,编码工具":  # 解码编码工具
            tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                         "conversion of number systems", "ASCII"))
            if tools == "MD5 encryption":  # MD5加密
                md5(e.enterbox(msg="original:"))
            elif tools == "sh1 encryption":  # shi加密
                sh1(e.enterbox(msg="original:"))
            elif tools == "The family of the Base":  # Base
                base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                   choices=("base64", "base32", "base16"))
                if base == "base64":  # base64编,解码
                    Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base64 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base64 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base32":  # base32编，解码
                    Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base32 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base32 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base16":  # base16编，解码
                    Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base16 == "encode":  # base16编码
                        strToB16(e.enterbox(msg=""))
                    elif Base16 == "decode":  # base16解码
                        b16ToStr(e.enterbox(msg=""))
            elif tools == "conversion of number systems":  # 进制转换
                systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("二进制转化为十进制", "八进制转化为十进制",
                                               "十六进制转化为十进制", "十进制转化为二进制",
                                               "十进制转化为八进制", "十进制转化为十六进制"))
                if systems == "二进制转化为十进制":
                    binToDec(e.enterbox(msg="输入整数"))
                elif systems == "八进制转化为十进制":
                    octToDec(e.enterbox(msg="输入整数"))
                elif systems == "十六进制转化为十进制":
                    hexToDec(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为二进制":
                    decToBin(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为八进制":
                    decToOct(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为十六进制":
                    decToHex(e.enterbox(msg="输入整数"))
            elif tools == "url":  # url
                url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                  choices=("encode", "decode"))
                if url == "encode":  # url解码
                    url_encode(e.enterbox(msg=""))
                elif url == "decode":  # url编码
                    url_decode(e.enterbox(msg=""))
            elif tools == "ASCII":  # ASCII
                ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("encode", "decode"))
                if ASCII == "encode":  # ASCII解码
                    lettToASCII(e.enterbox(msg=""))
                elif ASCII == "decode":  # ASCII编码
                    asciiToLett(e.enterbox(msg=""))
        elif b == "个人中心":  # 个人中心
            e.msgbox(n, title="'CTF' systems", ok_button="OK")
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
def card5():#用户信息
    global card5_name, card5_Integral, name, vi
    n = {"Your name:":card5_name,"Your password:":card5_psd}
    Integral = card5_Integral  # 积分
    e.msgbox("land successfully", title="'CTF' systems", ok_button="OK")
    while True:  # 服务
        b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                        choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
        if b == "成员":  # 成员信息
            e.msgbox(name, title="'CTF' systems")  # buttonbox
        elif b == "积分":  # 积分
            e.msgbox(Integral, title="'CTF' systems")
        elif b == "版本信息":  # 版本信息
            e.msgbox(vi, title="'CTF' systems")
        elif b == "解码,编码工具":  # 解码编码工具
            tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                         "conversion of number systems", "ASCII"))
            if tools == "MD5 encryption":  # MD5加密
                md5(e.enterbox(msg="original:"))
            elif tools == "sh1 encryption":  # shi加密
                sh1(e.enterbox(msg="original:"))
            elif tools == "The family of the Base":  # Base
                base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                   choices=("base64", "base32", "base16"))
                if base == "base64":  # base64编,解码
                    Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base64 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base64 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base32":  # base32编，解码
                    Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base32 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base32 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base16":  # base16编，解码
                    Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base16 == "encode":  # base16编码
                        strToB16(e.enterbox(msg=""))
                    elif Base16 == "decode":  # base16解码
                        b16ToStr(e.enterbox(msg=""))
            elif tools == "conversion of number systems":  # 进制转换
                systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("二进制转化为十进制", "八进制转化为十进制",
                                               "十六进制转化为十进制", "十进制转化为二进制",
                                               "十进制转化为八进制", "十进制转化为十六进制"))
                if systems == "二进制转化为十进制":
                    binToDec(e.enterbox(msg="输入整数"))
                elif systems == "八进制转化为十进制":
                    octToDec(e.enterbox(msg="输入整数"))
                elif systems == "十六进制转化为十进制":
                    hexToDec(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为二进制":
                    decToBin(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为八进制":
                    decToOct(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为十六进制":
                    decToHex(e.enterbox(msg="输入整数"))
            elif tools == "url":  # url
                url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                  choices=("encode", "decode"))
                if url == "encode":  # url解码
                    url_encode(e.enterbox(msg=""))
                elif url == "decode":  # url编码
                    url_decode(e.enterbox(msg=""))
            elif tools == "ASCII":  # ASCII
                ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("encode", "decode"))
                if ASCII == "encode":  # ASCII解码
                    lettToASCII(e.enterbox(msg=""))
                elif ASCII == "decode":  # ASCII编码
                    asciiToLett(e.enterbox(msg=""))
        elif b == "个人中心":  # 个人中心
            e.msgbox(n, title="'CTF' systems", ok_button="OK")
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
def card6():#用户信息
    global card6_name, card6_Integral, name, vi
    n = {"Your name:":card6_name,"Your password:":card6_psd}
    Integral = card6_Integral  # 积分
    e.msgbox("land successfully", title="'CTF' systems", ok_button="OK")
    while True:  # 服务
        b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                        choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
        if b == "成员":  # 成员信息
            e.msgbox(name, title="'CTF' systems")  # buttonbox
        elif b == "积分":  # 积分
            e.msgbox(Integral, title="'CTF' systems")
        elif b == "版本信息":  # 版本信息
            e.msgbox(vi, title="'CTF' systems")
        elif b == "解码,编码工具":  # 解码编码工具
            tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                         "conversion of number systems", "ASCII"))
            if tools == "MD5 encryption":  # MD5加密
                md5(e.enterbox(msg="original:"))
            elif tools == "sh1 encryption":  # shi加密
                sh1(e.enterbox(msg="original:"))
            elif tools == "The family of the Base":  # Base
                base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                   choices=("base64", "base32", "base16"))
                if base == "base64":  # base64编,解码
                    Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base64 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base64 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base32":  # base32编，解码
                    Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base32 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base32 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base16":  # base16编，解码
                    Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base16 == "encode":  # base16编码
                        strToB16(e.enterbox(msg=""))
                    elif Base16 == "decode":  # base16解码
                        b16ToStr(e.enterbox(msg=""))
            elif tools == "conversion of number systems":  # 进制转换
                systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("二进制转化为十进制", "八进制转化为十进制",
                                               "十六进制转化为十进制", "十进制转化为二进制",
                                               "十进制转化为八进制", "十进制转化为十六进制"))
                if systems == "二进制转化为十进制":
                    binToDec(e.enterbox(msg="输入整数"))
                elif systems == "八进制转化为十进制":
                    octToDec(e.enterbox(msg="输入整数"))
                elif systems == "十六进制转化为十进制":
                    hexToDec(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为二进制":
                    decToBin(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为八进制":
                    decToOct(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为十六进制":
                    decToHex(e.enterbox(msg="输入整数"))
            elif tools == "url":  # url
                url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                  choices=("encode", "decode"))
                if url == "encode":  # url解码
                    url_encode(e.enterbox(msg=""))
                elif url == "decode":  # url编码
                    url_decode(e.enterbox(msg=""))
            elif tools == "ASCII":  # ASCII
                ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("encode", "decode"))
                if ASCII == "encode":  # ASCII解码
                    lettToASCII(e.enterbox(msg=""))
                elif ASCII == "decode":  # ASCII编码
                    asciiToLett(e.enterbox(msg=""))
        elif b == "个人中心":  # 个人中心
            e.msgbox(n, title="'CTF' systems", ok_button="OK")
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
def card7():#用户信息
    global card7_name, card7_Integral, name, vi
    n = {"Your name:":card7_name,"Your password:":card7_psd}
    Integral = card7_Integral  # 积分
    e.msgbox("land successfully", title="'CTF' systems", ok_button="OK")
    while True:  # 服务
        b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                        choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
        if b == "成员":  # 成员信息
            e.msgbox(name, title="'CTF' systems")  # buttonbox
        elif b == "积分":  # 积分
            e.msgbox(Integral, title="'CTF' systems")
        elif b == "版本信息":  # 版本信息
            e.msgbox(vi, title="'CTF' systems")
        elif b == "解码,编码工具":  # 解码编码工具
            tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                         "conversion of number systems", "ASCII"))
            if tools == "MD5 encryption":  # MD5加密
                md5(e.enterbox(msg="original:"))
            elif tools == "sh1 encryption":  # shi加密
                sh1(e.enterbox(msg="original:"))
            elif tools == "The family of the Base":  # Base
                base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                   choices=("base64", "base32", "base16"))
                if base == "base64":  # base64编,解码
                    Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base64 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base64 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base32":  # base32编，解码
                    Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base32 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base32 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base16":  # base16编，解码
                    Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base16 == "encode":  # base16编码
                        strToB16(e.enterbox(msg=""))
                    elif Base16 == "decode":  # base16解码
                        b16ToStr(e.enterbox(msg=""))
            elif tools == "conversion of number systems":  # 进制转换
                systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("二进制转化为十进制", "八进制转化为十进制",
                                               "十六进制转化为十进制", "十进制转化为二进制",
                                               "十进制转化为八进制", "十进制转化为十六进制"))
                if systems == "二进制转化为十进制":
                    binToDec(e.enterbox(msg="输入整数"))
                elif systems == "八进制转化为十进制":
                    octToDec(e.enterbox(msg="输入整数"))
                elif systems == "十六进制转化为十进制":
                    hexToDec(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为二进制":
                    decToBin(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为八进制":
                    decToOct(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为十六进制":
                    decToHex(e.enterbox(msg="输入整数"))
            elif tools == "url":  # url
                url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                  choices=("encode", "decode"))
                if url == "encode":  # url解码
                    url_encode(e.enterbox(msg=""))
                elif url == "decode":  # url编码
                    url_decode(e.enterbox(msg=""))
            elif tools == "ASCII":  # ASCII
                ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("encode", "decode"))
                if ASCII == "encode":  # ASCII解码
                    lettToASCII(e.enterbox(msg=""))
                elif ASCII == "decode":  # ASCII编码
                    asciiToLett(e.enterbox(msg=""))
        elif b == "个人中心":  # 个人中心
            e.msgbox(n, title="'CTF' systems", ok_button="OK")
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
def card():#用户信息
    global card_name, card_Integral, name, vi
    n = {"Your name:":card_name,"Your password:":card_psd}
    Integral = card_Integral  # 积分
    e.msgbox("land successfully", title="'CTF' systems", ok_button="OK")
    while True:  # 服务
        b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                        choices=("成员", "积分", "版本信息", "解码,编码工具", "个人中心", "返回登录界面", "退出"))
        if b == "成员":  # 成员信息
            e.msgbox(name, title="'CTF' systems")  # buttonbox
        elif b == "积分":  # 积分
            e.msgbox(Integral, title="'CTF' systems")
        elif b == "版本信息":  # 版本信息
            e.msgbox(vi, title="'CTF' systems")
        elif b == "解码,编码工具":  # 解码编码工具
            tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                         "conversion of number systems", "ASCII"))
            if tools == "MD5 encryption":  # MD5加密
                md5(e.enterbox(msg="original:"))
            elif tools == "sh1 encryption":  # shi加密
                sh1(e.enterbox(msg="original:"))
            elif tools == "The family of the Base":  # Base
                base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                   choices=("base64", "base32", "base16"))
                if base == "base64":  # base64编,解码
                    Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base64 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base64 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base32":  # base32编，解码
                    Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base32 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base32 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base16":  # base16编，解码
                    Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base16 == "encode":  # base16编码
                        strToB16(e.enterbox(msg=""))
                    elif Base16 == "decode":  # base16解码
                        b16ToStr(e.enterbox(msg=""))
            elif tools == "conversion of number systems":  # 进制转换
                systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("二进制转化为十进制", "八进制转化为十进制",
                                               "十六进制转化为十进制", "十进制转化为二进制",
                                               "十进制转化为八进制", "十进制转化为十六进制"))
                if systems == "二进制转化为十进制":
                    binToDec(e.enterbox(msg="输入整数"))
                elif systems == "八进制转化为十进制":
                    octToDec(e.enterbox(msg="输入整数"))
                elif systems == "十六进制转化为十进制":
                    hexToDec(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为二进制":
                    decToBin(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为八进制":
                    decToOct(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为十六进制":
                    decToHex(e.enterbox(msg="输入整数"))
            elif tools == "url":  # url
                url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                  choices=("encode", "decode"))
                if url == "encode":  # url解码
                    url_encode(e.enterbox(msg=""))
                elif url == "decode":  # url编码
                    url_decode(e.enterbox(msg=""))
            elif tools == "ASCII":  # ASCII
                ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("encode", "decode"))
                if ASCII == "encode":  # ASCII解码
                    lettToASCII(e.enterbox(msg=""))
                elif ASCII == "decode":  # ASCII编码
                    asciiToLett(e.enterbox(msg=""))
        elif b == "个人中心":  # 个人中心
            e.msgbox(n, title="'CTF' systems", ok_button="OK")
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

def card_new():
    global new_id, new_Integral, new_psd, vi,new_Member
    n = {"你的名字:": new_id, "你的密码:": new_psd}
    Integral = new_Integral  # 积分
    e.msgbox("登陆成功", title="'CTF' systems", ok_button="OK")
    while True:  # 服务
        b = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                        choices=("成员信息", "积分", "版本信息", "个人中心", "解码,编码工具", "返回登录界面", "退出"))
        if b == "成员信息":  # 成员信息
            if Member == 0:
                e.msgbox("你没有创建一个团队", title="'CTF' systems")  # buttonbox
                new_member = e.buttonbox("是否要创建吗?", title="'CTF' systems", choices=("yes", "no"))
                if new_member == "yes":
                    new_Member = [new_id]
                elif new_member == "no":
                    continue
            elif Member==1:
                e.msgbox(new_Member, title="'CTF' systems")  # buttonbox

        elif b == "积分":  # 积分
            e.msgbox(Integral, title="'CTF' systems")
        elif b == "版本信息":  # 版本信息
            e.msgbox(vi, title="'CTF' systems")
        elif b == "解码,编码工具":  # 解码编码工具
            tools = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                         "conversion of number systems", "ASCII"))
            if tools == "MD5 encryption":  # MD5加密
                md5(e.enterbox(msg="original:"))
            elif tools == "sh1 encryption":  # shi加密
                sh1(e.enterbox(msg="original:"))
            elif tools == "The family of the Base":  # Base
                base = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                   choices=("base64", "base32", "base16"))
                if base == "base64":  # base64编,解码
                    Base64 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base64 == "encode":  # base64编码
                        strToB64(e.enterbox(msg=""))
                    elif Base64 == "decode":  # base64解码
                        b64ToStr(e.enterbox(msg=""))
                elif base == "base32":  # base32编，解码
                    Base32 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base32 == "encode":  # base64编码
                        strToB32(e.enterbox(msg=""))
                    elif Base32 == "decode":  # base64解码
                        b32ToStr(e.enterbox(msg=""))
                elif base == "base16":  # base16编，解码
                    Base16 = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                         choices=("encode", "decode"))
                    if Base16 == "encode":  # base16编码
                        strToB16(e.enterbox(msg=""))
                    elif Base16 == "decode":  # base16解码
                        b16ToStr(e.enterbox(msg=""))
            elif tools == "url":  # url
                url = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                  choices=("encode", "decode"))
                if url == "encode":  # url编,解码
                    url_encode(e.enterbox(msg=""))
                elif url == "decode":  # url编，解码
                    url_decode(e.enterbox(msg=""))

            elif tools == "conversion of number systems":  # 进制转换
                systems = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                      choices=("二进制转化为十进制", "八进制转化为十进制",
                                               "十六进制转化为十进制", "十进制转化为二进制",
                                               "十进制转化为八进制", "十进制转化为十六进制"))
                if systems == "二进制转化为十进制":
                    binToDec(e.enterbox(msg="输入整数"))
                elif systems == "八进制转化为十进制":
                    octToDec(e.enterbox(msg="输入整数"))
                elif systems == "十六进制转化为十进制":
                    hexToDec(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为二进制":
                    decToBin(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为八进制":
                    decToOct(e.enterbox(msg="输入整数"))
                elif systems == "十进制转化为十六进制":
                    decToHex(e.enterbox(msg="输入整数"))
            elif tools == "ASCII":  # ASCII
                ASCII = e.buttonbox("请选择您需要的服务", title="'CTF' systems",
                                    choices=("encode", "decode"))
                if ASCII == "encode":  # ASCII解码
                    lettToASCII(e.enterbox(msg=""))
                elif ASCII == "decode":  # ASCII编码
                    asciiToLett(e.enterbox(msg=""))
        elif b == "个人中心":  # 个人中心
            e.msgbox(n, title="'CTF' systems", ok_button="OK")
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
while True:
    #while b==a:
    try:
        b = int(input("~~~~~~~~~~欢迎来到CTF系统~~~~~~~~~~\n最后更新:\t2021.12.27\t开发人员:\tPECompact\n输入密码\n(只可输入三次)\t"))
    except ValueError:
        print("输入有误，不能为非数字")
    except BaseException as e:
        print("出现异常")
        print(repr(e))
    while b != a:#【第一层密码】验证失败
        try:
            print("密码输入错误")
            b = int(input("~~~~~~~ 输入密码 ~~~~~~~\n(只可输入三次)\t"))
        except ValueError:
            print("输入有误，不能为非数字")
        i = i+1
        if i == 2 and b != a:#【第一层密码】验证失败次数超过三次
            q = 30  #锁屏时间
            f = f+1
            print("出错3次以上，在30秒后可重新输入!")
            i = -1
            for p in range(30):
                t.sleep(1)
                print("~~~~~~ 锁屏中 ~~~~~~(",q,")")
                q = q-1

        if f >= 3:#【锁屏】次数超过三次
            f = 0
            '''while True:
                print("··········lock screen more than 3 times,Please contact the administrator··········")
                psd3 = int(input("Please enter the administrator password\t"))
                if psd3 == psd2:  # 管理员密码
                    continue
                else:
                    psd3 = int(input("Please enter the administrator password\t"))
                    times = 0'''
            gly()
    else:#【第一层密码】验证成功
        print("密码正确,加载中")
        while True:
            w = e.buttonbox("登录成功(初始密码:0000)", title="'CTF' systems",choices=("ok", "新用户?创建一个!", "quit"))
            if w == "quit":
                sys.exit()
            if w == "新用户?创建一个!":
                new_id = e.enterbox(msg="新的ID", title="'Hack' systems")
                new_psd = e.enterbox(msg="新的密码", title="'Hack' systems")
                #new_name = e.enterbox(msg="你的昵称", title="'Hack' systems")
                #new = [new_id, new_psd]
                #card_new()
            if w == "ok":
                #e.msgbox("land successfully(initial password:0000)",title = "'CTF' systems",ok_button = "yes")
                c = e.multpasswordbox("您的帐号···",title = "'Hack' systems",fields = ("ID","PASSWORD"))
                #money = card1_mony
                if c == [card1_name,card1_psd]:  # 密码正确
                    card1()#执行函数
                elif c == [card2_name, card2_psd]:  # 密码正确
                    card2()#执行函数
                elif c == [card3_name, card3_psd]:  # 密码正确
                    card3()#执行函数
                elif c == [card4_name, card4_psd]:  # 密码正确
                    card4()#执行函数
                elif c == [card5_name, card5_psd]:  # 密码正确
                    card5()#执行函数
                elif c == [card6_name, card6_psd]:  # 密码正确
                    card6()#执行函数
                elif c == [card7_name, card7_psd]:  # 密码正确
                    card7()#执行函数
                elif c == [card_name, card_psd]:  # 密码正确
                    card()#执行函数
                elif c == [new_id,new_psd]:  # 密码正确
                    if new_member==0:
                        e.msgbox("你没有创建一个团队", title="'CTF' systems")  # buttonbox
                        new_member = e.buttonbox("是否创建?", title="'CTF' systems", choices=("yes", "no"))
                        if new_member == "yes":
                            new_Member = [new_id]
                            Member = 1
                            card_new()
                        elif new_member == "no":
                            Member = 0
                            card_new()
                    elif new_member==1:
                        card_new()
                    card_new()
                elif c!=[card1_name, card1_psd] or [card2_name, card2_psd] or [card3_name, card3_psd] or [card4_name, card4_psd] or [card5_name, card5_psd] or [card6_name, card6_psd] or [card7_name, card7_psd] or [card_name, card_psd] or [new_id,new_psd]:
                    e.msgbox("输入错误或没有帐户", title="'CTF' systems", ok_button="OK")
                    #sys.exit()
                    l = l+1
                    if l>=5:
                        e.msgbox("程序可能出现未知错误无法成功登录，可以联系开发者或重试!  \nQQ\t3139373615\n邮箱\t3139373615@qq.com\n电话号码\t13199827726", title="'CTF' systems", ok_button="OK")
                    continue
