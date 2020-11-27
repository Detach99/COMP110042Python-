## 1) 假设 t = (1, 2, 4, 3), t[1 : 3]为？
	A. (1, 2)
	B. (1, 2, 4)
	C. (2, 4)
	D. (2, 4, 3)
    E. [2, 4]
    F. [1, 2]
#### D

## 2) 假设 t1 = (1, 2, 4, 3), t2 = (1, 2, 3, 4), t1 < t2结果为？
    A. True
    B. False
#### B
## 3) 下列代码执行后输出为？
```python
x, y = 1, 2
x, y = y, x
print(x, y)
```
	 A. 1 1
	 B. 2 2
	 C. 1 2
	 D. 2 1
#### D

## 4) 下列代码执行后变量x、y和z 的值是什么？

```python
x, y, z = '123'
```
	 A. 1 2 3
	 B. '1' '2' '3'
	 C. '123' ''  ''
	 D. '123'  None  None

#### B 

## 5) 下列代码执行后变量x、y、z和f的值是什么？
```python
f = list('abcdefg')
x, *y, f[:4], z = '1234567890'
```
#### x = '1', y = ['2', '3', '4', '5', '6', '7' ,'8'], f=['9', 'e', 'f', 'g'], z = '0'

## 6)  下列代码执行后的结果是？
```python
list1 = range(3)
list2 = 'abcd'
list3 = 'ABC'
list4 = list(zip(list1,list2,list3))
print(list4)
```
    A. [(0, 'a', 'A'), (1, 'b', 'B'), (2, 'c', 'C') ]
    B. [(0, 'a', 'A'), (1, 'b', 'B'), (2, 'c', 'C'), (None, 'd', None) ]
    C. [[0, 'a', 'A'], [1, 'b', 'B'], [2, 'c', 'C'] ]
    D. 抛出异常
#### A

## 7) 下列代码执行后的结果是？
```python
list1 = range(3)
for i in enumerate(list1):
    print(i,end='\t')
```
    A. (0, 0)	(1, 1)	(2, 2)
    B. [0, 0]	[1, 1]	[2, 2]
    C. (1, 0)	(2, 1)	(3, 2)
    D. 0	1	2
#### A

## 8.  假设isPrime是一个boolean变量，下列哪个判断isPrime是否为True的选项最好？
	 A. if isPrime = True:
	 B. if isPrime == True:
	 C. if isPrime:
	 D. if not isPrime = False:
	 E. if not isPrime == False:
#### C

## 9. 分析下列代码，最后的输出是什么？
```python
even = False
if even = True:
    print("It is even!")
```
#### invalid syntax

## 10. 下列代码最后输出是什么？
```python
x = z = 1
y = -1

if x > 0:
    if y > 0:
        print("x > 0 and y > 0")
elif z > 0:
    print("x < 0 and z > 0")
```
    A. x > 0 and y > 0
    B. x < 0 and z > 0
    C. x < 0 and z < 0
    D. 没有输出
#### D

## 11. 下列代码最后输出是什么？
```python
income = 4001
if income > 3000:
    print("Income is greater than 3000")
elif income > 4000:
    print("Income is greater than 4000")
```
	 A. 没有输出
	 B. Income is greater than 3000
	 C. Income is greater than 3000
	    Income is greater than 4000
	 D. Income is greater than 4000
	 E. Income is greater than 4000
	    Income is greater than 3000
#### B

## 12. 下列代码执行后y的值是？
```python
x = 0
y = 10 if x > 0 else -10
```
    A. -10
    B. 0
    C. 10
    D. 20
    E. 非法表达式
#### A

## 13. 分析下列代码
```python
#代码块1

if number % 2 == 0:
    even = True
else:
    even = False

#代码块2

even = True if number % 2 == 0 else False

#代码块3
even = number % 2 == 0
```
    A. 代码块2有语法错误
    B. 代码块3和2有语法错误
    C. 3个代码块都正确
	D. 代码块1有语法错误

#### C

## 14. 请针对下列描述,分别写出相应的条件表达式以判断该描述是否成立。
    a. x和y都等于0
    b. x和y其中至少有一个等于0
    c. x和y至少有一个等于0，但是不会都等于0
#### a: if not (a or b):
#### b: if not (a and b):
#### c: if (not a and b) or (not b and a)

## 15. 请使用德摩根定理简化如下条件表达式，要求不出现逻辑not运算
    not (number % 2 == 0 and number % 3 == 0)
#### number % 2 or number % 3

## 16. x为一个整数，请写出相应的代码，根据x的取值分别输出x为正整数、x为0和x为负整数。
#### code:
```python
if x>0:
    print("x是正整数")
elif x==0:
    print("x为0")
else:
    print("x为负整数")
```

## 17.  下列代码执行后输出是...
```python
number = 6
while number > 0:
    number -= 3
    print(number, end = ' ')
```
    A. 6 3 0
    B. 6 3
    C. 3 0
    D. 3 0 -3
    E. 0 -3
#### C

## 18. 下列代码执行后输出是....?
```python
sum = 0
item = 0
while item < 5:
    item += 1
    sum += item
    if sum > 4: break

print(sum)
```
    A. 5
    B. 6
    C. 7
    D. 8
#### B

## 19. 下列代码执行后输出是....?
```python
sum = 0
item = 0
while item < 5:
    item += 1
    sum += item
    if sum >= 4: continue

print(sum)
```
    A. 15
    B. 16
    C. 17
    D. 18
#### A

## 20. 下列代码执行完后的输出是：
```python
number = 25
isPrime = True
i = 2
while i < number and isPrime:
    if number % i == 0:
        isPrime = False
    i += 1

print("i is", i, "isPrime is", isPrime)
```
    A. i is 5 isPrime is True
    B. i is 5 isPrime is False
    C. i is 6 isPrime is True
    D. i is 6 isPrime is False

#### D