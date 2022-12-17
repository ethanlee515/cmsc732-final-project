#!/usr/bin/env python

import datasets
import nltk
from dataclasses import dataclass
import spacy
import replace
import random
import json

spacy_tokenizer = spacy.load("en_core_web_md")

@dataclass
class ContextSentence:
    content: str
    offset: int

def split_context(context):
    sentences = nltk.sent_tokenize(context)
    result = list()
    offset = 0
    for sentence in sentences:
        while context[offset : offset + len(sentence)] != sentence:
            offset += 1
        result.append(ContextSentence(sentence, offset))
    return result

def get_gold_sentence(context, answer_start):
    sentences = split_context(context)
    for i in range(len(sentences)):
        if sentences[i].offset >= answer_start:
            return sentences[i - 1].content
    return sentences[-1].content

def get_overlaps(question, gold_sentence, answer):
    question_tokens, gold_tokens, answer_tokens = spacy_tokenizer.pipe([question, gold_sentence, answer])
    question_tokens = set(token.lemma_ for token in question_tokens
            if replace.is_edit_candidate(token))
    gold_tokens = set(x.lemma_ for x in gold_tokens)
    answer_tokens = set(x.lemma_ for x in answer_tokens)
    return (question_tokens & gold_tokens) - answer_tokens
    
if __name__ == "__main__":
    squad = datasets.load_dataset('squad')
    squad = squad['validation']
    no_keyword_count = 0
    no_synonym_count = 0
    output_rows = list()
    for i in range(len(squad)):
        row = squad[i]
        # TODO multiple answers
        answer = row['answers']['text'][0]
        answer_start = row['answers']['answer_start'][0]

        gold_sentence = get_gold_sentence(row['context'], answer_start)

        overlaps = get_overlaps(row['question'], gold_sentence, answer)
        if len(overlaps) == 0:
            no_keyword_count += 1
            # print(f"row {i}: no keyword found")
            continue
        keyword = random.choice(list(overlaps))
        synonyms = replace.get_synonyms(keyword)
        if len(synonyms) == 0:
            no_synonym_count += 1
            # print(f'row {i}: no synonyms found for "{keyword}"')
            continue
        synonym = random.choice(list(synonyms))
        perturbed = row['question'].replace(keyword, synonym)
        # print(f"row {i}: original question = {row['question']}")
        # print(f"row {i}: perturbed question = {perturbed}")
        output_rows.append({
            "title": row["title"],
            "id": row["id"],
            "context": row["context"],
            "question": perturbed,
            "answers": {
                "answer_start": [answer_start],
                "text": [answer]
            }
        })
    print(f"no keywords count = {no_keyword_count}")
    print(f"no synonyms count = {no_synonym_count}")
    print(f"successful perturbs = {len(output_rows)}")
    with open('perturbed.json', 'w') as output_file:
        json.dump({"data": output_rows}, output_file)
