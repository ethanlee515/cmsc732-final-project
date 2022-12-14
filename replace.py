#!/usr/bin/env python

import spacy
import json
# from nltk.corpus import wordnet as wn

spacy_nlp = spacy.load("en_core_web_md")

ppdb_path = "./TASA/auxiliary_data/ppdb_synonym_dict.json"
with open(ppdb_path, "r", encoding="utf-8") as f:
    ppdb_synonyms = json.load(f)

def get_synonyms(word):
    synonyms = list()
    if word in ppdb_synonyms:
        synonyms.extend(ppdb_synonyms[word])
    # TODO Can use wordnet here too
    return synonyms

def is_edit_candidate(token):
    if token.ent_type != 0:
        return False
    if token.is_punct:
        return False
    return token.pos_ in ["VERB", "NOUN", "ADJ", "ADV"]

if __name__ == "__main__":
    sentence = input("Enter the sentence to perturb: ")
    tokens = spacy_nlp(sentence)
    # TODO index?
    edit_candidates = filter(is_edit_candidate, tokens)
    # TODO How to use these?
    # entities = tokens.ents
    for candidate in edit_candidates:
        word = candidate.lemma_
        print(f'"{word}" can be replaced with {get_synonyms(word)}.')


