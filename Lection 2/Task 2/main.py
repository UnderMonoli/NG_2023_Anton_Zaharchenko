number_list = []
a = int(input("Enter the list size "))

print("\n")
for i in range(0, a):
    print("Enter your number ", i, ":")
    item = input()

    if item.isnumeric():
        number_list.append(int(item))
    else:
        print(f"'{item}' is not number and will be ignored.")

print("User list has numeric elements", number_list)