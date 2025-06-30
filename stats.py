def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_list = []
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in character_list:
                pass
            else:
                pass
    character_list.sort()
    return(character_list)