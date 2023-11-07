for variable in sequence:
    # Code to execute inside the loop

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


while condition:
    # Code to execute inside the loop

count = 0
while count < 5:
    print(count)
    count += 1

for number in range(1, 6):
    if number == 3:
        break
    print(number)

for number in range(1, 6):
    if number == 3:
        continue
    print(number)
