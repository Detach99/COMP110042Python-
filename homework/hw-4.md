# homework 4

## 1) 执行代码 list("abcd")后产生的list是什么？
	 A. ['a', 'b', 'c', 'd']
	 B. ['ab']
	 C. ['cd']
	 D. ['abcd']
> ans: A
## 2) 假设list1 = [1, 3, 2, 4, 5, 2, 1, 0], 请问list1[-1]为
	 A. 3
	 B. 5
	 C. 1
	 D. 0
> ans: D
## 3) 下列代码输出是什么？
list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)

	 A. [1, 3]
	 B. [4, 3]
	 C. [1, 4]
	 D. [1, 3, 4]
>ans: B
## 4) 下列代码输出是什么？

```python    
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(m[0][0])
```
	 A. 1
	 B. 2
	 C. 4
	 D. 7
>ans: A

## 5） 假设 m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 请问len(m)和len(m[0])的结果是什么？
	 A. 0
	 B. 1
	 C. 2
	 D. 3
	 E. 4
> ans: D;D

## 6) 下列代码产生的list是什么？
    list(range(5))
    list(range(1, 5))
    list(range(1, 10, 3))
    list(range(12, 5, -2))
> ans:
> 
> list(range(5)) -------------> [0, 1, 2, 3, 4]
> 
> list(range(1, 5)) -----------> [1, 2, 3, 4]
> 
> list(range(1, 10, 3)) -------> [1, 4, 7]
> 
> list(range(12, 5, -2)) ------> [12, 10, 8, 6]


# 7) 添加5到list1末尾，应该：
	 A. list1.add(5)
	 B. list1.append(5)
	 C. list1.addLast(5)
	 D. list1.append([5])
>ans: B

# 8) 插入5到list1的第3个元素处，应该：
	 A. list1.insert(3, 5)
	 B. list1.insert(2, 5)
	 C. list1.add(3, 5)
	 D. list1.append(3, 5)
> ans: A

# 9) 假设list1=[3, 4, 5, 20, 5, 25, 1, 3]list1=[3, 4, 5, 20, 5, 25, 1, 3],  执行list1.extend([34, 5])后list1结果为 
	 A. [3, 4, 5, 20, 5, 25, 1, 3, 34, 5]
	 B. [1, 3, 3, 4, 5, 5, 20, 25, 34, 5]
	 C. [25, 20, 5, 5, 4, 3, 3, 1, 34, 5]
	 D. [3, 4, 5, 20, 5, 25, 1, 3, [34, 5]]
> ans : A

# 10) 假设list1 = [1, 3, 2], 请问 list1 * 2为
	 A. [2, 6, 4]
	 B. [1, 1, 3, 3, 2, 2]
	 C. [1, 3, 2, 1, 3, 2] 
	 D. [1, 3, 2, 3, 2, 1]
> ans: C

## 11) 假设list1 = [1, 3, 2],  list2 = [7, 6, 8] 请问 list1  + list2为
	 A. [1, 3, 2, 7, 6, 8]
	 B. [7, 6, 8, 1, 3, 2]
	 C. [1, 3, 2, [7, 6, 8]] 
	 D. [7, 6, 8, [1, 3, 2] ]
> ans:  A

# 12)  下列代码的输出是什么？
    list1 = list(range(1, 10, 2))
    list2 = [] + list1
    list1[0] = 111
    print(list1)
    print(list2)
>ans: 
> 
> list1: [111, 3, 5, 7, 9]
> list2: [1, 3, 5, 7, 9]

# 13)  课堂上我们介绍过可以使用下标来访问可迭代对象中的元素，如下所示：
```python
s = list(range(0,20,2))
for i in range(len(s)):
    print(i + 1, s[i])
```

    如果要通过下标逆序访问，应该怎么实现？即输出：
    1  倒数第1个元素
    2  倒数第2个元素

> ans:
```python
    s = list(range(0,20,2))
    for i in range(len(s)-1,-1,-1):
        print(i, s[i])
```