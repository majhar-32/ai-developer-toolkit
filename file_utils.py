from pathlib import Path

def read_text_file(filepath: str) -> str:
    """Reads a text file and returns its content. Returns empty string if not found."""
    path = Path(filepath)
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Could not find the file '{filepath}'.")
        return ""

if __name__ == "__main__":
    content = read_text_file("does_not_exist.txt")
    
    if content:
        print("--- File Content ---")
        print(content)
        print("--------------------")
    else:
        print("No content to display.")
