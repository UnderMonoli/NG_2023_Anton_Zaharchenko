number_list=[]
n=(int(input("Enter the list size ")))

print("\n")
for i in range(0,n):
    print("Enter your number at index", i, ":")
    item = int(input())
    number_list.append(item)

unique_elements = list(set(number_list))

print("User list with unique elements is ", unique_elements)