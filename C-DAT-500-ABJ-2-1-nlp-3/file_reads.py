from pathlib import Path

directory_path = Path('./books')  # Replace with your directory path
for file_path in directory_path.iterdir():
    if file_path.is_file():
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content of {file_path.name}:\n{content}\n")   