import math  

def main():
    side1 = int(input("Input Side1: "))
    side2 = int(input("Input Side2: "))
    pythag(side1, side2)

def pythag(A,B):
    hyp = math.sqrt(A ** 2 + B ** 2)
    print("The Hypotenuse is equal to: ", hyp)

main()

# Can also use hyp = math.hypot(A, B)