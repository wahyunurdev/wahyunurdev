# Step 1: Declare the list to store item names
itemNames = []

# Step 2: Declare the while loop for user input
while True:
    name = input("Enter the item's name (Enter key to exit): ")

    # Step 3: Exit condition for the loop (empty input)
    if name == '':
        break

    # Add the name to the list
    itemNames.append(name)

# Step 4: Output all the items entered
print("Item’s Name:")
for name in itemNames:
    print(name, end=", ")