def reverse_string(string):
    return string[::-1]

def reverse_using_stack(string):
    new_string = ""
    for c in string[::-1]:
        new_string += c
    return  new_string

def reverse_string_alt(string):
    string_list = list(string)
    reversed_string = ''
    while (len(string_list) > 0):
        reversed_string += string_list.pop()
    return reversed_string




if __name__ == "__main__":
    arthurvargas = "arthurvargas"
    print(reverse_string_alt(arthurvargas))