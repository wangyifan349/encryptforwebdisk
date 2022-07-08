import re,os,sys
from Crypto.Cipher import AES
s=input("输入python3能理解的文件路径")
os.chdir(str(s))
def decryptdata(filename):
   if os.path.exists(filename)==True:
      file_in = open(filename, "rb")
      tag, ciphertext = [ file_in.read(x) for x in (16, -1) ]
      nonce=b'123'#这个也可以改一下,需要和加密的时候填写一样的。
      key=b'Fjwld.xkwpe[fjsld.xaer@!'#密码在这里QAQ
# let's assume that the key is somehow available again
      cipher = AES.new(key, AES.MODE_GCM, nonce)
      data = cipher.decrypt_and_verify(ciphertext,tag)
      with open(filename,"wb")as f:
          f.write(data)
   else:
      print("python3 无法命中文件,而文件存在,解决办法:检查或修改路径")


      
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
   for name in files:
      print("@@",os.path.join(root, name))#这里能找到全部的文件(并带有完整路径)
      fname=os.path.join(root,name)
      decryptdata(fname)
   for name in dirs:
      print("!!",os.path.join(root, name))

