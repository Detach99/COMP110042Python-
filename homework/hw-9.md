# homework 9

### 1.  不执行下述代码，请给出两个print函数最后的输出。
```python
month = "June"
day = 5
year = 2011
print("The date is {} {}, {}.".format(month, day, year))
print("{:<15s}: {:>8.1f}".format("Length",23.875))
```
#### ans: 
```bash
data is June 5, 2011.
Length         :    23.9
```

### 2. 我们补充介绍了f-string，请将第1题的最后两个语句改写，不用字符串的format方法，而是采用f-string实现。

#### ans:
```python
f"The date is {month} {day}, {year}."
f"{'Length':<15}:{23.875:>8.1f}"
```

### 3 我们想要输出一张表格，给出了正多边形的各个内角和、每个内角以及每个外外角的度数，下面的代码给出了相应的实现。但是其输出不是那么令人满意，我们希望采用字符串的format方法，修改代码，使得其输出的是一个比较整齐的表格形式，请给出修改后的代码。
```python
print('side', 'total', 'interior', 'exterior')
for n in range(3, 11):
    print(n, 180 * (n - 2), 180 * (n - 2) / n, 360 / n)
```
### 上面的代码输出的部分内容
```bash
side total interior exterior
3 180 60.0 120.0
4 360 90.0 90.0
5 540 108.0 72.0
```
#### 期待输出：

```bash
side   total      interior   exterior
3      180        60.00      120.00
4      360        90.00      90.00
5      540        108.00     72.00
6      720        120.00     60.00
7      900        128.57     51.43
8      1080       135.00     45.00
9      1260       140.00     40.00
10     1440       144.00     36.00
```
#### ans:
```python
print("{:s}\t{:s}\t{:s}\t{:s}".format('side', 'total', 'interior', 'exterior'))
for n in range(3, 11):
    print("{:<2}\t{:<}\t{:<.2f}\t\t{:<.2f}".format(n, 180*(n-2),180 * (n - 2) / n, 360 / n))
```

### 4. 不执行，给出下面两个表达式运算的结果
    (a) "dome" in "seldom errs" 
    (b) "pig" in "pigeonhole"

#### ans:
```bash
False
True
```

### 5. 不执行，给出下面两个表达式运算的结果
```python 
t = "Fun with Python"
#(a) 
t.isalpha()
#(b) 
t[4:8].islower()
#(c)
'\n\n\n'.isspace()
```
#### ans:
```bash
# a
False
# b
True
# c
True
```

### 6. 假设一个句子最后可以包括多个感叹号、问号和点，请给出一条语句，将句子最后的那些感叹号问号和点删除,比如, text为如下的字符串，希望最后得到的字符串为'Hi'
    text="Hi!......"

#### ans;
```python
t = []
for ch in text:
    print(ch)
    if ch not in ".!?":
        t.append(ch)
print(''.join(t))
```
### 7. levels保存了如下的字符串，要对levels进行分割，最终产生如下的列表，请给出相应的代码
    levels = 'Beginner, Average, Advanced, Expert'

#### 产生的列表为 ['Beginner', 'Average', 'Advanced', 'Expert']

#### ans:
```python
new_arr = levels.split(',')
```

### 8. 下面的表达式有没有错误？如果没有错误，给出运算的结果。如果有错误，请尝试改正。
    (a) "".join(["h", "e", "l", "l", "o"])
    (b) " ".join("glue", "these", "words", "together")
    (c) "".join([1, 2, 3, 4])

#### ans:
```bash
# a. 无错
hello
# b. 有错
" ".join(["glue", "these", "words", "together"])
glue these words together
# c.有错
"".join(["1","2","3","4"])
1234
```
