# Step 1: Function to read from a file
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Step 2: Function to modify the content
def modify_content(original_content):
    # Example modification: convert text to uppercase and add a header
    modified = "=== Modified Content ===\n" + original_content.upper()
    return modified

# Step 3: Function to write to a new file
def write_file(new_file_path, content):
    with open(new_file_path, 'w') as file:
        file.write(content)

# Step 4: Call functions in sequence
input_path = r"C:\Users\LENOVO\Desktop\PLP\Python\Week 4\README.MD"  # Use raw string for Windows path
output_path = r"C:\Users\LENOVO\Desktop\PLP\Python\Week 4\output.txt"  # Use raw string for Windows path

original = read_file(input_path)
modified = modify_content(original)
write_file(output_path, modified)

# Step 5: Print success message
print("✅ File processing complete. Modified content saved to:", output_path)
