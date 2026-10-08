import json
from pathlib import Path

def load_json(filepath: str) -> dict:
    """Reads a JSON file and converts it into a Python dictionary."""
    path = Path(filepath)
    
    with open(path, "r", encoding="utf-8") as file:
        # json.load() translates the raw JSON text into Python data types
        return json.load(file)

def save_json(filepath: str, data: dict):
    """Writes a Python dictionary to a JSON file."""
    path = Path(filepath)
    
    # "w" mode means write. It will overwrite the file if it exists.
    with open(path, "w", encoding="utf-8") as file:
        # indent=4 makes the JSON readable for humans
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    # 1. Read the data
    data = load_json("data.json")
    
    print("--- JSON Data ---")
    print(f"Project Name: {data['name']}")
    print(f"Version: {data['version']}")
    
    print("Features included:")
    for feature in data["features"]:
        print(f"- {feature}")
        
    # 2. Modify the data in Python
    data["version"] = 1.1
    data["features"].append("json_writing")
    
    # 3. Save it back to a NEW file
    save_json("updated_data.json", data)
    print("\nSaved updated data to 'updated_data.json'!")
