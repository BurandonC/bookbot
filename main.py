def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()  # Convert text to lowercase
    character_counts = {}
    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def generate_report(path_to_file, word_count, character_counts):
    report_lines = []
    report_lines.append(f"--- Begin report of {path_to_file} ---")
    report_lines.append(f"{word_count} words found in the document\n")
    
    # Sort characters by count in descending order
    sorted_characters = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_characters:
        if char.isprintable() and char != ' ':
            report_lines.append(f"The '{char}' character was found {count} times")
    
    report_lines.append("--- End report ---")
    
    return "\n".join(report_lines)

def main():
    path_to_file = 'books/frankenstein.txt'
    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    character_counts = count_characters(file_contents)
    
    report = generate_report(path_to_file, word_count, character_counts)
    print(report)

if __name__ == "__main__":
    main()
