from collections import deque

def is_palindrome(input_str):
    cleaned_str = input_str.lower().replace(" ", "")

    char_queue = deque(cleaned_str)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True

def main():
    
    input_string = "A man a plan a canal Panama"
    # input_string = "Ded"
    result = is_palindrome(input_string)

    if result:
        print(f'Рядок "{input_string}" є паліндромом.')
    else:
        print(f'Рядок "{input_string}" не є паліндромом.')

if __name__ == "__main__":
    main()