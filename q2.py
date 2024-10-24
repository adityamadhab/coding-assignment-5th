def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    freq1 = {}
    freq2 = {}
    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1
    
    for char in str2:
        freq2[char] = freq2.get(char, 0) + 1
    return freq1 == freq2

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if are_anagrams(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
