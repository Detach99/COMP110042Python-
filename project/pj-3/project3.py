#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import project3_util as util


if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print()
    print('总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)

    # 你编写的代码放在后面
    n = len(exam_scores)
    exam_scores.sort(reverse=True)
    top_ten = exam_scores[:10]
    bottom_ten = exam_scores[-11:-1:1]
    avg = round(sum(exam_scores)/n, 1)
    if n % 2: # odd
        medium = exam_scores[int((n+1)/2)-1]
    else:
        medium = (exam_scores[int(n/2)-1]+exam_scores[int(n/2)])/2
    medium = round(medium, 1)
    print("排名前十为:\n {0}\n排名后十为:\n{1}\n平均成绩为:{2}\n中位数为:{3}".format(top_ten, bottom_ten, avg, medium))


