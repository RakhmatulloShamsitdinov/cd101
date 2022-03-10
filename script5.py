user_info = input("name, age, 0 or 1: ").split(' ')
if user_info[2] == '1':
    if int(user_info[1]) >= 18:
        print('Your cigs')
    else:
        print("not allowed")
else:
    print("your coffe")