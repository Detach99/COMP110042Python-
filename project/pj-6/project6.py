#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

def chick_calc( ):
    """ 今有鸡翁一，值钱伍；鸡母一，值钱三；鸡雏三，值钱一。凡百钱买鸡百只，
    问鸡翁、母、雏各几何？ 出自《张邱建算经》
    """
    solutions = []
    for rooster in range(21):
        for hen in range(34):
            for chick in range(0,100,3):
                num = rooster+hen+chick
                price = rooster*5 + hen*3 + chick/3
                if price == 100 and num==100:
                    solutions.append([rooster, hen, chick])
    return solutions
    
def chick_calc_comphrehension( ):
    """ 今有鸡翁一，值钱伍；鸡母一，值钱三；鸡雏三，值钱一。凡百钱买鸡百只，
    问鸡翁、母、雏各几何？ 出自《张邱建算经》
    """
    solutions=[(rooster, hen, chick) for rooster in range(21) 
                                                                  for hen in range(34) 
                                                                  for chick in range(0,100,3) 
                                                                  if 5*rooster+3*hen+chick/3 ==100 and rooster+hen+chick==100]                                   
    return solutions

def print_solutions(solutions):
    """ solutions里面保存了之前找到的所有解，按照指定格式输出这些解
    """
    print("总共{}个解".format(len(solutions)))
    for i in range(len(solutions)):
        print("解{0}:鸡翁 {1} 鸡母 {2} 鸡雏 {3}".format(i, solutions[i][0], solutions[i][1],solutions[i][2]))

if __name__ == '__main__':
    solutions = chick_calc()
    print_solutions(solutions)
    
    print()
    solutions = chick_calc_comphrehension()
    print_solutions(solutions)
