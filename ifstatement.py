import time

def main():
    while True:
        try: 
            age = int(input("\nWhat is your Age?"))

            if age < 0:
                print("Age cannot be negative.")
                time.sleep(1)
                continue

            if age > 116:
                print("You are lying.")
                time.sleep(1)
                continue

            calc(age)
            break
        
        except ValueError:
            print("Please enter an Integer for your Age.")
            time.sleep(1)

def calc(check):
    if check >= 18:
        print("You are an adult.")
    else:
        print("You are a child.")

main()