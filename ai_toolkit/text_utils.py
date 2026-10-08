def clean_whitespace(text: str) -> str:
    """Removes extra spaces from the beginning, end, and between words."""
    # split() breaks the text into a list of words, ignoring extra spaces
    # " ".join() connects the words back together with exactly one space
    return " ".join(text.split())

# Let's test it quickly when the file runs
if __name__ == "__main__":
    messy_text = "   Hello     world! This   is   AI.   "
    cleaned = clean_whitespace(messy_text)
    print(f"Original: '{messy_text}'")
    print(f"Cleaned:  '{cleaned}'")
