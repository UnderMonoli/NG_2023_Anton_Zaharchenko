number_list=[]
Size_list=(int(input("Enter the list size ")))

print("\n")
for i in range(0, Size_list): 
    item = input(f"Enter your elements {i}: ")
    number_list.append(item)

unique_elements = list(set(number_list))

print("User list with unique elements is ", unique_elements)