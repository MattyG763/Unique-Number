# This program takes your name and outputs a number that is unique to your name based on ascii.

def main():
    name = input_name()
    first, last = name.split(" ")
    
    sum_of_name = add(count_first(first), count_last(last))
    print(f"Your unique number based on your name is: {sum_of_name}")

# Take the users First and last name and split it into two vaiables.
def input_name():
    return input("What is your first and last name? ").strip().title()

def count_first(first):
    # Go through the first name and convert each letter to ascii
    # add each ascii together and return the total
    total_in_ascii = 0

    for i in first:
        total_in_ascii += ord(i)
    
    print(f"First Total: {total_in_ascii}")
    return total_in_ascii

def count_last(last):
    # Go through the last name and convert each letter to ascii
    # add each ascii together and return the total
    total_in_ascii = 0

    for i in last:
        total_in_ascii += ord(i)
    
    print(f"Last Total: {total_in_ascii}")
    return total_in_ascii

# Add the two numbers together and return the total.
def add(num1, num2):
    return num1 + num2

if __name__ == '__main__':
    main()