# inner module
import hashlib

# custom module
from conf import setting
from lib import common

status_dic = {
    'username': None,
    'status': False,
}
flag = True


def get_md5(password):
    gmd5 = hashlib.md5()
    gmd5.update(password.encode('utf-8'))
    return gmd5.hexdigest()


def register():
    with open(setting.register_path, 'r', encoding='utf-8') as f1:
        dic = {i.strip().split('|')[0]: i.strip().split('|')[1] for i in f1}
        #print(dic)
    while 1:
        print('\033[1;45m 欢迎来到注册页面 \033[0m')
        username = input("请输入用户名： ").strip()
        if not username.isalnum():
            print('\033[1;31;0m 用户名有非法字符，请重新输入 \033[0m')
            continue
        if username in dic.keys():
            print('\033[1;31;0m 用户名已经存在，请重新输入 \033[0m')
            continue
        password = input("请输入密码： ").strip()
        if 3 < len(password) <= 14:
            password = get_md5(password)
            with open(setting.register_path, 'a', encoding='utf-8') as f2:
                f2.write('\n{}|{}'.format(username, password))

                status_dic['username'] = str(username)
                status_dic['status'] = True
                print('\033[1;32;0m 恭喜您，注册成功！已帮您成功登录~ \033[0m')
                return True
        else:
            print('\033[1;31;0m 密码长度超出范围，请重新输入 \033[0m')


def login():
    i = 0
    with open(setting.register_path, encoding='utf-8') as f1:
        dic = {i.strip().split('|')[0]: i.strip().split('|')[1] for i in f1}
        #print(dic)
    while i < 3:
        username = input('请输入用户名：').strip()
        password = get_md5(input('请输入密码：').strip())

        if username in dic and dic[username] == password:
            print('登录成功')
            status_dic['username'] = str(username)
            status_dic['status'] = True
            return True
        else:
            print('用户名密码错误，请重新登录')
            i += 1




@common.auth
def article():
    print("\033[1;32;0m 欢迎{}访问文章页面\033[0m".format(status_dic["username"]))


@common.auth
def diary():
    print("\033[1;32;0m 欢迎{}访问日记页面\033[0m".format(status_dic["username"]))


@common.auth
def comment():
    print("\033[1;32;0m 欢迎{}访问评论页面\033[0m".format(status_dic["username"]))


@common.auth
def enshrine():
    print("\033[1;32;0m 欢迎{}访问评论页面\033[0m".format(status_dic["username"]))


def login_out():
    status_dic['username'] = None
    status_dic['status'] = False
    print('\033[1;32;0m 注销成功 \033[0m')


def exit_program():
    global flag
    flag = False
    return flag


choice_dict = {
    1: register,
    2: login,
    3: article,
    4: diary,
    5: comment,
    6: enshrine,
    7: login_out,
    8: exit_program,
}


def run():


    while flag:
        print('''
        欢迎来到博客园首页
        1:请注册
        2:请登录
        3:文章页面
        4:日记页面
        5:评论页面
        6:收藏页面
        7:注销
        8:退出程序''')

        choice = input('请输入您选择的序号:').strip()
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(choice_dict):
                choice_dict[choice]()
            else:
                print('\033[1;31;0m 您输入的超出范围，请重新输入 \033[0m')
        else:
            print('\033[1;31;0m 您您输入的选项有非法字符，请重新输入 \033[0m')


