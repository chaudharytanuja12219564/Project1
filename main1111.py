n = int(input("Enter Number:"))  # input from user
# ====================================PRIME CHECK==================================== #
flag = 0
for i in range(2,n):  # looping to check if number is divisible by other numbers
    if n % i == 0:
        flag = 1  # setting flag value to 1
        print(i)  # printing value of i for which n is divisible
        break  # to exit from the if clause
if flag == 1:  # checking if the value of flag is 1 then print it is not prime
    print(n, "is not a Prime")
else:  # else print prime and the value of n
    print(n, "is Prime")
# ====================================PALINDROME CHECK#==================================== #
    x = n  # storing the value of n in variable x
    sum = 0  # initializing the value of sum to be 0
    while x > 0:  # starting while loop with condition z is non-zero
        r = x % 10 # storing remainder in variable r
        sum = sum * 10 + r  # adding remainder with sum
        x = x // 10  # true division of x
    if sum == n:  # checking if sum and n both are equal
        print(n, "is a Prime Palindrome")  # if equal print it is palindrome
    else:
        print(n, "is not a prime Palindrome")  # else not palindrome
