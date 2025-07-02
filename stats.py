def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_list = []
    for char in text:
        if char.isalpha():
            char = char.lower()
            if not character_list:
                print(f"Adding first character: {char}")
                new_character = {"name": char, "num": 1}
                character_list.append(new_character)
            else:
                found = False
                for character in character_list:
                    if character["name"] == char:
                        print(f"Found existing character: {char}")
                        character['num'] += 1
                        found = True
                        break
                if not found:
                    print(f"Adding new character: {char}")
                    new_character = {"name": char, "num": 1}
                    character_list.append(new_character)

    #character_list.sort()
    print(character_list)
    return(character_list)