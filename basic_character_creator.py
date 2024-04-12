#Basic Character Creator
def create_character(character_name, character_race, character_class):
    """Basic character creator"""
    character = f"{character_name} {character_race} {character_class}"
    return character.title()

while True:
    print("\nCreate your character:")
    print("(Press 'q' to quit this program)")

    c_name = input("Character Name: ")
    if c_name == 'q':
        break

    c_race = input("Select Your Race: ")
    if c_race == 'q':
        break

    c_class = input("Select Your Class: ")
    if c_class == 'q':
        break

    character = create_character(c_name, c_race, c_class)
    print("\nHere is your character:")
    print(f"\nName: {c_name}, Race: {c_race}, Class: {c_class}")
    break
