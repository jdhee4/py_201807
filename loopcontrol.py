# num = 1
# while True:
#     print(num)
#     num += 1

# message =''
# while message != 'q':
#     message = input("typing your message:")
#     print(">" + message)

# message =''
# while True :
#     message = input("typing your message:")
#     print(">" + message)
#     if message == 'q' :
#         break

num = 0
while num < 100:
    num += 1
    if num%2 == 0:
        continue        
    print(num)