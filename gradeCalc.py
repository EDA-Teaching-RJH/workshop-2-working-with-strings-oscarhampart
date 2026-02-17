def main():
    while True:
        try:
            score = int(input("Please enter your mark: "))
            if score > 100 or score < 0:
                print("Please enter a valid mark.")
                continue
            else:
                calc(score)
                break

        except ValueError:
            print("Please enter an integer.")
            continue
        
def calc(mark):
    if 90 <= mark <= 100:
        print("You got a Grade A.")

    elif 80 <= mark <= 89:
        print("You got a Grade B.")

    elif 70 <= mark <= 79:
        print("You got a grade C.")

    elif 60 <= mark <= 69:
        print("You got a grade D.")

    else:
        print("You failed with a Grade F.")

main()