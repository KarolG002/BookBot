def read_file(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> dict:
    char_dict = {}
    for letter in text.lower():
        if letter.isalpha():  # Only count alphabetic characters
            char_dict[letter] = char_dict.get(letter, 0) + 1
    return char_dict


if __name__ == "__main__":
    FILEPATH = "books/frankenstein.txt"

    x = read_file(FILEPATH)

    char_counts = count_chars(x)

    # Convert dictionary to a list of dictionaries
    char_list = [{"letter": key, "count": value} for key, value in char_counts.items()]

    # Sort by count (descending)
    char_list.sort(key=lambda d: d["count"], reverse=True)

    # Print sorted results
    for item in char_list:
        print(f"The '{item['letter']}' character was found {item['count']} times")
