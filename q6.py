def count_words(input_file, output_file):
    word_count = {}
    
    with open(input_file, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?"\'')
                word_count[word] = word_count.get(word, 0) + 1
    
    with open(output_file, 'w') as file:
        for word, count in sorted(word_count.items()):
            file.write(f"{word}: {count}\n")

input_file = 'input.txt'
output_file = 'output.txt'

count_words(input_file, output_file)
