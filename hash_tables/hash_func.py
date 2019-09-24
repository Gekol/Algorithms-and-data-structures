def get_hash(elem):
    hash_code = 0
    for i in range(len(elem)):
        ch = elem[i]
        factor = i + 1
        if "0" <= ch <= "9":
            hash_code += (ord(ch) - 48) * factor
        elif "A" <= ch <= "Z":
            hash_code += (9 + ord(ch) - 64) * factor
        elif "a" <= ch <= "z":
            hash_code += (9 + 26 + ord(ch) - 96) * factor
    return hash_code