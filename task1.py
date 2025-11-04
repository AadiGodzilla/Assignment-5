# Takes user input for 'n' elements
n = int(input("Number of items: "))
# List to store those 'n' elements
fruits = []
# For loop that run 'n' number of times
for _ in range(n):
    # takes user input 'item' to be stored in the list 'fruits' in lowercase for each iteration
    item = input("Enter item: ").lower()
    # add 'item' to the 'fruits' list
    fruits.append(item)

# User input for 'search_item' to query the list 
search_item = input("What do you want to search: ").lower()
# find the position of the element of value 'search_item' in the list and display it
print(f"{search_item} is in { fruits.index(search_item)} position",)