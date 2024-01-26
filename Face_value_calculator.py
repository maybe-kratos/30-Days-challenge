#sum of face value calculator

# Simply take the number and print the sum of its didits like 
# 123 prints 6 and 555 prints 15
Number = int(input("Enter the number =>"))
number_in_string = str(Number)

total = 0
for i in range (0,len(number_in_string)):
    digit = int(number_in_string[i])
    total = total + digit

print(total)