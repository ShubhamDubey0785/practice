salary = float(input("current salary"))
year = float(input("year of experience"))
if year > 5:
    salary = salary + 1000
else:
    print("same salary")
print(salary)