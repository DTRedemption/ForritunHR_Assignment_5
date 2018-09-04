n = int(input("Enter the length of the sequence: "))  # Do not change this line

# insert number "n"
# use while loop
# define a,b,c
# a b c are 0 1 0 for this specific fibonacci sequence
# while x less than number
# create trib variable that is sum of a + b + c
# assign a,b,c to trib, a and b respectively
# increment by 1
# print each number successively

x = 0

a = 0
b = 1
c = 0

while x < n:

    trib = a + b + c

    a, b, c = trib, a, b

    x += 1

    print(trib)
