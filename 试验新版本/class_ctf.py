# coding=gbk
from urllib.parse import quote, unquote
import easygui as e
import hashlib
import base64
import time
import sys
import os
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

        self.card3_name = "Ѧ����"
        self.card3_psd = "0000"
        self.card3_Integral = "unknown"

        self.card4_name = "�����"
        self.card4_psd = "0000"
        self.card4_Integral = "unknown"

        self.card5_name = "��׿��"
        self.card5_psd = "0000"
        self.card5_Integral = "unknown"

        self.card6_name = "�������"
        self.card6_psd = "0000"
        self.card6_Integral = "unknown"

        self.card7_name = "�Ź���"
        self.card7_psd = "0000"
        self.card7_Integral = "unknown"

        self.new_name = {}#"q"
        self.new_psd = {}#"q"
        self.new_Integral = "unknown"

        self.name = f"name1(developer): {self.card1_name}\nname2: {self.card2_name}\nname3: {self.card3_name}\nname4: {self.card4_name}\nname5: {self.card5_name}\nname6: {self.card6_name}\nname7: {self.card7_name}\nteacher: {self.card_name}"
        self.list_Integral = [self.card1_Integral,self.card2_Integral,self.card3_Integral,self.card4_Integral,self.card5_Integral,self.card6_Integral,self.card7_Integral,self.card_Integral]
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
        self.vi = "1.0:���µ�¼ϵͳ�����ף�\n1.2�����¿ɶ���Ա��¼\n1.2.1���޸��޷�������½��bug\n1.4�������˵�½�˵�\n1.5���޸���ȫӢ��\n1.6���Ż��˵�¼����\n1.7�����������ܼ��δ֪������\n1.8����ǿ�������½��׼ȷ��\n1.9���޸��˹���Ա��֤���޷������˳�ѭ����bug\n2.0�������˲鿴�����汾������Ϣ����\n2.1���޸���ʧ����֤����Ա������ٴ���֤�ɹ��޷������˳���bug\n2.2���޸��˵�������֤��һ������ɹ�ʱ�޷���������ϵͳ��bug\n2.3�������˷��ص�¼����Ĺ���\n2.4���޸������������ʱ�����bug\n2.5������'����'����\n2.6���Ż������㷨\n2.7���޸��޷������������е�bug\n2.8���޸�����Ա�����������\n2.9���Ż��쳣��������\n3.0���޸���֪���⣬��߳����ȶ���\n4.0���Ż�������߳���Ч��"
    # ����MD5����
    def md5(self,s):
        # new_id = e.enterbox(msg="new_ID", title="'Hack' systems")
        original = s
        md = hashlib.md5()
        s = s.encode(encoding='utf-8')
        md.update(s)
        e.msgbox('Original:' + original, title="'CTF' systems")
        e.msgbox('Md5 Encryption:' + md.hexdigest(), title="'CTF' systems")
    # ����sh1����
    def sh1(self,s):
        original = s
        sh = hashlib.sha1()
        s = s.encode(encoding='utf-8')
        e.msgbox('Original:' + original, title="'CTF' systems")
        e.msgbox('SH1 Encryption:' + sh.hexdigest(), title="'CTF' systems")
    # ���ַ���ת��Ϊbase64�����ʽ
    def strToB64(self,s):
        encode = base64.b64encode(s.encode("utf-8"))
        e.msgbox('Original:' + s, title="'CTF' systems")
        e.msgbox('Base64 encode:' + str(encode), title="'CTF' systems")
    # ��base64�����ʽת��Ϊ�������ַ�����
    def b64ToStr(self,s):
        decode = base64.b64decode(str(s))
        e.msgbox('Base64:' + s, title="'CTF' systems")
        e.msgbox('Base64 decode:' + str(decode), title="'CTF' systems")
    # ���ַ���תΪb32�����ʽ
    def strToB32(self,s):
        encode = base64.b32encode(s.encode("utf-8"))
        e.msgbox('Original:' + s, title="'CTF' systems")
        e.msgbox('Base32 encode:' + str(encode), title="'CTF' systems")
    # ��base32�����ʽת��Ϊ�������ַ�����
    def b32ToStr(self,s):
        decode = base64.b32decode(str(s))
        e.msgbox('Base32:' + s, title="'CTF' systems")
        e.msgbox('Base32 decode:' + str(decode), title="'CTF' systems")
    # ���ַ���תΪbase16�����ʽ
    def strToB16(self,s):
        encode = base64.b16encode(s.encode("utf-8"))
        e.msgbox('Original:' + s, title="'CTF' systems")
        e.msgbox('Base16 encode:' + str(encode), title="'CTF' systems")
    # ��base16�����ʽת��Ϊ�������ַ�����
    def b16ToStr(self,s):
        decode = base64.b16decode(str(s))
        e.msgbox('Base16:' + s, title="'CTF' systems")
        e.msgbox('Base16 decode:' + str(decode), title="'CTF' systems")
    # ��������ת��Ϊʮ����
    def binToDec(self,s):
        result = int(s, 2)
        e.msgbox('Binary :' + str(s), title="'CTF' systems")
        e.msgbox('Decimal :' + str(result), title="'CTF' systems")
    # ���˽���ת��Ϊʮ����
    def octToDec(self,s):
        result = int(s, 8)
        e.msgbox('Octal :' + str(s) + s, title="'CTF' systems")
        e.msgbox('Decimal :' + str(result), title="'CTF' systems")
    # ��ʮ������ת��Ϊʮ����
    def hexToDec(self,s):
        result = int(s, 16)
        e.msgbox('Hex :' + str(s) + s, title="'CTF' systems")
        e.msgbox('Decimal :' + str(result), title="'CTF' systems")
    # ��ʮ����ת��Ϊ������
    def decToBin(self,s):
        s = int(s)
        result = bin(s)
        e.msgbox('Decimal:' + str(s), title="'CTF' systems")
        e.msgbox('Binary:' + str(result), title="'CTF' systems")
    # ��ʮ����ת��Ϊ�˽���
    def decToOct(self,s):
        s = int(s)
        result = oct(s)
        e.msgbox('Decimal :' + str(s), title="'CTF' systems")
        e.msgbox('Octal :' + str(result), title="'CTF' systems")
    # ��ʮ����ת��Ϊʮ������
    def decToHex(self,s):
        s = int(s)
        result = hex(s)
        e.msgbox('Decimal :' + str(s), title="'CTF' systems")
        e.msgbox('Hex :' + str(result), title="'CTF' systems")
    # ����url����
    def url_encode(self,s):
        encode = quote(s)
        e.msgbox('Original:' + s, title="'CTF' systems")
        e.msgbox('URL encode:' + encode, title="'CTF' systems")
    # ����url����
    def url_decode(self,s):
        decode = unquote(s)
        e.msgbox('URL encode:' + s, title="'CTF' systems")
        e.msgbox('URL decode:' + decode, title="'CTF' systems")
    # ����ĸת��Ϊ��Ӧ��ASCII
    def lettToASCII(self,s):
        e.msgbox('Letters:' + s, title="'CTF' systems")
        result = ''
        for i in s:
            result = result + str(ord(i)) + ' '
        e.msgbox('ASCII  :' + result, title="'CTF' systems")
    # ��ASCIIת��Ϊ��Ӧ����ĸ�Լ��ַ�
    def asciiToLett(self,s):
        list = s.split(' ')
        result = ''
        e.msgbox('ASCII    :' + s, title="'CTF' systems")
        for i in list:
            i = int(i)
            result = result + chr(i)
        e.msgbox('Letters  :' + result, title="'CTF' systems")
    #�������ѭ��(����Ա��֤)
    def gly(self):
        while True:
            try:
                print("��������������������������Ļ����3�Σ�����ϵ����Ա��������������������")
                self.psd3 = int(input("���������Ա����\t"))
            except ValueError:
                print("�������󣬲���Ϊ������")
            except BaseException as e:
                print("�����쳣")
                print(repr(e))
            if self.psd3 == self.psd2:  # ����Ա����
                return
    #�쳣������Ϣ
    def result_worse(self,worse):
        print("\n_�ѱ��رջ�����쳣_")
        print("��������ѱ��رջ����δ֪�����޷��ɹ����У�������ϵ�����߻�����!  \nQQ\t3139373615\n����\t3139373615@qq.com\n�绰����\t13199827726")
        print("������룺", repr(worse))
        time.sleep(3)
    #�������Ŷ�
    def make_new(self):
        if self.new_member == 0:
            e.msgbox("��û�д���һ���Ŷ�", title="'CTF' systems")  # buttonbox
            new_member = e.buttonbox("�Ƿ񴴽�?", title="'CTF' systems", choices=("yes", "no"))
            if new_member == "yes":
                self.new_Member = [Name.new_name]
                self.member = 1
                Card.card_new()
            elif new_member == "no":
                # Code.member = 0
                Card.card_new()
        elif self.new_member == 1:
            Card.card_new()
        # Card.card_new()
    #��������û���ʻ����ڶ���:�û���½��
    def no_card(self):
        e.msgbox("��������û���ʻ�", title="'CTF' systems", ok_button="OK")
        # sys.exit()
        self.l = self.l + 1
        if self.l >= 5:
            e.msgbox("������ܳ���δ֪�����޷��ɹ���¼��������ϵ�����߻�����!  \nQQ\t3139373615\n����\t3139373615@qq.com\n�绰����\t13199827726",
                     title="'CTF' systems", ok_button="OK")
    #��������>=����
    def lock_screen_three(self):
        self.f = 0
        self.gly()
        self.con = True
    #����һ�����롿����>=����
    def worse_screen_three(self):
        if self.con == False:
            print("�����������")
        # init(autoreset=False)
        self.q = 30  # ����ʱ��
        self.f = self.f + 1
        print("����3�����ϣ���30������������!")
        self.i = -1
        for p in range(30):
            time.sleep(1)
            print("~~~~~~ ������ ~~~~~~(", self.q, ")")
            self.q = self.q - 1
        self.con = True
    #����һ�����롿���δ���
    def password_worse_first(self):
        try:
            if self.con == False:
                print("�����������")
            self.b = int(input("~~~~~~~ �������� ~~~~~~~\n(ֻ����������)\t"))
            self.con = False
        except ValueError:
            print("�������󣬲���Ϊ������")
        self.i = self.i + 1
        if self.i == 2 and self.b != self.a:  # ����һ�����롿��֤ʧ�ܴ�����������
            self.worse_screen_three()
        if self.f >= 3:  # ��������������������
            self.lock_screen_three()
