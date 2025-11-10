






def main() -> None:
    print('This is a cool matrix code')
    input_value: str = input("give me some input")
    matrix: list = []
    while len(input_value) != 0:
        try:
            input_split: list = input_value.split(' ')
            operator: str = input_split[0]
            if operator == '1':
                matrix = get_matrix(f'../lectureExamplesData/{input_split[1]}')
                print(matrix)
            elif operator == '2':
                adjustment = int(input_split[2])
            row_numbers = get_row_numbers(input_split,3)
            print(write_matrix(f'../lectureExamplesData/{input_split[1]}', matrix, adjustment, row_numbers))
    elif operator == '3':
        get_primes(matrix, )

def get_row_numbers(input_split: list, row_numbers: int) -> list:
    return [int(nums( for nums in input_split[index].split(',')] if len(input_split) > index else []

if __name__ == '__main__':
    main()
