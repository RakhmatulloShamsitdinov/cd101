import random
def generation_id(count):
    rnd_id = 0
    for i in range(count):
        rnd_id = str(random.randint(1,100)) + str(rnd_id)
    return rnd_id
# r_id = generation_id(10)


customers = [{"id": "1212", "name": "akmal","age":23, "prods": ["water"]}, {"id": "12121", "name": "roma","prods": ["cola"]}]
g = input('Do you want to buy something? ')
while g == 'Yes' or g == 'yes':
    prov = input("do you have an account? ")
    if prov == "yes" or prov == "Yes":
        prov_id = input('Enter your id: ')
        if prov_id == 'exit':
            break
        for x in customers:
            if prov_id == x["id"]:
                new_prods= input("Choice a product: ")
                x["prods"].append(new_prods)
                with open("text.txt", 'w') as f:
                    f.write(f"{customers}\n")
                    f.close()
                print(customers)
        else:
            print("error!! Please enter correct id! ")

    elif prov == "No" or prov == "no":
        cust_new = {}
        cust_new["id"] = generation_id(12)
        cust_new["name"] = input("Enter a name: ")
        cust_new["age"] = int(input("Enter your age: "))
        cust_new["prods"] = input("Choice a product: ").split(", ")
        customers.append(cust_new)
        print(customers)
        f=open("text.txt", 'w')
        for cust_new in customers:
             f.write(f"{cust_new}\n")
        f.close()
    elif prov == "exit":
        break


