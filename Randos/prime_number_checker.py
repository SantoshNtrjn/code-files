def prime_number_checker(x):
    if x % 2 != 0:
        print("Prime.")
    else:
        print("Not Prime.")

user_value = int(input("Enter the number: "))
prime_number_checker(user_value)

