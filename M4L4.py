# Step 1: Write to learning_python.txt
with open('learning_python.txt', 'w') as file:
    file.write("In Python you can:\n")
    file.write("In Python you can create classes and objects.\n")
    file.write("In Python you can work with files and directories.\n")
    file.write("In Python you can perform data analysis and visualization.\n")

# Step 2: Read and print the file three times
with open('learning_python.txt', 'r') as file:
    # Reading and printing the entire file
    content = file.read()
    print(content * 3)

    # Reading and printing using a loop over the file object
    file.seek(0)  # Reset file pointer to the beginning
    for line in file:
        print(line.strip() * 3)

    # Reading and printing using a list
    file.seek(0)  # Reset file pointer to the beginning
    lines = file.readlines()
    for line in lines:
        print(line.strip() * 3)

# Step 3: Replace 'Python' with 'PHP' and print modified lines
with open('learning_python.txt', 'r') as file:
    for line in file:
        modified_line = line.replace('Python', 'PHP')
        print(modified_line.strip())
