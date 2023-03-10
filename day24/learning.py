# with open("my_text.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_text.txt", mode="a") as file:
    file.write("\nsome else new text")

with open("my_text_1.txt", mode="a") as file:
    file.write("\nSome new teext in new file")