
car = ['honda', 'lamborghini', 'mazda']

# del car[0]
# del_car = car.pop(2)
# print(car)
# print(del_car.title())
del_car = 'honda'
car.remove(del_car)
print(car)

car = ['honda', 'lamborghini', 'mazda']
print(car)
# car.sort(reverse=True)
# print(car)
# print(sorted(car))
#
# car.reverse()
# print(car)
dlina = len(car)
print(dlina)

car = ['honda', 'lamborghini', 'mazda']
print(car)
for i in car:
    print(f"я хочу такую машну под маркой {i.title()}")
    print(f"\t\t-{i.title()} крутая тачка\n")