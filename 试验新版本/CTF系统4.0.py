# coding=gbk
from class_ctf import Code,Name,Card
import sys
import easygui as e
try:
    while True:
        try:
            Code.b = int(input("~~~~~~~~~~欢迎来到CTF系统~~~~~~~~~~\n最后更新:\t2022.8.13\t开发人员:\tPECompact\n输入密码\n(只可输入三次)\t"))
        except ValueError:
            print("输入有误，不能为非数字")
        while Code.b != Code.a:#【第一层密码】验证失败
            Code.password_worse_first()
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
                        Card.card(list_name = 0,list_Intedral = 0)#执行函数
                    elif c == [Name.card2_name, Name.card2_psd]:  # 密码正确
                        Card.card(list_name = 1,list_Intedral = 1)#执行函数
                    elif c == [Name.card3_name, Name.card3_psd]:  # 密码正确
                        Card.card(list_name = 2,list_Intedral = 2)#执行函数
                    elif c == [Name.card4_name, Name.card4_psd]:  # 密码正确
                        Card.card(list_name = 3,list_Intedral = 3)#执行函数
                    elif c == [Name.card5_name, Name.card5_psd]:  # 密码正确
                        Card.card(list_name = 4,list_Intedral = 4)#执行函数
                    elif c == [Name.card6_name, Name.card6_psd]:  # 密码正确
                        Card.card(list_name = 5,list_Intedral = 5)#执行函数
                    elif c == [Name.card7_name, Name.card7_psd]:  # 密码正确
                        Card.card(list_name = 6,list_Intedral = 6)#执行函数
                    elif c == [Name.card_name, Name.card_psd]:  # 密码正确
                        Card.card(list_name = 7,list_Intedral = 7)#执行函数
                    elif c == [Name.new_name,Name.new_psd]:  # 密码正确
                        Code.make_new()
                    elif c!=[Name.card1_name, Name.card1_psd] or [Name.card2_name, Name.card2_psd] or [Name.card3_name, Name.card3_psd] or [Name.card4_name, Name.card4_psd] or [Name.card5_name, Name.card5_psd] or [Name.card6_name, Name.card6_psd] or [Name.card7_name, Name.card7_psd] or [Name.card_name, Name.card_psd] or [Name.new_name,Name.new_psd]:
                        Code.no_card()
                        continue
except BaseException as worse:
    Code.result_worse(worse)