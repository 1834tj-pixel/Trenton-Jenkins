#def main() -> None:

#    f = open"../Lecture ExampleDota/test-file1.txt", "r", encoding="utf8")

  #  file_input = f.read()
#    file_input_lower: str = file_input.lower()
   # counter: int = file_input_lower.count("this", _start:0, len(file_input_lower))

#    print(counter)

#if __name__ == "__main__":
   # main()


#if __name__ == "__main__":
#    main()
#
#def boolean_computer() -> None:
#    for a in range(0,2):
   #     for b in range(0,2):
  #          for c in range(0,2):
 #               print(a, b, c)
#
#if __name__ == "__main__":
#    boolean_computer()


def main() -> None:
        print("Check out this cool book reader app!")
        text_file: str = input("What file do you want to proccess? ")
        try:
            with open(f"../Lecture ExamplesData/{text_file}.txt", "r") as file:
                text = file.read()
                print(text)
            except FileNotFoundError:
            print("File not found")
