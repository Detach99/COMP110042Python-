## 1. 分析下列代码：
```python
sum = d = 0
while d != 10.0:
    d += 0.1
    sum += sum + d

```
    A. 语法上有错
    B. 程序进入死循环，因为循环中d一直为0.10
    C. 程序有可能不会停止，因为浮点数运算的问题
    D. 循环结束后，sum的值相当于 0 + 0.1 + 0.2 + 0.3 + ... + 1.9

> ans: C

## 2. 下列代码的输出是什么？
```python
def filter_numbers(numbers, n):
    results = []
    for number in numbers:
        if not number % n:
            results.append(number)
    return results

for i, v in enumerate(filter_numbers(range(0, 10), 4)):
    print(i, v)
```
> 0, 0
> 
> 1, 4
> 
> 2, 8

## 3. 写一个循环，打印100行的python
>ans:
```python
for i in range(100):
    print("python")
```

## 4. 将下列for循环用while重写：
```python
for count in range(100, 0 -1):
    print(count)
```
>ans:
```python
    i = 100
    while i:
        print(i)
        i -= 1
```

## 5. 写一个while循环，接收用户的输入，然后输出其输入的内容，直到用户输入quit时结束。你也可以如同ppt中介绍的一样，试着用多种方法实现。
>ans:
```python
while True:
    In = input("请输入:(quit退出)")
    if In == "quit":
        break
    print(In)
```


## 6. 写一个while循环求从1开始的前面n个奇数的和.
1 + 3 + 5 + ... + 2n-1
>ans:
```python
def PrintOdds(n):
    i = 0
    sum = 0
    while i<n:
        if i % 2:
            sum+=i
        i+=1
    print(sum)
```

## 7. 下列循环中的print调用多少次？
```python
for i in range(10):
    for j in range(i):
        print(i * j)
```
	 A. 100
	 B. 55
	 C. 10
	 D. 45
>ans: D

## 8. 如果不执行下面的代码，你能够知道其输出的是什么吗？(有些难度的题)
```python
for i in range(1, 7):
    for j in range(6, 0, -1):
       print(j if j <= i else " ", end = " ")
    print()
```
>ans:
```bash
          1
        2 1
      3 2 1
    4 3 2 1
  5 4 3 2 1
6 5 4 3 2 1
```

## 9. 下面这段代码中，前面部分产生一个包含了许多整数的列表，接下来的for循环试图完成如下任务：
#### a. 将那些大于25的元素从列表中移走
#### b. 如果某个元素的值小于0，则更新该元素使得其为原来值的绝对值。
遗憾的是for循环的实现有错误，请改正其中的错误。
如果 s最初为
s = [-19, 18, 27, 4, 14, 35, 0, 27, -5, 35, 13, 2, 50, 3, 25, -9]
则最后应该为：
[19, 18, 4, 14, 0, 5, 13, 2, 3, 25, 9]
```python
import random
random.seed(12345)
s = [random.randint(-20, 50) for i in range(random.randint(10,20))]
print(s)

for idx in range(len(s)):
    item = s[idx]
    if item > 25:
        s.remove(item)
    elif item < 0:
        item = -item
print(s)
```
> ans:
```python
import random
random.seed(12345)
s = [random.randint(-20, 50) for i in range(random.randint(10,20))]
print(s)

idx = 0
while idx<len(s):
    item = s[idx]
    if item > 25:
        s.remove(item)
        continue
    s[idx] = abs(s[idx])
    idx += 1
print(s)

```
