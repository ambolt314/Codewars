def average_string(s):
    
    if s == "":
        return ""
    
    words = s.split(" ")
    
    starting_letters = []
    for word in words:
        starting_letters.append(word[0].upper())

    alphabet = Alphabet()
    starting_indices = list(map(alphabet.get_number_from_letter, starting_letters))
    avg_index = sum(starting_indices) // len(starting_indices)
    
    output = ""
    
    for word in words:
        if word[0].isupper():
            output += "{}{}".format(alphabet.get_letter_from_number(avg_index).upper(), word[1:]) + " "
        else:
            output += "{}{}".format(alphabet.get_letter_from_number(avg_index).lower(), word[1:]) + " "
    output = output.strip()
    return output
