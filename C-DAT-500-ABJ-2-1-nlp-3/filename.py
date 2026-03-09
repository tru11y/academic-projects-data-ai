# 
from pathlib import Path

directory_path = Path("./books") 

for file_path in directory_path.rglob("*"):  
    if file_path.is_file():  
        try:
            
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print(f"Content of {file_path.replace('books/', '')}")
                # print(content.head())
                print("-" * 50)
        except Exception as e:
            print(f"{file_path}".replace('books/', ''))   