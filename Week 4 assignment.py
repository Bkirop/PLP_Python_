
# Week 4 Assignment: File Handling and Text Processing
'''🔹 Challenge: Create a program that reads a text file, processes its content, and writes the results to a new file'''
.
# Step 1: Create input.txt with at least five lines of text
with open("input.txt", "w") as file:
    file.write("The sun rises in the east.\n")
    file.write("Birds chirp in the morning.\n")
    file.write("Coffee wakes up the soul.\n")
    file.write("Nature is peaceful and calm.\n")
    file.write("Every day is a new beginning.\n")

# Step 2: Read contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Step 3: Count the number of words
word_count = len(content.split())

# Step 4: Convert all text to uppercase
uppercase_content = content.upper()

# Step 5: Write processed text and word count to output.txt
with open("output.txt", "w") as file:
    file.write(uppercase_content)
    file.write(f"\n\nWORD COUNT: {word_count}\n")

# Step 6: Print success message
print("✅ Success! 'output.txt' has been created with processed content.")

# TODO: Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
def process_file():
    # Ask the user for a filename
    filename = input("📂 Enter the name of the file to process (e.g., input.txt): ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Count words
        word_count = len(content.split())

        # Convert to uppercase
        uppercase_content = content.upper()

        # Write to output.txt
        with open("output.txt", "w") as output_file:
            output_file.write(uppercase_content)
            output_file.write(f"\n\nWORD COUNT: {word_count}\n")

        print("✅ Success! 'output.txt' has been created with processed content.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"⚠️ Error: The file '{filename}' could not be read.")

# Run the function
process_file()
