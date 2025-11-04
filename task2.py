# Result Dictionary
results = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92
}
# Total Result variable
total = 0

# For loop running for each key and value in the result dictionary
for key, value in results.items():
    # Display Name and Mark of each student
    print(f"Name: {key}")
    print(f"Mark: {value}")
    print()
    # Increment total by value of each student's mark
    total += value

# Calculate the average marks of all student
avg = total / len(results.values())
# Display average
print("Overall Average:", avg)

