if __name__ == "__main__":
    print("可以重复输入, 退出请Ctrl+C")
    try:
        while True:
            index = int(input("请输入pocket编号:"))
            if index == 0:
                color = "绿色"
            elif index < 11 or (index > 18 and index < 29):
                color = "红色" if index%2 else "黑色"
            elif index > 37:
                color = "不在编号内"
            else:
                color = "黑色" if index%2 else "红色"

            print(color)
    except KeyboardInterrupt:
            exit()
