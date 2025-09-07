#Write and Append Data to a File
#Code:

user_input = input("Enter some text to write into output.txt: ")
with open("myfile.txt", "w") as file:
    file.write(user_input + "\n")
    print("Data written to file")

append_input = input("Enter some text to append into output.txt: ")
with open("myfile.txt", "a") as file:
    file.write(append_input + "\n")
    print("Data appended to file")

print("\nFinal contents of output.txt:")
with open("myfile.txt", "r") as file:
    print(file.read())
