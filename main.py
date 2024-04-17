def main():
    file_path = "books/frankenstein.txt"

    def count_words(text):
        length = len(text.split())
        print(f"{length} words found in thee document")

    def sort_by_value(dictionary):
        items = list(dictionary.items())
        n = len(items)
        for i in range(n):
            # Flag to check if any swapping occurred in this pass
            swapped = False
            for j in range(0, n - i - 1):
                if items[j][1] < items[j + 1][1]:
                    # Swap if the current value is greater than the next value
                    items[j], items[j + 1] = items[j + 1], items[j]
                    swapped = True
            # If no swapping occurred, the list is already sorted
            if not swapped:
                break

        return dict(items)

    def group_letters(text):
        letters_dict = {}
        string_list = text.split()

        for string in string_list:
            for character in string:
                if not character.isalpha():
                    continue

                lower_char = character.lower()

                if lower_char not in letters_dict:
                    letters_dict[lower_char] = 1
                else:
                    letters_dict[lower_char] += 1

        letters_dict = sort_by_value(letters_dict)

        for entry in letters_dict:
            print(f"The '{entry}' character was found {letters_dict[entry]} times")

    with open(file_path, "r") as file:
        text = file.read()
        print("---Report---")
        print()
        count_words(text)
        group_letters(text)
        print("---End Report---")


main()
