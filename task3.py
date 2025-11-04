import sys  # importing built-in python 'sys' module

# if cmdline arguments are less or equals 2, exit with an error message
if len(sys.argv) <= 2:
    sys.exit("Insufficient arguments provided!!")

# Convert the two arguments to integer and store them in n1 and n2 variables respectively
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

# Addition of n1 and n2
sum = n1 + n2
# Display the above sum
print("Sum:", sum)