#课后作业1
# name = input("请输入姓名：")
# age = input("请输入年龄：")
# sex = input("请输入性别:")
# print("*"*20)
# print('''
# 姓名：{0}
# 性别：{2}
# 年龄：{1}
# '''.format(name,age,sex))
# print("*"*20)

#课后作业2
# str1 = 'python hello aaa 123123aabb'
# print(str1[:6:])
# print('o a' in str1)
# print('he' in str1)
# print('ab' in str1)
# print(str1.replace('python','lemon'))
# print(str1.index('aaa'))

# list1 = ['andy',52.36,'接口',74,[4,52,65,8],False]
# print(list1.append(45))
# print(list1.insert(2,'插入'))
# print(list1.extend([10,'jk']))
# print(list1[4][0])

# dict1 = { "type":"bottle","price":"30","rom":"500" }
# print(dict1["rom"])
# print(dict1.get("type"))

# score = int(input("请输入分数："))
# if score >= 90:
#     print("您的等级为：A")
# elif score >= 80:
#     print("您的等级为：B")
# elif score >= 70:
#     print("您的等级为：C")
# elif score >= 60:
#     print("您的等级为：D")
# else:
#     print("不及格！")

#课后作业1
# a = [1,2,'6','summer']
# print('i' in a)

#课后作业2
# dict_1 = {"class_id": 45, "num": 20}
# if dict_1["num"] > 5:
#     print("班级上课人数为{}".format(dict_1["num"]))

#课后作业3
# list3 = ['菠萝','球球','Lewis','瓜瓜']
# dict1 = {"name":"菠萝","性别":"famale","年龄":20}
# dict2 = {"name":"球球","性别":"famale","年龄":27}
# dict3 = {"name":"Lewis","性别":"male","年龄":30}
# dict4 = {"name":"瓜瓜","性别":"famale","年龄":25}
# list_all = [dict1,dict2,dict3,dict4]
# print(list_all)

# list3 = ['菠萝','球球','Lewis','瓜瓜']
#
# dict1 = dict(name="菠萝","性别":"famale","年龄":20)
# dict2 = {"name":"球球","性别":"famale","年龄":27}
# dict3 = {"name":"Lewis","性别":"male","年龄":30}
# dict4 = {"name":"瓜瓜","性别":"famale","年龄":25}
#
# print(list_all)

# count = 0
# list1 = ['菠萝','球球','Lewis','瓜瓜']
# for people in list1:
#     print(people)
#     print("------")
#     count += 1
# print(count)
# print(len(list1))

# for num in range(10,60,13):
#     print(num)
#     print('---')

# count = 0
# list1 = ['菠萝','球球','Lewis','瓜瓜']
# for people in list1:
#     if people == 'Lewis' :
#         break     #退出整个循环
#         continue    #退出当前本次循环
#     count += 1
#     print(people)
# print(count)
# print(len(list1))

# def visitor_flow(line,entity,free=10,*args):
#     print("*args的值是：{}".format(args))
#     total = line+entity+free
#     for i in args:
#         total += i
#     print("当日人流量为：{}".format(total))
# visitor_flow(200,450,60,20,10)

#day4课后作业1
# str1 = "today is Thursday"
# print(list(str1))

#day4课后作业2
# def add_fun(num):
#     sum1 = 0
#     # num = int(input("请输入个数："))
#     for i in range(num):
#         sum1 += i
#     print("生成的整数序列和为：{}".format(sum1))
#
# add_fun(8)


#day4课后作业3
# def mean(obj1):
#     if type(obj1) == list:
#         print("该对象数据类型为列表")
#         if len(obj1) > 5:
#             return True
#         else:
#             return False
#     elif type(obj1) == dict:
#         print("该对象数据类型为字典")
#         if len(obj1) > 5:
#             return True
#         else:
#             return False
#     elif type(obj1) == str:
#         print("该对象数据类型为字符串")
#         if len(obj1) > 5:
#             return True
#         else:
#             return False
#
#
# a = ["jkks",145,"加看看",20,89]
# b = {"name":"yying","age":21,"height":160}
# c = "have a good day"
# result = mean(c)
# print(result)

