# Import spacy and English models
import spacy

nlp = spacy.load('en_core_web_md')

doc = nlp(u'I want to play soccer.')

# Get first token of the processed document
token = doc[0]
print(token)

# Print sentences (one sentence per line)
for sent in doc.sents:
    print(sent)

# For each token, print corresponding part of speech tag
for token in doc:
    print('{} - {}'.format(token, token.pos_))

# For a given document, calculate similarity between 'apples' and 'oranges' and 'boots' and 'hippos'


doc = nlp(u"Apples and oranges are similar. Boots and hippos aren't.")
apples = doc[0]
oranges = doc[2]
boots = doc[6]
hippos = doc[8]
print(apples.similarity(oranges))


# Print similarity between sentence and word 'fruit'
apples_sent, boots_sent = doc.sents
fruit = doc.vocab[u'fruit']
print(apples_sent.similarity(fruit))
print(boots_sent.similarity(fruit))


"""
Print all named entities with named entity types

PERSON	People, including fictional.
NORP	Nationalities or religious or political groups.
FAC	Buildings, airports, highways, bridges, etc.
ORG	Companies, agencies, institutions, etc.
GPE	Countries, cities, states.
LOC	Non-GPE locations, mountain ranges, bodies of water.
PRODUCT	Objects, vehicles, foods, etc. (Not services.)
EVENT	Named hurricanes, battles, wars, sports events, etc.
WORK_OF_ART	Titles of books, songs, etc.
LAW	Named documents made into laws.
LANGUAGE	Any named language.
DATE	Absolute or relative dates or periods.
TIME	Times smaller than a day.
PERCENT	Percentage, including ”%“.
MONEY	Monetary values, including unit.
QUANTITY	Measurements, as of weight or distance.
ORDINAL	“first”, “second”, etc.
CARDINAL	Numerals that do not fall under another type.
"""

# doc = nlp("Jennifer speaks German and she runs on Tuesday")
# for ent in doc.ents:
#     print('{} - {}'.format(ent.text, ent.label_))

# For a given document, calculate similarity between 'apples' and 'oranges' and 'boots' and 'hippos'
doc = nlp(u"soccer and baseball are similar. Boots and hippos aren't.")
soccer = doc[0]
baseball = doc[2]
boots = doc[6]
hippos = doc[8]
print(soccer.similarity(baseball))
print(boots.similarity(hippos))
print(soccer.similarity(boots))
print(soccer.similarity(hippos))

print()
# Print similarity between sentence and word 'fruit'
soccer_sent, boots_sent = doc.sents
sports = doc.vocab[u'sports']
print(soccer_sent.similarity(sports))
print(boots_sent.similarity(sports))