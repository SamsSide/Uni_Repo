
def encrypt(data, key):
    result = []
    characters = "^6zV+eE}j;w2L@F4nQ|m0qDY(8M'?#o{O_5S]X!g3:GZK9,aRtP`iy1lT.N$C[bhWk7<UfxA&)d%r>B~IJsHv-uacJp="
    for i in range(len(data)):
        char = data[i]
        if char in characters:
            idx = characters.index(char)
            new_idx = (idx + key) % len(characters)
            result.append(characters[new_idx])
        else:
            result[i] = char
    return "".join(result)

def decrypt(data, key):
    result = []
    characters = "^6zV+eE}j;w2L@F4nQ|m0qDY(8M'?#o{O_5S]X!g3:GZK9,aRtP`iy1lT.N$C[bhWk7<UfxA&)d%r>B~IJsHv-uacJp="
    for i in range(len(data)):
        char = data[i]
        if char in characters:
            idx = characters.index(char)
            new_idx = (idx - key) % len(characters)
            result.append(characters[new_idx])
        else:
            result[i] = char
    return "".join(result)


print(encrypt("HelloWorld123", 100))
