#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
import project7_util as util

def get_class_sheet(total=25):
    """ 获得某个班级的学生成绩单，学生总人数total缺省为25人，最终返回生成的成绩单。
    采用dict来纪录学生成绩单，包含唯一标识学生的ID、姓名和期末考试成绩，具体而言
    key为学生的ID，value为[姓名,成绩]，比如{285:['Stone', 99], 297:['Idle', 90]}
    可以调用上面提供的get_id()、get_name()、get_score来随机生成学生的相关信息。
    """
    # 初始化class_sheet
    class_sheet = dict()
    for _ in range(total):
        class_sheet[util.get_id()]=[util.get_name(), util.get_score()]
    return class_sheet


def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    print("{}\t{}\t\t{}".format("ID","Name", "Score"))
    for stu in sorted(class_sheet):
        if len(class_sheet[stu][0]) == 8:
            print("{:<d}\t{:<s}        {:<d}".format(stu, class_sheet[stu][0],class_sheet[stu][1]))
        else:
            print("{:<d}\t{:<s}\t\t{:<d}".format(stu, class_sheet[stu][0],class_sheet[stu][1]))

def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    print("{}\t{}\t\t{}".format("ID","Name", "Score"))
    for stu in sorted(class_sheet.items(), key = lambda item: item[1][1]):
        if len(stu[1][0]) == 8:
            print("{:<d}\t{:<s}        {:<d}".format(stu[0], stu[1][0],stu[1][1]))
        else:
            print("{:<d}\t{:<s}\t\t{:<d}".format(stu[0], stu[1][0],stu[1][1]))

    
def main():
    class_sheet = get_class_sheet(10)

    print()
    print('成绩单如下，按照ID排序\n')
    print_class_sheet(class_sheet)

    print()
    print('-'*50)
    print()
    print('成绩单如下，按照成绩排序\n')

    print_class_sheet_sorted(class_sheet)

if __name__ == '__main__':
    main()
