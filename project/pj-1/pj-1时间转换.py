'''
时间转换：将时间间隔转换为天数, 小时和分钟数 
程序完成如下功能：
1. 提示并接收用户输入，假设用户输入的为正整数，不考虑用户输入有误的情形
   请输入时间间隔(分钟):
2. 将分钟转换为天数，小时和分钟数，提示采用求整商和求模运算符,可参考求模的应用中如何获得整数n的各位数字的例子；
3. 输出相应的结果，考虑天数/小时/分钟数可能为0的情形，如果为0，则不输出相应的部分。提示可使用单分支结构的if语句，利用print函数的end参数。
'''

time = int(input("请输入时间间隔(分钟):"))
day = int(time/(24*60))
hour = int((time-day*24*60)/60)
minute = time%60
info = ""
if day:
    info = info+repr(day)+"天"
if hour:
    info = info + repr(hour)+"小时"
if minute:
    info = info + repr(minute)+"分钟"
print(info)