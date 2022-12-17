#!/usr/bin/env python

import datasets
import nltk
from dataclasses import dataclass

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
    pass

if __name__ == "__main__":
    # squad = datasets.load_dataset('squad')
    # squad = squad['validation']
    pass

