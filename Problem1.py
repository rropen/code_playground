def count_sum(num):
    #This works out the sum of all the digits in the integer.
    Sum = 0
    for digit in str(num):
        Sum += int(digit)
    count = 0
    #This counts the digits in the integer.
    while(num > 0):
        count += 1
        num = num//10
    #This prints the results of the function.
    print("Number of digits: ", count)
    print("Sum of digits: ", Sum)

count_sum(123456890)