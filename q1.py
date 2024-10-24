def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    for char, count in sorted_freq:
        print(f"'{char}': {count}")
input_str = input("Enter a string: ")
char_frequency(input_str)
