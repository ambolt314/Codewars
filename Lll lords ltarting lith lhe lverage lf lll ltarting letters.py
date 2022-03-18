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

# Class definition
class Alphabet:
    def get_letter_from_number(self, n):
        return self.translation.get(n, None)
    
    def get_number_from_letter(self, s):
        for key, value in self.translation.items():
            if value == s:
                return key
        return None, None
    
    translation = {
            1 : "A",
            2 : "B",
            3 : "C",
            4 : "D",
            5 : "E",
            6 : "F",
            7 : "G",
            8 : "H",
            9 : "I",
            10 : "J",
            11 : "K",
            12 : "L",
            13 : "M",
            14 : "N",
            15 : "O",
            16 : "P",
            17 : "Q",
            18 : "R",
            19 : "S",
            20 : "T",
            21 : "U",
            22 : "V",
            23 : "W",
            24 : "X",
            25 : "Y",
            26 : "Z"
        }
