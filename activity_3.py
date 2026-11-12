flag = False
counter = 2
while not flag:
    try:
        n = int(input("Enter a number: "))
        while n % 2 == 0:
            print("Bye")
            n = int(input(f"Enter a {counter} number: "))
            counter +=1
        flag = True
    except ValueError:
        print("Invalid number")
