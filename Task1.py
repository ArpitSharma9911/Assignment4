#Task 1: Read a File and Handle Errors 
#Code:
try:
    with open("myfile.txt", "r") as file:
        print("Contents of sample.txt:")
        for line in file:
            print(line.strip())   # strip() removes extra newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
