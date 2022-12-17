#!/usr/bin/env python

import unittest
import perturb

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

if __name__ == "__main__":
    unittest.main()
