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
        self.vi = "1.0:���µ�¼ϵͳ�����ף�\n1.2�����¿ɶ���Ա��¼\n1.2.1���޸��޷�������½��bug\n1.4�������˵�½�˵�\n1.5���޸���ȫӢ��\n1.6���Ż��˵�¼����\n1.7�����������ܼ��δ֪������\n1.8����ǿ�������½��׼ȷ��\n1.9���޸��˹���Ա��֤���޷������˳�ѭ����bug\n2.0�������˲鿴�����汾������Ϣ����\n2.1���޸���ʧ����֤����Ա������ٴ���֤�ɹ��޷������˳���bug\n2.2���޸��˵�������֤��һ������ɹ�ʱ�޷���������ϵͳ��bug\n2.3�������˷��ص�¼����Ĺ���\n2.4���޸������������ʱ�����bug\n2.5������'����'����\n2.6���Ż������㷨\n2.7���޸��޷������������е�bug\n2.8���޸�����Ա�����������\n2.9���Ż��쳣��������\n3.0���޸���֪���⣬��߳����ȶ���"

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
    def gly(self):  # �������ѭ��(����Ա��֤)
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

    def card1(self):  # �û���Ϣ
        e.msgbox("��½�ɹ�", title="'CTF' systems", ok_button="OK")
        while True:  # ����
            b = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                            choices=("��Ա", "����", "�汾��Ϣ", "����,���빤��", "��������", "���ص�¼����", "�˳�"))
            if b == "��Ա":  # ��Ա��Ϣ
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "����":  # ����
                e.msgbox(Name.card1_Integral, title="'CTF' systems")
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
                e.msgbox(self.n1, title="'CTF' systems", ok_button="OK")
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
    def card2(self):  # �û���Ϣ
        e.msgbox("��½�ɹ�", title="'CTF' systems", ok_button="OK")
        while True:  # ����
            b = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                            choices=("��Ա", "����", "�汾��Ϣ", "����,���빤��", "��������", "���ص�¼����", "�˳�"))
            if b == "��Ա":  # ��Ա��Ϣ
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "����":  # ����
                e.msgbox(Name.card2_Integral, title="'CTF' systems")
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
                e.msgbox(self.n2, title="'CTF' systems", ok_button="OK")
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
    def card3(self):  # �û���Ϣ
        e.msgbox("��½�ɹ�", title="'CTF' systems", ok_button="OK")
        while True:  # ����
            b = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                            choices=("��Ա", "����", "�汾��Ϣ", "����,���빤��", "��������", "���ص�¼����", "�˳�"))
            if b == "��Ա":  # ��Ա��Ϣ
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "����":  # ����
                e.msgbox(Name.card3_Integral, title="'CTF' systems")
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
                e.msgbox(self.n3, title="'CTF' systems", ok_button="OK")
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
    def card4(self):  # �û���Ϣ
        e.msgbox("��½�ɹ�", title="'CTF' systems", ok_button="OK")
        while True:  # ����
            b = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                            choices=("��Ա", "����", "�汾��Ϣ", "����,���빤��", "��������", "���ص�¼����", "�˳�"))
            if b == "��Ա":  # ��Ա��Ϣ
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "����":  # ����
                e.msgbox(Name.card4_Integral, title="'CTF' systems")
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
                e.msgbox(self.n4, title="'CTF' systems", ok_button="OK")
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
    def card5(self):  # �û���Ϣ
        e.msgbox("��½�ɹ�", title="'CTF' systems", ok_button="OK")
        while True:  # ����
            b = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                            choices=("��Ա", "����", "�汾��Ϣ", "����,���빤��", "��������", "���ص�¼����", "�˳�"))
            if b == "��Ա":  # ��Ա��Ϣ
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "����":  # ����
                e.msgbox(Name.card5_Integral, title="'CTF' systems")
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
                e.msgbox(self.n5, title="'CTF' systems", ok_button="OK")
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
    def card6(self):  # �û���Ϣ
        e.msgbox("��½�ɹ�", title="'CTF' systems", ok_button="OK")
        while True:  # ����
            b = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                            choices=("��Ա", "����", "�汾��Ϣ", "����,���빤��", "��������", "���ص�¼����", "�˳�"))
            if b == "��Ա":  # ��Ա��Ϣ
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "����":  # ����
                e.msgbox(Name.card6_Integral, title="'CTF' systems")
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
                e.msgbox(self.n6, title="'CTF' systems", ok_button="OK")
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
    def card7(self):  # �û���Ϣ
        e.msgbox("��½�ɹ�", title="'CTF' systems", ok_button="OK")
        while True:  # ����
            b = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                            choices=("��Ա", "����", "�汾��Ϣ", "����,���빤��", "��������", "���ص�¼����", "�˳�"))
            if b == "��Ա":  # ��Ա��Ϣ
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "����":  # ����
                e.msgbox(Name.card7_Integral, title="'CTF' systems")
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
                e.msgbox(self.n7, title="'CTF' systems", ok_button="OK")
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
    def card(self):  # �û���Ϣ
        e.msgbox("��½�ɹ�", title="'CTF' systems", ok_button="OK")
        while True:  # ����
            b = e.buttonbox("��ѡ������Ҫ�ķ���", title="'CTF' systems",
                            choices=("��Ա", "����", "�汾��Ϣ", "����,���빤��", "��������", "���ص�¼����", "�˳�"))
            if b == "��Ա":  # ��Ա��Ϣ
                e.msgbox(Name.name, title="'CTF' systems")  # buttonbox
            elif b == "����":  # ����
                e.msgbox(Name.card_Integral, title="'CTF' systems")
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
                e.msgbox(self.n, title="'CTF' systems", ok_button="OK")
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
name_go = True
try:
    while True:
        try:
            if name_go:
                Code.b = int(input("~~~~~~~~~~��ӭ����CTFϵͳ~~~~~~~~~~\n������:\t2022.8.13\t������Ա:\tPECompact\n��������\n(ֻ����������)\t"))
        except ValueError:
            print("�������󣬲���Ϊ������")
        if name_go:
            while Code.b != Code.a:#����һ�����롿��֤ʧ��
                try:
                    if Code.con==False:
                        print("�����������")
                    if name_go:
                        Code.b = int(input("~~~~~~~ �������� ~~~~~~~\n(ֻ����������)\t"))
                        Code.con = False
                except ValueError:
                    print("�������󣬲���Ϊ������")
                Code.i = Code.i+1
                if Code.i == 2 and Code.b != Code.a:#����һ�����롿��֤ʧ�ܴ�����������
                    if Code.con==False:
                        print("�����������")
                    #init(autoreset=False)
                    Code.q = 30  #����ʱ��
                    Code.f = Code.f+1
                    if name_go:
                        name_go = False
                        print("����3�����ϣ���30������������!")
                        Code.i = -1
                        for p in range(30):
                            t.sleep(1)
                            print("~~~~~~ ������ ~~~~~~(",Code.q,")")
                            Code.q = Code.q-1
                        Code.con = True
                        name_go = True

                if Code.f >= 3:#��������������������
                    Code.f = 0
                    Code.gly()
                    Code.con = True
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
                            Card.card1()#ִ�к���
                        elif c == [Name.card2_name, Name.card2_psd]:  # ������ȷ
                            Card.card2()#ִ�к���
                        elif c == [Name.card3_name, Name.card3_psd]:  # ������ȷ
                            Card.card3()#ִ�к���
                        elif c == [Name.card4_name, Name.card4_psd]:  # ������ȷ
                            Card.card4()#ִ�к���
                        elif c == [Name.card5_name, Name.card5_psd]:  # ������ȷ
                            Card.card5()#ִ�к���
                        elif c == [Name.card6_name, Name.card6_psd]:  # ������ȷ
                            Card.card6()#ִ�к���
                        elif c == [Name.card7_name, Name.card7_psd]:  # ������ȷ
                            Card.card7()#ִ�к���
                        elif c == [Name.card_name, Name.card_psd]:  # ������ȷ
                            Card.card()#ִ�к���
                        elif c == [Name.new_name,Name.new_psd]:  # ������ȷ
                            if Code.new_member==0:
                                e.msgbox("��û�д���һ���Ŷ�", title="'CTF' systems")  # buttonbox
                                new_member = e.buttonbox("�Ƿ񴴽�?", title="'CTF' systems", choices=("yes", "no"))
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
                            e.msgbox("��������û���ʻ�", title="'CTF' systems", ok_button="OK")
                            #sys.exit()
                            Code.l = Code.l+1
                            if Code.l>=5:
                                e.msgbox("������ܳ���δ֪�����޷��ɹ���¼��������ϵ�����߻�����!  \nQQ\t3139373615\n����\t3139373615@qq.com\n�绰����\t13199827726", title="'CTF' systems", ok_button="OK")
                            continue

except BaseException as e:
    print("\n_�ѱ��رջ�����쳣_")
    print("��������ѱ��رջ����δ֪�����޷��ɹ����У�������ϵ�����߻�����!  \nQQ\t3139373615\n����\t3139373615@qq.com\n�绰����\t13199827726")
    print("������룺",repr(e))
    time.sleep(5)