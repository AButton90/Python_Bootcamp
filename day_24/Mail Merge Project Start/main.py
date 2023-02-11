# TODO: Create a letter using starting_letter.txt 
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Letters/starting_letter.txt") as file_a:
    letter = file_a.read()

with open("Input/Names/invited_names.txt") as file_a:
    names = file_a.read()

name_list = names.split("\n")


for name in name_list:
    personal_letter = letter.replace("[name]", name)

    with open(f"Output/ReadyToSend/{name}.txt", "w") as file:
        file.write(personal_letter)

pass
