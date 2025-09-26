# text_analyzer.py
import os
import datetime


def main():
    print("Welcome to the Awesome Book Reader App!")

    # Folder where text files are stored
    folder = "text_files"
    default_file = "default.txt"  # <- You should create this in text_files folder

    # Ask for filename
    filename = input("Enter the file name (inside 'text_files' folder): ").strip()
    if filename == "":
        filename = default_file

    filepath = os.path.join(folder, filename)
    if not os.path.isfile(filepath):
        print("Error: File not found.")
        return

    # Ask for search word
    search_word = input("Enter a word to search for: ").strip().lower()

    # Read file contents
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        text = "".join(lines)

    # Split into words (basic split by whitespace)
    words = text.split()

    # --- Required statistics ---
    # Normalize case + strip punctuation
    cleaned_words = [word.strip(".,!?;:\"'()[]{}").lower() for word in words]

    # 1. Count word occurrences
    word_count = cleaned_words.count(search_word)

    # 2. Number of characters
    num_chars = len(text)

    # 3. Number of lines
    num_lines = len(lines)

    # 4. Count first name occurrences ("Trenton")
    first_name = "trenton"
    name_count = cleaned_words.count(first_name)

    # 5. Number of words
    num_words = len(words)

    # --- Print statistics ---
    print(f"\nStatistics for '{filename}':")
    print(f"The word '{search_word}' appears {word_count} times.")
    print(f"Total characters: {num_chars}")
    print(f"Total lines: {num_lines}")
    print(f"My name shows up {name_count} times.")
    print(f"Total words: {num_words}\n")

    # --- Editing new file ---
    print("...making a new version of this file...")

    # Replace every occurrence of search_word with "Trenton Jenkins"
    replaced_text = []
    for word in words:
        cleaned = word.strip(".,!?;:\"'()[]{}").lower()
        if cleaned == search_word:
            replaced_text.append("Trenton Jenkins")
        else:
            replaced_text.append(word)
    new_text = " ".join(replaced_text)

    # Make uppercase
    new_text = new_text.upper()

    # Remove "a", "e", "o"
    for char in "AEO":
        new_text = new_text.replace(char, "")

    # Replace "p" or "P" with 9
    new_text = new_text.replace("P", "9")

    # Add signature line
    today = datetime.date.today().strftime("%m-%d-%Y")
    new_filename = f"{os.path.splitext(filename)[0]}_EDITED_BY_TJ_{today}.txt"
    new_filepath = os.path.join(folder, new_filename)

    with open(new_filepath, "w", encoding="utf-8") as f:
        f.write(new_text + "\n\n")
        f.write("Trenton Jenkins: Keep moving forward, no matter what!")

    print(f"New file created: {new_filename}")

    # Example usage of tuple, list, and set (required by assignment)
    demo_list = [search_word, first_name]
    demo_tuple = (num_chars, num_lines, num_words)
    demo_set = set(cleaned_words)

    # Just to show they are used
    print("\n[Debug] Example list:", demo_list)
    print("[Debug] Example tuple:", demo_tuple)
    print(f"[Debug] Unique words in file: {len(demo_set)}")

    print("\nProgram finished successfully.")


if __name__ == "__main__":
    main()
