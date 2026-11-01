# import random
# def c():
#     a = random.randint(1, 100)
#     print("猜数字:")
#     while True:
#         try:
#             b = input("请输入你猜的数字：")
#             g = int(b)
#             if g < 1 or g > 100:
#                 print("数字范围在1~100")
#                 continue
#             if g < a:
#                 print("小了")
#             elif g > a:
#                 print("大了")
#             else:
#                 print("猜对了")
#                 break
#         except ValueError:
#             print("请重新输入")
#
# if __name__ == "__main__":
#     c()

# def a(n=9):
#     for i in range(1, n+1):
#         b = ""
#         for j in range(1, i+1):
#             b += f"{j}*{i}={i*j}\t"
#         print(b)
#
# if __name__ == "__main__":
#     a()

# def a(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 60:
#         return "C"
#     else:
#         return "D"
#
# if __name__ == "__main__":
#     print(a(85))
#     print(a(59))

