
# with open("my_file.txt") as file:
#     contents = file.read()

# read -r, write -w, append -a

# print(contents)

with open("my_file.txt", "a") as file:
    file.write("\nNew line written")


# Absolute file paths start off at the Root (C: on Windows)
# Working directory - the folder that you are in, form there you'll use a Relative file path
    # Down (./Lower_Folder/file.pdf)
    # Up (../Upper_Folder/file.txt)

# readlines() - returns each line in a file as an item in a list
