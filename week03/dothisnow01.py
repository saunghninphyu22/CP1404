# Vd 1

FILENAME = "text.txt"

def main():
    secret = load_number(FILENAME)
    guess = get_valid_number()
    while guess != secret:
        print("Guess again")
        guess = get_valid_number()
    print("You got it!")

def get_valid_number():
    """Get a valid number from the user"""
    is_valid_input = False
    while not is_valid_input:
        try:
            guess = int(input("Guess: "))
            is_valid_input = True
        except ValueError:
            print("Invalid integer.")
    return guess

def load_number(filename):
    """Load an integer from a file."""
    try:
        infile = open(FILENAME, "r")
        number = int(infile.read())
    except ValueError:
        print("Invalid contents in {filename}")
        number = 6
    except FileNotFoundError:
        print("File not found.")
        number = 4
    else:
        infile.close()
    return number

main()

