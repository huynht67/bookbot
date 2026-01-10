def count_words(text):
    words = text.split()
    return len(words)
def count_characters(text):
    # Convert to lowercase so 'A' and 'a' are counted as the same
    lowered_text = text.lower()
    
    # Create a dictionary to store counts
    char_count = {}
    
    # Count every character
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count
