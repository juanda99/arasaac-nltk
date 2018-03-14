# get all data from a word in a language defined by language variable

from nltk.corpus import wordnet as wn
import pprint
from itertools import chain

# get all languages 
sorted(wn.langs())

input = input("Enter word code to get hyponyms and hypernyms: ")
language = 'spa'
word = wn.synset(input)

pp = pprint.PrettyPrinter(indent=4)

dict = {
  'id': input, 
  'word': word.lemma_names(language), 
  'meaning': word.definition(),
  'hypernyms': [],
  'hyponyms': []
}

currentHyponyms = []
currentHypernyms = []

for hyponym in word.hyponyms():
  currentHyponyms.append(hyponym.lemma_names(language))

flat_list = [item for sublist in currentHyponyms for item in sublist]
dict["hyponyms"] = flat_list

for hypernym in word.hypernyms():
  currentHypernyms.append(hypernym.lemma_names(language))

flat_list = [item for sublist in currentHypernyms for item in sublist]
dict["hypernyms"] = flat_list

pp.pprint(dict)
