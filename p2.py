import random

def guess_number():
    secret = random.randint(1, 100)
    print("猜数字游戏！数字范围1~100")
    while True:
        num = int(input("请输入猜测数字："))
        if num > secret:
            print("猜大了")
        elif num < secret:
            print("猜小了")
        else:
            print("猜对了！")
            break

guess_number()

def nine_table():
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f"{j}*{i}={i*j}", end="\t")
        print()

nine_table()

def score_level():
    score = int(input("输入成绩："))
    if score >= 90:
        level = "优"
    elif score >= 80:
        level = "良"
    elif score >= 70:
        level = "中"
    elif score >= 60:
        level = "及格"
    else:
        level = "不及格"
    print("等级：", level)

score_level()

def is_prime():
    n = int(input("请输入整数："))
    prime_flag = True
    if n <= 1:
        prime_flag = False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                prime_flag = False
                break
    if prime_flag:
        print(f"{n} 是素数")
    else:
        print(f"{n} 不是素数")

is_prime()

def print_even():
    print("1~100的偶数：")
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, end=" ")

print_even()