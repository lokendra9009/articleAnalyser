#!/usr/bin/env python

from textblob import TextBlob
# from wordcloud import WordCloud


# txt = """Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the inter
# actions between computers and human (natural) languages."""


"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud

# d = path.dirname(_)

# Read the whole text.
text = open(r'/Users/lokendrasc/projects/constitutions.txt').read()

# print (text)

# print (type(text))

blob = TextBlob(text)

noun = blob.noun_phrases

# Generate a word cloud image
wordcloud = WordCloud().generate(str(noun))

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()