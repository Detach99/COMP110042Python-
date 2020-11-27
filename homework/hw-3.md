# 第3周作业

edited by 张雨竹

17307130246

on 2020.10.10
##  1. 尝试创建两个py文件，分别为util.py和test.py，分别运行看看有什么结果？你能够知道其中的原因吗？
<font size=1>
文件util.py的内容如下：

``` python
from math import pi, e, log2

def test_util():
    print('function test_util in util.py')
    print('__name__=', __name__)

if __name__ == '__main__':
    print('pi = %s\ne = %s' % (pi, e))
    test_util()
```
文件test.py的内容如下
``` python
import util

if __name__ == '__main__':
    print(util.log2(1024))
    util.test_util()
```

</font>

### ans:
![question1-ans](https://s1.ax1x.com/2020/10/10/0snfAO.png)
util.py 为函数,作用是调用math模块,并且打印出一系列信息; test.py将util.py作为模块调用, 将参数1024传入util.py中math.log2()函数, 计算得到log2(1024)=10

## 2. 采取多种方式（字符串转义、长字符串、原始字符串）定义一个字符串，该字符串应该包含下面两行文字
It's ok.

"Thank you very much!" she said.

### ans: 
```python
str = 'It\'s ok\n\n"Thank you very much!\" she said.' #字符串转义

str1 = '''It's ok.

"Thank you very much!" she said.'''#长字符串

str2 = r'It'+r"'s ok"+'\n\n'+r'"Thank you very much."she said.' #原始字符串
 ```    

## 3. 请问下列语句的输出应该是什么？
```python
print('new' 'line')
```
### ans: 
```bash
newline
```

## 4. 不执行你能够知道下述两个表达式的结果分别是什么吗？  
  chr(ord('A') + 4)    ord('4')-ord('0')
### ans: 
'E'
4

## 5. 下面的表达式中会出现错误的是(         )
      a. int('10.8')
      b. float('10')
      c. int('10')
      d. float(10.8)
      e. int(10.8)
      f. float('1.08e+1')

### ans: 
a

## 6. 下面python语句执行的结果是什么？
```python
# 字符串格式化的用法, 以浮点数为例
f1 = float('1230.141592653589793')
print('format string:%%s\t(%s)' % f1)
print('format string:%%f\t(%f)' % f1)
print('format string:%%.4\t(%.4f)' % f1)
print('format string:%%8.f\t(%8.f)' % f1)
print('format string:%%8.4f\t(%8.4f)' % f1)
print('format string:%%08.4f\t(%08.4f)' % f1)
print('format string:%%8.2f\t(%8.2f)' % f1)
print('format string:%%08.2f\t(%08.2f)' % f1)
print('format string:%%-8.2f\t(%-8.2f)' % f1)
```
### ans:
![question-6 ans](https://s1.ax1x.com/2020/10/10/0sKWfe.png)

## 7.  不执行下述代码，请给出两个print函数最后的输出。
```python 
month = "June"
day = 5
year = 2011
print("The date is {} {}, {}.".format(month, day, year))
print("{:<15s}|{:>8.1f}".format("Length",23.875))
```
### ans:
```bash
The date is June 5, 2011.
Length         |    23.9
```