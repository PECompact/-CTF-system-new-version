# coding=gbk
from class_ctf import Code,Name,Card
import sys
import easygui as e
try:
    while True:
        try:
            Code.b = int(input("~~~~~~~~~~��ӭ����CTFϵͳ~~~~~~~~~~\n������:\t2022.8.13\t������Ա:\tPECompact\n��������\n(ֻ����������)\t"))
        except ValueError:
            print("�������󣬲���Ϊ������")
        while Code.b != Code.a:#����һ�����롿��֤ʧ��
            Code.password_worse_first()
        else:#����һ�����롿��֤�ɹ�
            print("������ȷ,������")
            while True:
                w = e.buttonbox("��¼�ɹ�(��ʼ����:0000)", title="'CTF' systems",choices=("ok", "���û�?����һ��!", "quit"))
                if w == "quit":
                    sys.exit()
                if w == "���û�?����һ��!":
                    Name.new_name = e.enterbox(msg="�µ�ID", title="'Hack' systems")
                    Name.new_psd = e.enterbox(msg="�µ�����", title="'Hack' systems")
                    #new_name = e.enterbox(msg="����ǳ�", title="'Hack' systems")
                    #new = [new_id, new_psd]
                    #card_new()
                if w == "ok":
                    #e.msgbox("land successfully(initial password:0000)",title = "'CTF' systems",ok_button = "yes")
                    c = e.multpasswordbox("�����ʺš�����",title = "'Hack' systems",fields = ("ID","PASSWORD"))
                    #money = card1_mony
                    if c == [Name.card1_name,Name.card1_psd]:  # ������ȷ
                        Card.card(list_name = 0,list_Intedral = 0)#ִ�к���
                    elif c == [Name.card2_name, Name.card2_psd]:  # ������ȷ
                        Card.card(list_name = 1,list_Intedral = 1)#ִ�к���
                    elif c == [Name.card3_name, Name.card3_psd]:  # ������ȷ
                        Card.card(list_name = 2,list_Intedral = 2)#ִ�к���
                    elif c == [Name.card4_name, Name.card4_psd]:  # ������ȷ
                        Card.card(list_name = 3,list_Intedral = 3)#ִ�к���
                    elif c == [Name.card5_name, Name.card5_psd]:  # ������ȷ
                        Card.card(list_name = 4,list_Intedral = 4)#ִ�к���
                    elif c == [Name.card6_name, Name.card6_psd]:  # ������ȷ
                        Card.card(list_name = 5,list_Intedral = 5)#ִ�к���
                    elif c == [Name.card7_name, Name.card7_psd]:  # ������ȷ
                        Card.card(list_name = 6,list_Intedral = 6)#ִ�к���
                    elif c == [Name.card_name, Name.card_psd]:  # ������ȷ
                        Card.card(list_name = 7,list_Intedral = 7)#ִ�к���
                    elif c == [Name.new_name,Name.new_psd]:  # ������ȷ
                        Code.make_new()
                    elif c!=[Name.card1_name, Name.card1_psd] or [Name.card2_name, Name.card2_psd] or [Name.card3_name, Name.card3_psd] or [Name.card4_name, Name.card4_psd] or [Name.card5_name, Name.card5_psd] or [Name.card6_name, Name.card6_psd] or [Name.card7_name, Name.card7_psd] or [Name.card_name, Name.card_psd] or [Name.new_name,Name.new_psd]:
                        Code.no_card()
                        continue
except BaseException as worse:
    Code.result_worse(worse)