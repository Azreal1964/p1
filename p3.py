nums = [12, 45, 7, 23, 45, 89]
nums.append(66)
nums.remove(45)
nums[2] = 99
for i in nums:
    print(i)
t = ("apple", "banana", "orange")
print(t[1])
lst = list(t)
print(lst)
data = [2,3,2,5,6,3,7,5,9]
s = set(data)
new_lst = sorted(s)
print(new_lst)
score = {"张三":88, "李四":76, "王五":92}
print(score["李四"])
score["赵六"] = 81
score["张三"] = 90
del score["王五"]
for k, v in score.items():
    print(k, v)
s = "apple banana apple orange banana apple"
words = s.split()
word_count = {}
for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1
print(word_count)
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a & b) # 交集
print(a | b) # 并集
print(a - b) # a独有
arr = [34, 7, 19, 82, 5, 41]
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)
print(arr[:3])
users = [("小明", 18, "男"), ("小红", 17, "女"), ("小明", 18, "男")]
unique_user = set(users)
user_dict = {}
for name, age, gender in unique_user:
    user_dict[name] = (age, gender)
for k, v in user_dict.items():
    print(f"姓名:{k}, 年龄:{v[0]}, 性别:{v[1]}")
