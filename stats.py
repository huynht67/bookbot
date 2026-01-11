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

def get_sorted_char_counts(char_counts):
    # Build list of dicts: [{'char': 'e', 'num': 44538}, ...]
    items = []
    for char, count in char_counts.items():
        # Only include alphabetical characters (a-z after lowercase)
        if char.isalpha():
            items.append({"char": char, "num": count})
    
    # Sort by count descending (highest to lowest)
    def sort_on(item):
        return item["num"]
    
    items.sort(reverse=True, key=sort_on)
    
    return items
