'''
Date: 2020-01-15 16:16:13
LastEditors: Lonel Vino
LastEditTime: 2020-11-01 21:59:14
'''
import datetime
import os
import asyncio

# from heavy import special_commit


def modify():
  file = open(r'C:\Users\lenovo\Desktop\zero.md', 'r')
  flag = int(file.readline()) == 0
  file.close()
  file = open(r'C:\Users\lenovo\Desktop\zero.md', 'w+')
  if flag:
    file.write('1')
  else:
    file.write('0')
    file.close()


def commit():
    # os.sysytem = C语言system()
    os.system('git commit -a -m "test"')


def set_sys_time(day, month, year):
    # date -s Linux修改时间方法
    # Windows 查看Dos命令
    print('date %02d-%02d-%04d' % (day,month,year))
    os.system('date %02d-%02d-%04d'  % (day, month, year))


def trick_commit(day, month, year):
    print(day, month, year )
    set_sys_time(day, month, year)
    modify()
    commit()


def daily_commit(start_date, end_date):
    for i in range((end_date - start_date).days + 1):
        cur_date = start_date + datetime.timedelta(days=i)
        trick_commit(cur_date.day, cur_date.month, cur_date.year)


if __name__ == '__main__':
    j = datetime.date(2020, 9, 16) - datetime.date(2020,4,14)
    print(j.days)
    i = datetime.date(2020, 4, 14) + datetime.timedelta(days=j.days)
    print(i.day,i.month,i.year)
    daily_commit(datetime.date(2020, 4, 13), datetime.date(2020, 9, 16))
