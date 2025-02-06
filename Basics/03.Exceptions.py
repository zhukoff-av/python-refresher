def divide_numbers():
    while True:
        try:
            num1 = float(input('Input the first number: '))
            num2 = float(input('Input the second number: '))
            result = num1 / num2
            print(f'Result {result}')
            break
        except ValueError:
            print('Enter the valid number')
        except ZeroDivisionError:
            print("🚫 Sorry, can't divide by zero! Even Chuck Norris tried and failed 💪😅")
        finally:
            print("🧹 Cleaning up the mess... Because even superheroes need to tidy up! 🦸‍♂️")


divide_numbers()
