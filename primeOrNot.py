while True:
    number = input("Enter any number: ")
    try:
        num = int(number)
        break
    except ValueError:
        print("Enter a valid number!")
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
else:
    print("Prime Number")
    
     