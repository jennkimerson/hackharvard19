# spaCy v2.2.0 · Python 3
import spacy

# Load the pre-installed spacy model
nlp = spacy.load('en_core_web_md')



# User input: List of interests (elements)

# TODO
# Here, assume that user input is simply verb or noun or verb + noun form.
# Future iterations should noun chunk to seperate out the rest of the adjuncts

# user_a, main user
a = [nlp(u'play football'), nlp(u'study biology'), nlp(u'build a computer')]

# user_x, no
x = [nlp(u'fashion'), nlp(u'listen to music'), nlp(u'discuss politics')]

# user_y
y = [nlp(u'play golf'), nlp(u'study math'), nlp(u'play piano')]

# user_z
z = [nlp(u'play football'), nlp(u'study biology'), nlp(u'build a computer')]



# Part-of-speech (POS) Tagging
# Determinds the part of speech of each token / word inputted by the user
ent_a = [[token.pos_ for token in element] for element in a]
ent_x = [[token.pos_ for token in element] for element in x]
ent_y = [[token.pos_ for token in element] for element in y]
ent_z = [[token.pos_ for token in element] for element in z]

entries = [ent_a, ent_x, ent_y, ent_z]
print(entries)

 

# # Calculate cosine distance:

# # If element has more than one token, then we must weight and "merge" them into one vector
# # TODO
# # Here, noun is prioritized over verb if user input was verb + noun --> (0.5(verb)*noun)1.5
# # Must test and fine-tune the values

# v_a = [[token.vector for token in element] for element in a]
# v_x = [[token.vector for token in element] for element in x]
# v_y = [[token.vector for token in element] for element in y]
# v_z = [[token.vector for token in element] for element in z]


# vectors = [v_a, v_x, v_y, v_z]
# print(vectors)

# # for ent in entries:
# #     for element in ent:
# #         if len(element) != 1: #  and (element[0].pos_ == 'VERB' and element[1].post_ == 'NOUN')
# #             vector = (0.5*element[0].token.vector + element[1].token.vector)/1.5
# #         else:
# #             vector = element.token.vector_norm
# #     print(vector)
# #