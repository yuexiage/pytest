# for i in range(1, 10):
#     print('当前值为：' + str(i))
# list_range = list(range(1, 100, 5))
# list_range.insert(2, 'aaaaaaaaaaaa')
# print(list_range)
# list_range.remove('aaaaaaaaaaaa')
# print(list_range)
squares = []
# for i in range(1, 100000000, 5000000):
#     print(i)
# print(squares)
# print(min(squares))
# print(max(squares))
# print(sum(squares))
squares = [value**2 for value in range(1, 11)]
# print(squares)
# print(squares[-5:-1])
# s = 'abcdefghigklimn'
# print(s[:3])
# for i in squares[:3]:
#     print(i)
# print(squares)
# # 引用
# squares2 = squares
# # 复制
# squares2 = squares[:]
# print(squares2)
# squares2.append('aa')
# print(squares)
# print(squares2)
# dimensions = (1, '2', '3', [1, 2, 3], [1, '2', 3], 9, 9)
# print(dimensions[0])
# print(type(dimensions))
# for i in dimensions:
#     print(type(i))
# dimensions = (1,)
# info_tuple = "小马", 21, 180
# print(dimensions.count(9))
# print(type(info_tuple))
# info_tuple = "小马", 21, 180
# print('将要输出第一个内容%s 和第二个内容 %d 和第三个内容 %d' % info_tuple)
# car = 'A'
# print(car.lower() == 'a')
# if 'a' == 'a' or 'b' == 'B':
#     print(1)
# else:
#     print(2)
# str_info = 'abcdefg'
# print(tuple(str_info))
# if ( 'b' in tuple(str_info) ):
#     print(1)
