#!/usr/bin/env python

import unittest
import perturb
import datasets

class TestPerturb(unittest.TestCase):
    def test_split_context(self):
        context = '''It was the last week of classes. Now we have final exams.
        I did okay on mine.'''
        sentences = perturb.split_context(context)

        offset = sentences[0].offset
        self.assertEqual(context[offset : offset + 6], 'It was')
        offset = sentences[1].offset
        self.assertEqual(context[offset : offset + 6], 'Now we')
        offset = sentences[2].offset
        self.assertEqual(context[offset : offset + 5], 'I did')

    def test_gold_sent(self):
        squad = datasets.load_dataset('squad')
        squad = squad['train']
        row = squad[0]
        answer_start = row['answers']['answer_start'][0]
        context = row['context']
        gold_sent_output = perturb.get_gold_sentence(context, answer_start)
        true_gold_sent = 'It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858.'
        self.assertEqual(gold_sent_output, true_gold_sent)

if __name__ == "__main__":
    unittest.main()
