import os
import re
from collections import Counter


def create_sample_file():
    """Prompt user to create 'sample.txt' if it doesn't exist."""
    text = input("Enter text to create sample.txt: ")
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write(text)


def read_file_line_by_line():
    """Read the content of 'sample.txt' line by line."""
    with open("sample.txt", "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def clean_and_tokenize(text):
    """Convert text to lowercase, remove punctuation using regex, and split into words."""
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text.split()


def count_word_frequency():
    """Count occurrences of each word in the file using a memory-efficient approach."""
    word_counter = Counter()
    for line in read_file_line_by_line():
        words = clean_and_tokenize(line)
        word_counter.update(words)
    return word_counter


def save_report(total_words, word_counts):
    """Save the word count report to 'word_count_report.txt'."""
    with open("word_count_report.txt", "w", encoding="utf-8") as f:
        f.write("Word Count Report\n")
        f.write(f"Total Words: {total_words}\n")
        f.write("Top 5 Words:\n")
        for word, count in word_counts:
            f.write(f"{word} - {count}\n")


def main():
    if not os.path.exists("sample.txt"):
        create_sample_file()

    word_freq = count_word_frequency()
    total_words = sum(word_freq.values())
    top_5_words = word_freq.most_common(5)

    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_5_words:
        print(f"{word} - {count} times")

    save_report(total_words, top_5_words)


if __name__ == "__main__":
    main()
