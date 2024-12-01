def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = count_words(text)
    character_list = characters(text)
    report = print_report(words_count, character_list)


# Prints Text
def get_book_text(path):
    
    with open(path) as f:
        return f.read()

# Makes Directory with number of characters
def characters(text):
    lowercase = text.lower()
    character_count = {}

    for i in lowercase:
        
        if i.isalpha():
            if i in character_count:
                character_count[i] += 1
            else:
                character_count[i] = 1

    character_list = [{"char": char, "num": num} for char, num in character_count.items()]
    character_list.sort(key=lambda x: x["num"], reverse=True)
    return character_list

# Counts Total Words Count
def count_words(text):
    words = text.split()
    return f"{len(words)} words found in the document"

def print_report(words_count, character_list):
    
    print("--- Begin report ---")
    print(words_count)
    print("")
    
    for character in character_list:
        char = character["char"]
        num = character["num"]
        print(f"The {char} characcter was found {num} times")

    print("--- End report ---")

main()
