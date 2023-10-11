number_list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter your number at index", i, ":")
    item = input()

    if item.isnumeric():
        number_list.append(int(item))
    else:
        print(f"'{item}' is not number and will be ignored.")

print("User list has numeric elements", number_list)