import collections
#Open and Read txt file
def read_file(filename):
    with open("./sample.txt", 'r') as file:
        return file.read()
content = read_file('sample.txt')
print(content) 

#Counting Number of lines
def count_lines(content):
    return len(content.split('\n'))

#Counting Words
def count_words(content):
    return len(content.split())

#Average Word Length
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

#Most Common Word
def most_common_word(content):
    words = content.lower().split() 
    word_counts = collections.Counter(words) 
    common_word, count = word_counts.most_common(1)[0] 
    return common_word, count

# Count Number of Unique words in TXT
def count_unique_words(text):
    words = text.split()
    unique_words = set(words) 
    return len(unique_words)

# Find Longest word in text
def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word 

# Counting the Occurance of specific word
def count_word_occurrences(text, specific_word):
    words = text.lower().split() 
    specific_word = specific_word.lower()
    return words.count(specific_word)

#Calculate % of Words Longer than Average Length
def percentage_words_longer_than_average(text):
    words = text.split()
    word_lengths = [len(word) for word in words]
    average_length = sum(word_lengths) / len(word_lengths) 
    longer_than_average = [word for word in words if len(word) > average_length]
    percentage = (len(longer_than_average) / len(words)) * 100 
    return percentage

# Combine all to main
def analyze_text(filename):
    content = read_file(filename)
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    unique_word_count = count_unique_words(content)
    longest_word = find_longest_word(content)
    occurrences = count_word_occurrences(content, 'the')
    percentage_longer_than_average = percentage_words_longer_than_average(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Number of unique words: {unique_word_count}")
    print(f"Longest word: {longest_word}")
    print(f"Occurrences of 'the': {occurrences}")
    print(f"Percentage of words longer than the average length: {percentage_longer_than_average:.2f}%")
analyze_text('sample.txt') 
