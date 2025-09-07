
# Assignment4
This repository contains Python scripts for basic programming practice.  

## 📌 Task 1: Read a File and Handle Errors 
### Problem Statement:  
Write a Python program that:  
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.


### Code: 
try:
    with open("sample.txt", "r") as file:
        print("Contents of sample.txt:")
        for line in file:
            print(line.strip()) 
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

### Features:
Uses with open() for safe file handling.
Implements try-except for error handling.
Prints file content line by line.

## 📌 Task 2: Write and Append Data to a File
### Problem Statement:  
Write a Python program that:  
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

### Code: 
# Step 1: Write user input to output.txt
user_input = input("Enter some text to write into output.txt: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data
append_input = input("Enter some text to append into output.txt: ")
with open("output.txt", "a") as file:
    file.write(append_input + "\n")

# Step 3: Read and display final content
print("\nFinal contents of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())

### Example Output:  
Enter some text to write into output.txt: Hello World!
Data written to file
Enter some text to append into output.txt: How are you?
Data appended to file

Final contents of output.txt:
Hello World!
How are you?
