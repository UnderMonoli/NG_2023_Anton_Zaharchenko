number = int(input("Enter number "))

numbers = []
dividers = []

for i in range (1, number + 1):
    numbers.append(i)
    current_dividers = []
    for j in range (1, i + 1):
        current_dividers.append(j)
        dividers.append(current_dividers)

print("Number | divider")
print("-----------")
for i in range(number):
    print(f"'{numbers[i]:^6}' | {dividers[i]}")

simple_number = []
for i in range(2, number + 1):
    current_dividers = []
    for j in range(1, i + 1):
        if i % j == 0:
            current_dividers.append(j)
if len(current_dividers) == 2:
    simple_number.append(i)

print("Simple numbers for", number, ":", simple_number)
