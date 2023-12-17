import os
import sys

def count_vowels(sentence):
    vowels = set("aeiouAEIOU")
    count = sum(1 for char in sentence if char in vowels)
    print(f"Parent Process - Number of Vowels: {count}")

def count_words(sentence):
    words = sentence.split()
    count = len(words)
    print(f"Child Process - Number of Words: {count}")

def main():
    sentence = "Hello, world! This is a sample sentence."

    # Fork a child process
    pid = os.fork()

    if pid > 0:
        # Parent process
        count_vowels(sentence)
        os.wait()  # Wait for the child process to finish
    elif pid == 0:
        # Child process
        count_words(sentence)
        sys.exit(0)  # Terminate the child process

if __name__ == "__main__":
    main()
