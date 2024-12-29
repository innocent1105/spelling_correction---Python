# pip install textblob

from textblob import TextBlob

text = TextBlob(input("Enter your text here... "))

# correct the spelling
correct_spelling = text.correct()

print(correct_spelling)