from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import re,os,sys,time
global wrong,time
wrong=0
wronglist=[]
print("加密可能导致你的文件无法恢复的破坏,请反复测试程序再运行哦!")
s=str(input("输入python3能理解的文件路径，例如:C:\\\文件夹\\子文件夹"))
os.chdir(s)
def encryptdata(filename):
    global wrong
    enfilename=filename
    if os.path.exists(filename)==True:
        with open(filename,"rb")as f:
            data=f.read()
        key = b'Fjwld.xkwpe[fjsld.xaer@!'#密码在这里,记得修改哦,16为或者24位随机字符,这里我随便填写的
        cipher = AES.new(key, AES.MODE_GCM,nonce=b'123')
        ciphertext, tag = cipher.encrypt_and_digest(data)
        file_out = open(enfilename, "wb")
        #print(cipher.nonce)
        #print(tag)
        [ file_out.write(x) for x in (tag, ciphertext) ]
        file_out.close()
    else:
        print("遍历到了文件但是python3似乎无法准确命中文件")
        wrong=wrong+1
        wronglist.append(str(filename))
for root, dirs, files in os.walk(os.getcwd(),topdown=False):
   for name in files:
      #print("@@",os.path.join(root, name))#这里能找到全部的文件(并带有完整路径)
      fname=os.path.join(root,name)
      encryptdata(fname)
   for name in dirs:
      #print("!!",os.path.join(root, name))
      pass
print("完成了任务,错误文件有",wrong)
print(wronglist)
time.sleep(2000)
