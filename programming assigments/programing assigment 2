# simple_calculator.py

def odd_or_even(number: int) -> str:
    """Return 'even' if number is even, 'odd' if number is odd."""
    return "even" if number % 2 == 0 else "odd"


def count_the_digits(number: int) -> int:
    """Return the number of digits in the number."""
    return len(str(abs(number)))  # abs() handles negatives


def is_prime(number: int) -> bool:
    """Return True if number is prime, else False."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def next_prime(number: int) -> int:
    """Return the next prime >= number."""
    if number < 2:
        return 2
    while not is_prime(number):
        number += 1
    return number


def list_of_primes(max: int) -> list:
    """Return a list of all primes <= max."""
    return [n for n in range(2, max + 1) if is_prime(n)]


def this_many_primes(count: int) -> list:
    """Return a list of the first 'count' primes starting from 2."""
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def main():
    print("Check out this amazing calculator!")
    print("Options:")
    print("1 <number>   → odd_or_even")
    print("2 <number>   → count_the_digits")
    print("3 <number>   → is_prime")
    print("4 <number>   → next_prime")
    print("5 <number>   → list_of_primes")
    print("6 <count>    → this_many_primes")
    print("Press ENTER with no input to quit.\n")

    while True:
        user_input = input("Enter operation: ").strip()
        if user_input == "":
            print("Goodbye!")
            break

        try:
            option, value = user_input.split()
            option, value = int(option), int(value)

            if option == 1:
                print(odd_or_even(value))
            elif option == 2:
                print(count_the_digits(value))
            elif option == 3:
                print(is_prime(value))
            elif option == 4:
                print(next_prime(value))
            elif option == 5:
                print(list_of_primes(value))
            elif option == 6:
                print(this_many_primes(value))
            else:
                print("Invalid option. Please choose between 1 and 6.")

        except ValueError:
            print("Invalid input format. Use: <option> <number>")


if __name__ == "__main__":
    main()
