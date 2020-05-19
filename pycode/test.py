#!/usr/bin/python
# -*- coding: utf-8 -*-
import pdb


def bSearch(dataList, startIndex, endIndex, value):
    if startIndex > endIndex:
        return -1

    midIndex = (startIndex + endIndex) // 2

    if value > dataList[midIndex]:
        return bSearch(dataList, midIndex + 1, endIndex, value)
    elif value < dataList[midIndex]:
        return bSearch(dataList, startIndex, midIndex - 1, value)
    else:
        return midIndex


if __name__ == '__main__':
    dataList = [1, 2, 3, 5, 7, 8]
    index = bSearch(dataList, 0, len(dataList) - 1, 1)
    print(index)

    index = bSearch(dataList, 0, len(dataList) - 1, 2)
    print(index)

    index = bSearch(dataList, 0, len(dataList) - 1, 7)
    print(index)

    index = bSearch(dataList, 0, len(dataList) - 1, 8)
    print(index)

    index = bSearch(dataList, 0, len(dataList) - 1, 44)
    print(index)


'''

id(index) name grade(index)


create table sixGrade(
        id int primary key,
        name char(20),
        grade int,
        index gradeIndex grade,

)engine=InnoDB default charset=utf8;


select * from sixGrade order by grade desc;
select * from sixGrade order by id asc;


'''


