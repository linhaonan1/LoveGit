import datetime
import os
import asyncio

# from heavy import special_commit


def modify():
    file = open('F:\LoveGit\zero.md', 'r')
    flag = int(file.readline()) == 0
    file.close()
    file = open('F:\LoveGit\zero.md', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()


def commit():
    # os.sysytem = C语言system()
    os.system('git commit -a -m "test"')


async def set_sys_time(year, month, day):
    # date -s Linux修改时间方法
    # Windows 查看Dos命令
    await os.system('date')
    os.system('%04d-%02d-%02d' % (year, month, day))


def trick_commit(year, month, day):
    print(year, month, day)
    set_sys_time(year, month, day)
    modify()
    commit()


def daily_commit(start_date, end_date):
    for i in range((end_date - start_date).days + 1):
        cur_date = start_date + datetime.timedelta(days=i)
        trick_commit(cur_date.year, cur_date.month, cur_date.day)


if __name__ == '__main__':
    daily_commit(datetime.date(2019, 4, 13), datetime.date(2019, 5, 16))
