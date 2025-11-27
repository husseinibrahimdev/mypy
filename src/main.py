# src/main.py
from utils import add, multiply, greet

def say(word):
    print(f"{word}")

for c in 'character':
    print(c)

def main():
    print("=== Python Project Starter ===")
    name = input("Enter your name: ")
    word = input('what should i say ')
    say(word)
    print(greet(name))

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))


    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")

if __name__ == "__main__":
    main()