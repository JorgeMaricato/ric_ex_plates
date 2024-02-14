def main():
    plate = input("Plate: ")
    if is_valid(plate) and number_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif s[0].isdigit() or s[1].isdigit():
        return False
    for c in s:
        if c in [":", ":", "?", "!", ",", " ", ";"]:
            return False
    else:
        return True
#ate aqui vai certo esse segunda parte não ta funcionando.

def number_valid(s):
    i = 0
    j = len(s)
    while i < j:
       if s[i].isdigit() == "0":
            return False
       elif s[i].isdigit() and s[i:j].isalpha():
            return False
       else:
           break
    i = i + 1

main()