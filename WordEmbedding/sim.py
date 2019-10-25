import spacy

nlp = spacy.load('en_core_web_md')

doc = nlp(u'football soccer baseball')
football = doc[0]
soccer = doc[1]
baseball = doc[2]
print(football.similarity(soccer))
print(football.similarity(baseball))
print(baseball.similarity(soccer))

# simulates 2 users
doc1 = nlp(u'football')
football = doc1[0]

doc2 = nlp(u'soccer')
soccer = doc2[0]


print(football.similarity(soccer))