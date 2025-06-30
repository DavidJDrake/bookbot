def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_list = []
    for char in text:
        if char.isalpha():
            char = char.lower()
            for character in character_list:
                if character['name'] == char:
                    print(f"Character '{char}' already exists in the list.")
                    character['num'] += 1
                else:
                    print(f"Adding character '{char}' to the list.")
                    character_dict = {"name": char, "num": 1}
                    character_list.append(character_dict)
    character_list.sort()
    print(character_list)
    return(character_list)