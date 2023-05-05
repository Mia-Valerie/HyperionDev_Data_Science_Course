import spacy
nlp = spacy.load('en_core_web_md')

# Finding similarities between words
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Output:
# 0.5929929675536907
# 0.4041501317354622
# 0.22358825939615987

# The similarity was highest between cat and monkey. It is likly that this is because they are both animals.
# The similarity between bannana and monkey was higher than that between bannana and cat. It is likly that this is due to the association between monkeys and bannanas.

# An example of my own
word1 = nlp("sailing")
word2 = nlp("surfing")
word3 = nlp("sea")
sim1 = str(word1.similarity(word2))
sim2 = str(word3.similarity(word2))
sim3 = str(word3.similarity(word1))

print("The similarity between \'sailing\' and \'surfing\' is " + sim1)
print("The similarity between \'sea\' and \'surfing\' is " + sim2)
print("The similarity between \'sea\' and \'sailing\' is " + sim3)

#Working with vectors
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Working with sentences
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# Running the example file with 'en_core_web_sm' will produce less accurate judgments when using Doc.similarity.
# This is because 'en_core_web_sm' is relying on context sensitive sesors rather than word vectors which are avalible in 'en_core_web_md'