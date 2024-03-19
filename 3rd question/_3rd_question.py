with open("text_file.txt", "r") as file:
    lines = file.readlines()


lines.reverse()


with open("reversed.txt", "w") as file:
    file.writelines(lines)

print("Reversed lines have been saved to 'reversed.txt'")