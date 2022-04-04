"""
输入    输出
reset	reset what
reset board	board fault
board add	where to add
board delete	no board at all
reboot backplane	impossible
backplane abort	install first
he he	unknown command
"""


def main():
    cmd_lis = input().split()
    if len(cmd_lis) == 1:
        if cmd_lis[0] in 'reset'[:len(cmd_lis[0])]:
            print('reset what')
        else:
            print('unknown command')
    else:
        flag = 0
        msg = 'unknown command'
        if cmd_lis[0] in 'reset'[:len(cmd_lis[0])] and cmd_lis[1] in 'board'[:len(cmd_lis[1])]:
            flag += 1
            msg = 'board fault'
        if cmd_lis[0] in 'reboot'[:len(cmd_lis[0])] and cmd_lis[1] in 'backplane'[:len(cmd_lis[1])]:
            flag += 1
            msg = 'impossible'
        if cmd_lis[0] in 'board'[:len(cmd_lis[0])] and cmd_lis[1] in 'add'[:len(cmd_lis[1])]:
            flag += 1
            msg = 'where to add'
        if cmd_lis[0] in 'board'[:len(cmd_lis[0])] and cmd_lis[1] in 'delete'[:len(cmd_lis[1])]:
            flag += 1
            msg = 'no board at all'
        if cmd_lis[0] in 'backplane'[:len(cmd_lis[0])] and cmd_lis[1] in 'abort'[:len(cmd_lis[1])]:
            flag += 1
            msg = 'install first'
        if flag >= 2:
            msg = 'unknown command'
        if cmd_lis:
            print(msg)

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            break