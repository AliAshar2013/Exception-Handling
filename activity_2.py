try:
    n = int(input("Enter a number: "))
    m = int(input("Enter another number you would like to divide with the first one: "))
    print(n/m)
except ZeroDivisionError:
    print("Dividing by zero is error!!")
except ValueError:
    print("Invalid number")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")