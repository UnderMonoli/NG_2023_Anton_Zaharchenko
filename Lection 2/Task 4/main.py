list1 = []
n = (int(input("Enter the list size ")))

print("\n")
for i in range(0, n):
    print(f"Enter your english word at index {i}:")
    item = input()
    if item.isalpha():
        list1.append(item)
    else:
        print(f"'{item}' is not word and will be ignored.")

for word in list1:
    vowels = "aeiouAEIOU"
    consonants_count = sum(1 for letter in word if letter.isalpha() and letter not in vowels)
    print(f"Vomels in '{word}': {consonants_count}")