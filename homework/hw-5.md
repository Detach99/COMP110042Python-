# <center> Homework 5 </center>
<p align = "right">17307130246<br>张雨竹<br>20201022</p>

## 1 假设list1 = [1, 3, 2, 4, 5, 2, 1, 0], 请问list1[:-1]为
	 A. 0
	 B. [1, 3, 2, 4, 5, 2, 1]
	 C. [1, 3, 2, 4, 5, 2]
	 D. [1, 3, 2, 4, 5, 2, 1, 0]
ans: D

## 2 请问下列代码执行后的输出为？
```python
list1 = [2,4,6,8,10,12,14,16,18,20] 
print (list1[0:1],list1[5:7])
```
    A.  [2,4] [10, 12]
    B.  [2,4] [12, 14]
    C.  [2] [12, 14]
    D.  [2] [10, 12, 14]
ans: C


## 3 请问下列代码执行后的输出为？
```python
myList = [1, 2, 5, 8, 9, 12]
print(myList[1:-1])
print(myList[-2])
print(myList[:]) 
print(myList[1::2]) 
print(myList[6])
```
ans:
```bash
[2, 5, 8, 9]
[9]
[1, 2, 5, 8, 9, 12]
[2, 8, 12]
IndexError: list index out of range
```
## 4 list1 = [3, 4, 5, 20, 5, 25, 1, 3], 执行list1.sort()后list1为? 
	 A. [3, 4, 5, 20, 5, 25, 1, 3]
	 B. [1, 3, 3, 4, 5, 5, 20, 25]
	 C. [25, 20, 5, 5, 4, 3, 3, 1] 
	 D. [1, 3, 4, 5, 20, 5, 25, 3]
ans: B

## 5 list1 = [3, 4, 5, 20, 5, 25, 1, 3], 执行list1.reverse()后list1为?  
	 A. [3, 4, 5, 20, 5, 25, 1, 3]
	 B. [1, 3, 3, 4, 5, 5, 20, 25]
	 C. [25, 20, 5, 5, 4, 3, 3, 1] 
	 D. [1, 3, 4, 5, 20, 5, 25, 3]
	 E. [3, 1, 25, 5, 20, 5, 4, 3]
ans: C

## 6 list1 = [11, 2, 23], list2 = [11, 2, 2], list1 < list2结果为？
	 A. True
	 B. False
ans: B

## 7 list1 = [11, 2], list2 = [11, 2, 2], list1 < list2结果为？
	 A. True
	 B. False
ans: A

## 8 list1 = [11, 2, 23] , list2 = [2, 11, 23], list1 == list2结果为？
	 A. True
	 B. False
ans: B

## 9 t = [1, 2, 4, 3], 下列代码执行后的结果分别是什么？
	 A. print(t[3])
	 B. print(max(t))
	 C. print(len(t))
	 D. print(sum(t))
ans:
```bash
    A: 3
    B: 4
    C: 4
    D: 10 
```

## 10.  已经定义了一个列表lst，请问你能想出几种方法来获得该列表的拷贝？
    s = list(range(20))
ans: 

    浅拷贝：
    1) tmp = s
    2) tmp = s[:]
    深拷贝:
    1)
    import copy
    tmp = copy.deepcopy(s)
    1) 
    tmp = []
    for i in range(len(s)):
        tmp.append(s[i])

## 11.  请按照如下步骤写出相应的代码：
    a. data初始化为包含5、3和7的列表
    b. new_data初始化为包含1到20内的奇数的列表
    c. data的第1个元素替换为该元素的相反数
    d. 附加10到data的尾部
    e. 插入22作为data的第3个元素
    f. 删除data中第1个元素，并且将删除的元素输出
    g. 将new_data中的所有值附加到data的尾部
    h. 如果7在data中，则输出7在data中首次出现的位置
    i. 统计7在data出现的次数
    j. data进行原地排序
    k. data进行原地逆序
ans:
```python
    data = list([5, 3, 7]) # a
    new_data = list(range(1,20,2)) # b
    data[0] = -data[0] # c
    data.append(10) # d
    data[2:2] = [22] # e
    data.pop(0) # f
    data[len(data):]=new_data # g
    if 7 in data: # h
        data.index(7)
    data.count(7) # i
    data.sort() # j
    data.reverse() # k
```


## 12. 这道题考察切片出现在赋值语句左边的情况。下面给出了一系列的代码，请在注释行的下面写出相应的赋值语句，列表s的切片出现在赋值语句的左边，以将s的内容进行修改变为注释中给出的列表。如果有可能，尽量采用range函数，切片时尽量使用最小的范围。

```python
s = [2, 4, 6, 8, 10]
# [2, 4, 6, 8, 10, 10, 12, 14, 16, 18, 20]
s[len(s):] = range(10,21,2)
print(s)

s = [2, 4, 6, 8, 10]
# [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
s[0:0] = list(range(-10,1,2))
print(s)

s = [2, 4, 6, 8, 10]
# [2, 4, 6, 'a', 'b', 'c', 8, 10]
s[s.index(6)+1:s.index(8)]='abc'
print(s)

s = [2, 4, 6, 8, 10]
# [2, 4, 9, 7, 5, 3, 1, 10]
s[s.index(6):s.index(8)+1]=range(9,0,-2)
print(s)

s = [2, 4, 6, 8, 10]
# [2, 3, 4, 5, 6, 7, 6, 8, 10]
s[0:s.index(6)]=range(2,8,1)
print(s)

s = [2, 4, 6, 8, 10]
# []
s[:]=[]
print(s)

s = [2, 4, 6, 8, 10]
# [10, 8, 6, 4, 2]
s.reverse()
print(s)

s = [2, 4, 6, 8, 10]
# [2, 4, 6, 8]
s[-1:len(s)]=[]
print(s)

s = [2, 4, 6, 8, 10]
# [2, 10]
s[s.index(2)+1:s.index(10)]=[]
print(s)
```
