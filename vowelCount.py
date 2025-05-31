text = input("Enter any word or sentence: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Vowel Count: ", count)