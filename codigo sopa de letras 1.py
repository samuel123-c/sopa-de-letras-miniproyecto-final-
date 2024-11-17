import json

# Define a function to read the content of a file
def get_file_content(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Check if a word exists in the word search puzzle
def find_word(letter_soup, word):
    rows = len(letter_soup)  # Number of rows in the word search puzzle
    cols = len(letter_soup[0])  # Number of columns in the word search puzzle
    word = word.upper()  # Convert the word to uppercase for a case-insensitive search
    word_len = len(word)  # Length of the word to search

    # Define possible directions for word search
    directions = [
        (1, 0),   # down
        (-1, 0),  # up
        (0, 1),   # right
        (0, -1),  # left
        (1, 1),   # diagonal down-right
        (-1, -1), # diagonal up-left
        (1, -1),  # diagonal down-left
        (-1, 1)   # diagonal up-right
    ]

    # Traverse the entire word search puzzle
    for r in range(rows):
        for c in range(cols):
            if letter_soup[r][c] == word[0]:  # Match the first letter of the word
                for dr, dc in directions:  # Try all possible directions
                    found = True
                    for k in range(word_len):  # Check each character of the word
                        nr, nc = r + k * dr, c + k * dc  # Calculate the next position
                        if not (0 <= nr < rows and 0 <= nc < cols) or letter_soup[nr][nc] != word[k]:
                            found = False  # Stop if out of bounds or characters do not match
                            break
                    if found:
                        return True  # Return True if the word is found
    return False  # Return False if the word is not found

# Check if a list of words exists in the word search puzzle
def find_words(letter_soup, words):
    # Return a dictionary with each word and whether it is found (True or False)
    return {word: find_word(letter_soup, word) for word in words}

# Generate a JSON report and print it
def generate_report(letter_soup, words, output_file):
    # Get search results
    results = find_words(letter_soup, words)
    
    # Print results in JSON format
    print(json.dumps(results, indent=4))
    
    # Save results to a JSON file
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)
    print(f"Report saved to file: {output_file}")

# Main flow
def main():
    # Prompt the user for the file path
    file_path = input("Enter the input file path: ").strip()
    output_file = "result.json"  # Name of the output file
    
    # Read the file content
    content = get_file_content(file_path)
    
    # Split the word search puzzle and the list of words
    separator_index = content.index('---')  # Locate the separator
    letter_soup = [list(line) for line in content[:separator_index]]  # Word search puzzle
    words = [line.strip() for line in content[separator_index + 1:]]  # List of words
    
    # Generate the report
    generate_report(letter_soup, words, output_file)

# Entry point of the program
if __name__ == "__main__":
    main()
