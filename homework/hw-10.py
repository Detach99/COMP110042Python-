#1 写一个循环，询问用户 "Do you want to play again or quit?(y/n)" ，该循环将一直重复直到用户输入y或者n(可以是小写和大写形式)为止
while True:
   p = input("Do you want to play again or quit?(y/n)")
   if p in "Nn":
    break

#2 写一个函数is_http_url，其参数为一个字符串，如果该字符串以https://或者http://开头，则返回True，否则返回False
def is_http_url(url):
    if "//" not in url:
        return False
    if "https:" in url.split('//'):
        return True
    elif "http:" in url.split("//"):
        return True
    else:
        return False

#3 写一个函数remove_chars(text, chars)，将text中那些在chars中出现的字符移走，返回一个新的字符串。
def remove_chars(text, chars):
    new_text = []
    for c in text:
        if c not in chars:
            new_text.append(c)
    return "".join(new_text)
#4 要生成10个随机的位于[0,100]范围内的整数，并且将其保存在文件numbers.txt中，一个整数一行。请写出相应的代码。

import random
import os
fname = os.getcwd()+"\\numbers.txt"
f = open(fname, "w+")
print("file name:"+f.name)
for _ in range(0,10):
    f.writelines(str(random.randint(1,100))+"\n")
f.close()
print("file closed: {}".format(f.closed))
    
#5 上一题产生的numbers.txt，每行有一个整数，求其平均值。请写出相应的代码。
fname = os.getcwd()+"\\numbers.txt"
f = open(fname, "r")
raw = f.read()
raw = raw.split("\n")
print("mean is: {}".format(sum([int(i) for i in raw[:-1]])/(len(raw[:-1]))))
f.close()
print("file closed: {}".format(f.closed))

