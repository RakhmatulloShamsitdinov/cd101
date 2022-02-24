numbers = input("Enter nums using comma: ").split(",")

summ = 0


for z in numbers:
    summ = summ + int(z)**3
print(summ)  
