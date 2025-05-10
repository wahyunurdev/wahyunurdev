# Define the list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[2:5])
print(thislist[:-2])
print(thislist[-1:])

# Display the full list with formatting
print("🍎 Full List of Fruits:")
print(", ".join(thislist))

# Display a slice of the list
print("\n🍒 Fruits from index 2 to 4 (inclusive):")
print(", ".join(thislist[2:5]))

# Display the second-to-last item
print("\n🍈 Second-to-last fruit in the list:")
print(thislist[-2])

# Display the last item
print("\n🥭 Last fruit in the list:")
print(thislist[-1])

# Additional feature: Count the total number of fruits
print("\n📊 Total number of fruits in the list:")
print(len(thislist))