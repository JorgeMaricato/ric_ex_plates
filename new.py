def main():
    plate = input("Plate: ")

    if is_plate_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_plate_valid(s):
    # Condition: size validation
    if len(s) > 6 or len(s) < 2:
        return False

    # Condition: initial chars validation
    if s[0].isdigit() or s[1].isdigit():
    return False

    # Condition: no pontuation validation - legacy
    # for c in s:
    #     if c in [":", ":", "?", "!", ",", " ", ";"]:
    #         return False

    firstNumberFound = False

    for char in s:
    
        # Condition: no pontuation validation
        if not (char.isdigit() or char.isalpha()):
            return False

        if char.isdigit():
            firstNumberFound = True

            # Condition: no "0" as first digit
            if char == "0":
                return False

        # Condition: no number in the middle    
        if firstNumberFound and char.isalpha():
            return False

    return True


main()