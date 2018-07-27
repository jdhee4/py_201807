# 로또번호는 1~46, 총 6개 당첨번호

# import random
# today = []
# today = random.sample(range(1,47), 6)

# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))

# print("오늘의 추천번호는 "
# + str(today[0]) + ", "
# + str(today[1]) + ", "
# + str(today[2]) + ", "
# + str(today[3]) + ", "
# + str(today[4]) + ","
# + str(today[5]) + " 입니다.")

# import random
# today = []
# start = 0
# while start<6:
#     today.append(random.sample(range(1,47), 1))
#     start += 1
# print(today)


import random
today = []
#for num in range(0,6):
#    today.append(random.sample(range(1,47), 1))
today.append(random.sample(range(1,47), 6))
print(today)

