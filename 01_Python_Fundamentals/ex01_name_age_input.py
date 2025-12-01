# Exercise: ex01_name_age_input
# Topic: 01 Python Fundamentals
#-------------------------------------------------------------------------------------
# 1- Para um primeiro contacto com a linguagem Python e com o editor VS Code, crie um 
# pequeno programa que comece por perguntar ao utilizador o nome e a idade, e lhe diga a
# seguir se é maior ou menor de idade, tratando-o pelo seu nome.
#-------------------------------------------------------------------------------------

ADULT_AGE_THRESHOLD = 18

def check_age(name: str, age: int) -> bool:

    if age >= ADULT_AGE_THRESHOLD:
        print(f"{name}, you are an adult.")
        return True
    else:
        print(f"{name}, you are a minor.")
        return False

user_name = input("Input your name: ")
try:
    user_age = int(input("Input your age: "))
except ValueError:
    print("Invalid age entered. Please use a number.")
    user_age = 0 

check_age(user_name, user_age)