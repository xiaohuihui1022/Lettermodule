import os               # 检查pwd.txt
import sys              # 退出程序（直接用exit()在pyInstaller容易出事


def answerCheck(answer, rows):  # 检查答案函数
    if answer == "":  # 没任何答案
        print("所给参数错误，此参数针对此密码无任何可能性。")
        main()
    elif len(answer) == 5:  # 答案必定是5位英文字母，所以length = 5
        print("答案:" + answer)
        print("答案已浮现，请结束本程序。若答案错误请接着检索。")
        main()
    elif rows == 5 and len(answer) != 5:  # 如果第五列了答案还是多个，就说明参数错了或者有多个答案
        print("答案仍未浮现，可能是所给参数错误，正在重启程序。")
    else:
        print("当前可能的答案:\n" + answer)    # 上述情况都不是，直接打印


def rowCheck(row):
    if len(row) != 11:
        print("所给字母不为6个")  # 检查用户输入函数
        main()


def pwdCheck(pwdDir):
    if not os.path.exists(pwdDir):
        print("密钥文本不存在，请放入密钥文本再启动程序。")  # 检查密钥文本函数
        sys.exit()


def main():
    pwdCheck(".\\pwd.txt")                  # 先检查密钥文本
    f = open('.\\pwd.txt')                  # 再读取文件
    APwd = f.read().split("\n")             # 本来是分了A-E5个pwd列表，但实际上用不了这么多，一个就够
    for n in range(5):                      # 先整体循环，5代表一共5列所以循环5次
        a1 = ""                             # 定义答案（也是a-e5个字符串但是没用这么多，a=answer）
        Row = input("请输入第" + str(n + 1) + "列的\"所有\"字母(共6个):")  # 用户输入
        rowCheck(Row)                       # 检查用户输入
        for i in range(len(APwd)):          # 大循环找单词
            for r in range(len(Row) - 5):   # 小循环找字母(-5是因为要把5个逗号的位置减去)
                if APwd[i][n].find(Row.split(",")[r]) == 0:  # APwd为35单词列表 [i]精确单词 [n]精确字母 ==0代表找到了
                    if a1 == "":            # 如果a1是空的字符串（就是a1没写入任何东西，以下代码仅为美观作用）
                        a1 = APwd[i]        # 直接赋值答案单词
                        break               # break为了防止用户输入同一个（比如输入6个a就会打印6次），也可以起到优化作用
                    else:                   # 如果a1不是空的字符串
                        a1 = a1 + "\n" + APwd[i]    # a1后边加换行符追加答案单词
                        break               # break作用同上
        answerCheck(a1, n)                  # 检查一下答案
        APwd = a1.split("\n")               # 重新赋值当前答案开始下一次循环


if __name__ == '__main__':
    print("5列每一列字母每一个都用英文逗号“,”隔开、小写，不带任何空格，每一列共6个")
    print("若第一列所有字母为a e i o u q，那就这样写在程序里:a,e,i,o,u,q")
    main()
# BV1r7411x76e: 1:13:58, 1:17:00, 1:41:00
