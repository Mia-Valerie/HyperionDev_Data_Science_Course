# importing package 'spaCy, used in NLP
import spacy
nlp = spacy.load('en_core_web_sm')

# Creating list of garden path sentences
gardenpathSentences = ["When John called his old mother was happy", "After the young Londoner had visited his parents prepared to celebrate their anniversary"]
gardenpathSentences.append("Mary gave the child a Band-Aid")
gardenpathSentences.append("That Jill is never here hurts.")
gardenpathSentences.append("The cotton clothing is made of grows in Mississippi.")
print(gardenpathSentences)

# tokenising and performing named entity recognition for sentences in list and printing
for item in gardenpathSentences:
    doc = nlp(item)
    doc.text.split()
    [token.orth_ for token in doc]
    print([(token, token.orth_, token.orth) for token in doc])
    print([(i, i.label_, i.label) for i in doc.ents])


# Asking spacy to define entities
print(spacy.explain('GPE'))
print(spacy.explain('PERSON'))

# I looked up the entity 'GPE' which is defined as 'country, city or state', which makes sense as Mississippi is a state.
# I also looked up 'Person' which is defined as 'people, including fictional', which made sense as all entities with this lable are names or none relating to a person.





