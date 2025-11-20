def word_counter(text):
    words = text.split()
    return len(words)

def character_counter(text):
    character_count = {}
    for character in text:
        character = character.lower()
        if character in character_count:
            character_count[character] += 1
        else: 
            character_count[character] = 1
    return character_count

def sort_on(dioeunmostro):
    return dioeunmostro["num"]
    
def dictionary_to_sorted_list(character_count):
    sorted_list = []
    for ch in character_count:
        sorted_list.append({"character": ch, "num": character_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


