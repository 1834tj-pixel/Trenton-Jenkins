

import os
from math import sqrt


def get_matrix(filename: str) -> list:
    try:
        path = os.path.join("text_files", filename)
        with open(path, "r") as file:
            print("Looking for file at:", os.path.abspath(path))

            matrix = [list(map(int, line.split())) for line in file if line.strip()]
        return matrix
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def write_matrix(filename: str, matrix: list, adjustment: int, *row_numbers: int) -> bool:
    try:
        path = os.path.join("text_files", filename)
        rows = range(len(matrix)) if not row_numbers else row_numbers
        with open(path, "w") as file:
            for i, row in enumerate(matrix):
                if i in rows:
                    new_row = [str(num * adjustment) for num in row]
                else:
                    new_row = [str(num) for num in row]
                file.write(" ".join(new_row) + "\n")
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        return False


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(numbers: list, *row_numbers: int) -> list:
    rows = range(len(numbers)) if not row_numbers else row_numbers
    return [[num for num in numbers[i] if is_prime(num)] for i in rows]


def get_sum(numbers: list, *row_numbers: int) -> int:
    rows = range(len(numbers)) if not row_numbers else row_numbers
    return sum(sum(numbers[i]) for i in rows)


def get_largest_number(numbers: list, *row_numbers: int) -> int:
    rows = range(len(numbers)) if not row_numbers else row_numbers
    return max(max(numbers[i]) for i in rows)


def most_occurrences(numbers: list, *row_numbers: int) -> list:
    rows = range(len(numbers)) if not row_numbers else row_numbers
    result = []
    for i in rows:
        freq = {}
        for num in numbers[i]:
            freq[num] = freq.get(num, 0) + 1
        most_common = max(freq, key=freq.get)
        result.append(most_common)
    return result


def consolidate_sorted(numbers: list, *row_numbers: int) -> list:
    rows = range(len(numbers)) if not row_numbers else row_numbers
    combined = []
    for i in rows:
        combined.extend(numbers[i])
    return sorted(combined)


def page_data(numbers: list, page_size: int, page_number: int) -> list:
    start = (page_number - 1) * page_size
    end = start + page_size
    return numbers[start:end]


def main():
    print("Welcome to the Matrix!")
    matrix = []

    while True:
        print("\nChoose an operation:")
        print("1: Load matrix from file")
        print("2: Write adjusted matrix to file")
        print("3: Get primes from rows")
        print("4: Get sum of rows")
        print("5: Get largest number from rows")
        print("6: Get most frequent number per row")
        print("7: Consolidate and sort rows")
        print("8: Page through sorted data")
        print("(Press Enter with no input to exit)")

        user_input = input("\nEnter operation and arguments: ").strip()
        if not user_input:
            print("Goodbye! Exiting program.")
            break

        parts = user_input.split()
        op = int(parts[0])

        if op != 1 and not matrix:
            print("You must load a matrix first using option 1.")
            continue

        try:
            if op == 1:
                filename = parts[1]
                matrix = get_matrix(filename)
                print("Matrix loaded successfully.")

            elif op == 2:
                filename = parts[1]
                adjustment = int(parts[2])
                rows = [int(x) for x in parts[3].split(",")] if len(parts) > 3 else []
                success = write_matrix(filename, matrix, adjustment, *rows)
                print("File written successfully." if success else "Failed to write file.")

            elif op == 3:
                rows = [int(x) for x in parts[1].split(",")] if len(parts) > 1 else []
                print(get_primes(matrix, *rows))

            elif op == 4:
                rows = [int(x) for x in parts[1].split(",")] if len(parts) > 1 else []
                print(get_sum(matrix, *rows))

            elif op == 5:
                rows = [int(x) for x in parts[1].split(",")] if len(parts) > 1 else []
                print(get_largest_number(matrix, *rows))

            elif op == 6:
                rows = [int(x) for x in parts[1].split(",")] if len(parts) > 1 else []
                print(most_occurrences(matrix, *rows))

            elif op == 7:
                rows = [int(x) for x in parts[1].split(",")] if len(parts) > 1 else []
                print(consolidate_sorted(matrix, *rows))

            elif op == 8:
                page_size = int(parts[1])
                page_number = int(parts[2])
                # For paging, assume you already consolidated the matrix before
                numbers = consolidate_sorted(matrix)
                print(page_data(numbers, page_size, page_number))

            else:
                print("Invalid option. Please select between 1-8.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
