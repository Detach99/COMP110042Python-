# Homework8
## 1. 假设text='abcd 12345',请用列表推导式实现返回一个包含了每个字符的ASCII码的列表，该列表应该为：
	[97, 98, 99, 100, 32, 49, 50, 51, 52, 53]
> [x for x in [97,98,99,100,32,49,50,51,52,53]

## 2. 我们在课堂上介绍过如何获得一个正整数的各位数字，也可以采取另外一种方法，首先通过str函数将其转换为字符串，接下来可以使用列表推导式获得其各位数字，请给出具体的实现方法。 假设 n = 123456，你的列表推导式实现得到的新列表应该是 
	[1, 2, 3, 4, 5, 6]
```python
n = 123456
l = str(n)
print([num for num in l])
```
## 3.  下列代码执行完后的输出是什么？
```python
values = [[3, 4, 5, 1], [33, 6, 1, 2]]

v = values[0][0]
for row in range(0, len(values)):
    for column in range(0, len(values[row])):
        if v < values[row][column]:
            v = values[row][column]

print(v)
```
	A. 1
	B. 3
	C. 5
	D. 6
	E. 33
> E

## 4. 下列代码执行完后的输出是什么？
```python
matrix = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]

for i in range(0, 4):
    print(matrix[i][1], end = " ")
```
	A. 1 2 3 4
	B. 4 5 6 7
	C. 1 3 8 12
	D. 2 5 9 13
	E. 3 6 10 14
> D

## 5.  假设d = {"tom":"john", "peter":45},  "john" in d 的结果为?  
> False

## 6.  假设 d1 = {"john":40, "peter":45} , d2 = {"john":466, "peter":45}, d1 == d2 的结果为？
> False

## 7.  假设 d1 = {"john":40, "peter":45} , d2 = {"john":466, "peter":45}, d1 > d2 的结果为？
	 A. True
	 B. False
	 C. 异常
> C

## 8.  假设d = {"john":40, "peter":45},  d["john"] =？
> 40

## 9.  假设d = {"john":40, "peter":45},  要删除 "john":40, 写出相应的语句。
> d.pop("john")

## 10.  假设d = {"john":40, "peter":45}, 要知道字典有多少项，写出相应的语句。
> len(d)

## 11. 下列代码执行后输出为？
```python
d = {"john":40, "peter":45}
print(list(d))
```
> ['john', 'peter']

## 12.  假设d = {"john":40, "peter":45}, 执行语句s = d[45]后 s的值是？
	 A. "peter"
	 B. None
	 C. 抛出异常KeyError
	 D. 语法错
> C

## 13.  假设d = {"john":40, "peter":45},请按照如下步骤写出相应的代码：
	a. 修改key为"peter"对应的值，使得其为原来的值的负数
	b. 增加一个元素到d中，其中key为'tony'，value为50
	c. 写一个循环，输出字典d的所有元素，每行有两列，第1列为字典d的key，第2列为key所映射的value
	d. 询问用户并得到用户的输入，提示符为 请输入待删除的key
	e. 根据步骤d的输入，删除对应的元素，同时显示该key所映射的值，如果没有对应的元素，则显示 key不存在

> ans:
```python
d = {"john":40, "peter":45}
# a. 修改key为"peter"对应的值，使得其为原来的值的负数
d['john']=-d['john']
#	b. 增加一个元素到d中，其中key为'tony'，value为50
d['tony']=50
#	c. 写一个循环，输出字典d的所有元素，每行有两列，第1列为字典d的key，第2列为key所映射的value
for item in d:
	print(item, d[item])
#	d. 询问用户并得到用户的输入，提示符为 请输入待删除的key
rm = input("请输入待删除的key:\t")
#	e. 根据步骤d的输入，删除对应的元素，同时显示该key所映射的值，如果没有对应的元素，则显示 key不存在
if rm in d:
	d.pop(rm)
else:
	print(rm+"不存在")

```