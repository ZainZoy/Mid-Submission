# Question 1
def reverse(my_string: str) -> str:
    if len(my_string) == 0:
        return my_string
    else:
        return reverse(my_string[1:]) + my_string[0]


user_input = input("enter string to be reversed: ")
print(reverse(user_input))
