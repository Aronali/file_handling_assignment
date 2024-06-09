# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("We have the following data: 2.76, 1.83, 1.80, 1.45, 1.24 \n")
        file.write("The data are arranged from smallest to largest\n")
        file.write("12345\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Third line of text\n")
        file.write("Fourth line of text\n")
        file.write("54321\n")  # Appending more mixed content
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
finally:
    print("File operations completed.")