Code = CODE()
class CARD():
    def __init__(self):
        #��������
        self.n1 = {"�������:": Name.card1_name, "�������:": Name.card1_psd}
        self.n2 = {"�������:": Name.card2_name, "�������:": Name.card2_psd}
        self.n3 = {"�������:": Name.card3_name, "�������:": Name.card3_psd}
        self.n4 = {"�������:": Name.card4_name, "�������:": Name.card4_psd}
        self.n5 = {"�������:": Name.card5_name, "�������:": Name.card5_psd}
        self.n6 = {"�������:": Name.card6_name, "�������:": Name.card6_psd}
        self.n7 = {"�������:": Name.card7_name, "�������:": Name.card7_psd}
        self.n = {"�������:": Name.card_name, "�������:": Name.card_psd}
        self.n_new = {"�������:": Name.new_name, "�������:": Name.new_psd}
        self.list_name = [self.n1,self.n2,self.n3,self.n4,self.n5,self.n6,self.n7,self.n]

    def card(self,list_name,list_Intedral):  # �û���Ϣ
        e.msgbox("��½�ɹ�", title="'CTF' systems", ok_button="OK")
        while True:  # ����
            b = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                            choices=("��Ա", "����", "�汾��Ϣ", "����,���빤��", "��������", "���ص�¼����", "�˳�"))
            if b == "��Ա":  # ��Ա��Ϣ
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "����":  # ����
                e.msgbox(Name.list_Integral[list_Intedral], title="'CTF' systems")
            elif b == "�汾��Ϣ":  # �汾��Ϣ
                e.msgbox(Code.vi, title="'CTF' systems")
            elif b == "����,���빤��":  # ������빤��
                tools = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                    choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                             "conversion of number systems", "ASCII"))
                if tools == "MD5 encryption":  # MD5����
                    Code.md5(e.enterbox(msg="original:"))
                elif tools == "sh1 encryption":  # shi����
                    Code.sh1(e.enterbox(msg="original:"))
                elif tools == "The family of the Base":  # Base
                    base = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                       choices=("base64", "base32", "base16"))
                    if base == "base64":  # base64��,����
                        Base64 = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base64 == "encode":  # base64����
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base64 == "decode":  # base64����
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base32":  # base32�࣬����
                        Base32 = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base32 == "encode":  # base64����
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base32 == "decode":  # base64����
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base16":  # base16�࣬����
                        Base16 = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base16 == "encode":  # base16����
                            Code.strToB16(e.enterbox(msg=""))
                        elif Base16 == "decode":  # base16����
                            Code.b16ToStr(e.enterbox(msg=""))
                elif tools == "conv6ersion of number systems":  # ����ת��
                    systems = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                          choices=("������ת��Ϊʮ����", "�˽���ת��Ϊʮ����",
                                                   "ʮ������ת��Ϊʮ����", "ʮ����ת��Ϊ������",
                                                   "ʮ����ת��Ϊ�˽���", "ʮ����ת��Ϊʮ������"))
                    if systems == "������ת��Ϊʮ����":
                        Code.binToDec(e.enterbox(msg="��������"))
                    elif systems == "�˽���ת��Ϊʮ����":
                        Code.octToDec(e.enterbox(msg="��������"))
                    elif systems == "ʮ������ת��Ϊʮ����":
                        Code.hexToDec(e.enterbox(msg="��������"))
                    elif systems == "ʮ����ת��Ϊ������":
                        Code.decToBin(e.enterbox(msg="��������"))
                    elif systems == "ʮ����ת��Ϊ�˽���":
                        Code.decToOct(e.enterbox(msg="��������"))
                    elif systems == "ʮ����ת��Ϊʮ������":
                        Code.decToHex(e.enterbox(msg="��������"))
                elif tools == "url":  # url
                    url = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                      choices=("encode", "decode"))
                    if url == "encode":  # url����
                        Code.url_encode(e.enterbox(msg=""))
                    elif url == "decode":  # url����
                        Code.url_decode(e.enterbox(msg=""))
                elif tools == "ASCII":  # ASCII
                    ASCII = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                        choices=("encode", "decode"))
                    if ASCII == "encode":  # ASCII����
                        Code.lettToASCII(e.enterbox(msg=""))
                    elif ASCII == "decode":  # ASCII����
                        Code.asciiToLett(e.enterbox(msg=""))
            elif b == "��������":  # ��������
                e.msgbox(self.list_name[list_name], title="'CTF' systems", ok_button="OK")
            elif b == "���ص�¼����":  # ���ص�¼����
                Quit1 = e.buttonbox("��ȷ��Ҫ��ô����?", title="'CTF' systems", choices=("yes", "no"))
                if Quit1 == "yes":
                    return
                elif Quit1 == "no":
                    continue
            elif b == "�˳�":  # �˳�
                Quit = e.buttonbox("��ȷ��Ҫ��ô����?", title="'CTF' systems", choices=("yes", "no"))
                if Quit == "yes":
                    sys.exit()
                elif Quit == "no":
                    continue

    def card_new(self):
        e.msgbox("��½�ɹ�", title="'CTF' systems", ok_button="OK")
        while True:  # ����
            b = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                            choices=("��Ա��Ϣ", "����", "�汾��Ϣ", "��������", "����,���빤��", "���ص�¼����", "�˳�"))
            if b == "��Ա��Ϣ":  # ��Ա��Ϣ
                if Code.new_member == 0:
                    e.msgbox("��û�д���һ���Ŷ�", title="'CTF' systems")  # buttonbox
                    new_member = e.buttonbox("�Ƿ�Ҫ������?", title="'CTF' systems", choices=("yes", "no"))
                    if new_member == "yes":
                        Code.new_Member = [Name.new_name]
                        Code.new_member = 1
                    elif new_member == "no":
                        continue
                elif Code.new_member == 1:
                    e.msgbox(Code.new_Member, title="'CTF' systems")  # buttonbox

            elif b == "����":  # ����
                e.msgbox(Name.new_Integral, title="'CTF' systems")
            elif b == "�汾��Ϣ":  # �汾��Ϣ
                e.msgbox(Code.vi, title="'CTF' systems")
            elif b == "����,���빤��":  # ������빤��
                tools = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                    choices=("MD5 encryption", "sh1 encryption", "The family of the Base", "url",
                                             "conversion of number systems", "ASCII"))
                if tools == "MD5 encryption":  # MD5����
                    Code.md5(e.enterbox(msg="original:"))
                elif tools == "sh1 encryption":  # shi����
                    Code.sh1(e.enterbox(msg="original:"))
                elif tools == "The family of the Base":  # Base
                    base = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                       choices=("base64", "base32", "base16"))
                    if base == "base64":  # base64��,����
                        Base64 = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base64 == "encode":  # base64����
                            Code.strToB64(e.enterbox(msg=""))
                        elif Base64 == "decode":  # base64����
                            Code.b64ToStr(e.enterbox(msg=""))
                    elif base == "base32":  # base32�࣬����
                        Base32 = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base32 == "encode":  # base64����
                            Code.strToB32(e.enterbox(msg=""))
                        elif Base32 == "decode":  # base64����
                            Code.b32ToStr(e.enterbox(msg=""))
                    elif base == "base16":  # base16�࣬����
                        Base16 = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                             choices=("encode", "decode"))
                        if Base16 == "encode":  # base16����
                            Code.strToB16(e.enterbox(msg=""))
                        elif Base16 == "decode":  # base16����
                            Code.b16ToStr(e.enterbox(msg=""))
                elif tools == "url":  # url
                    url = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                      choices=("encode", "decode"))
                    if url == "encode":  # url��,����
                        Code.url_encode(e.enterbox(msg=""))
                    elif url == "decode":  # url�࣬����
                        Code.url_decode(e.enterbox(msg=""))

                elif tools == "conversion of number systems":  # ����ת��
                    systems = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                          choices=("������ת��Ϊʮ����", "�˽���ת��Ϊʮ����",
                                                   "ʮ������ת��Ϊʮ����", "ʮ����ת��Ϊ������",
                                                   "ʮ����ת��Ϊ�˽���", "ʮ����ת��Ϊʮ������"))
                    if systems == "������ת��Ϊʮ����":
                        Code.binToDec(e.enterbox(msg="��������"))
                    elif systems == "�˽���ת��Ϊʮ����":
                        Code.octToDec(e.enterbox(msg="��������"))
                    elif systems == "ʮ������ת��Ϊʮ����":
                        Code.hexToDec(e.enterbox(msg="��������"))
                    elif systems == "ʮ����ת��Ϊ������":
                        Code.decToBin(e.enterbox(msg="��������"))
                    elif systems == "ʮ����ת��Ϊ�˽���":
                        Code.decToOct(e.enterbox(msg="��������"))
                    elif systems == "ʮ����ת��Ϊʮ������":
                        Code.decToHex(e.enterbox(msg="��������"))
                elif tools == "ASCII":  # ASCII
                    ASCII = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                                        choices=("encode", "decode"))
                    if ASCII == "encode":  # ASCII����
                        Code.lettToASCII(e.enterbox(msg=""))
                    elif ASCII == "decode":  # ASCII����
                        Code.asciiToLett(e.enterbox(msg=""))
            elif b == "��������":  # ��������
                e.msgbox(self.n_new, title="'CTF' systems", ok_button="OK")
            elif b == "���ص�¼����":  # ���ص�¼����
                Quit1 = e.buttonbox("��ȷ��Ҫ��ô����?", title="'CTF' systems", choices=("yes", "no"))
                if Quit1 == "yes":
                    return
                elif Quit1 == "no":
                    continue
            elif b == "�˳�":  # �˳�
                Quit = e.buttonbox("��ȷ��Ҫ��ô����?", title="'CTF' systems", choices=("yes", "no"))
                if Quit == "yes":
                    sys.exit()
                elif Quit == "no":
                    continue
Card = CARD()
if __name__ == "__main__":
    try:
        main = e.buttonbox(r"�������ȷ���Ϊ/CTFϵͳ4.0.py/,�Ƿ��?", title="'CTF' systems",choices=("��", "��"))
        if main=="��":
            start_dire = "CTFϵͳ4.0.py"
            try:
                r = os.system("python %s" % start_dire)
                if r==0:
                    print(f"{r}˳������")
                else:
                    print(f"{r}����ʧ��")
            except BaseException as worse:
                Code.result_worse(worse)
        else:
            print("��л���ʹ�á�����������PECompact")
            sys.exit()
    except BaseException as worse:
        Code.result_worse(worse)