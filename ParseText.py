file_path = "ParseText.txt"
output_file_path = "Output.txt"

clearText = input("Clear: ")

try:
    with open(file_path, 'r') as file:
        content = file.read()
        # Stripping the substring from the content
        stripped_content = content.replace(clearText, '\n')
        print(stripped_content)

    with open(output_file_path, 'w') as output_file:
        output_file.write(stripped_content)

except FileNotFoundError:
    print(f"The file {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
