num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

# insert number
# while number >=0
# set max_int = 0
# if num_int is greater than max_int, assign max_int
# insert number again
# else print max_int

max_int = 0
while num_int > -1:
    if num_int > max_int:
        max_int = num_int
        num_int = int(input("Input a number: "))
    else:
        num_int = int(input("Input a number: "))

print("The maximum is", max_int)  # Do not change this line
