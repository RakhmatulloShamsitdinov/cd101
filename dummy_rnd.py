# import random 

# rnd_id = None

# for i in range(10):
#     rnd_id = str(random.randint(0,100)) + str(rnd_id)
# print(rnd_id)
import random 

def generate_id(count)
rnd_id = 0
for i in range(count):
    rnd_id = str(random.randint(0,9)) + str(rnd_id)
return rnd_id
def greet(name):
    print(f"Hey,{name}")