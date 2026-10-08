# Notice how clean this is! We import from our custom 'ai_toolkit' package.
from ai_toolkit import clean_whitespace, load_json

def main():
    print("Welcome to the AI Developer Toolkit!")
    
    # 1. Use our JSON tool
    data = load_json("data.json")
    print(f"\nLoaded project: {data['name']}")
    
    # 2. Use our Text tool
    messy = "   Look   how    clean our   architecture is  getting!   "
    clean = clean_whitespace(messy)
    print(f"\nCleaned text: '{clean}'")

if __name__ == "__main__":
    main()
