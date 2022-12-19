# CMSC 732 Final Project

Attacks on question-answer systems

Group project between 3 grad students

## Perturb results

Perturbed SQuAD validation set can be found in "perturbed.json". Some stats:
* Running time: 83 seconds
* no keywords found: 1965
* Keyword found, but no synonyms found: 793
* Successful perturbs = 7812

### Perturb training set too

* no keywords count = 19309
* no synonyms count = 5926
* successful perturbs = 62364
* Time: 10m46s

### More stats

```
number of rows = 87599
keyword counts = defaultdict(<class 'int'>, {1: 22940, 0: 19309, 2: 19429, 3: 12628, 4: 6964, 5: 3343, 6: 1637, 7: 804, 8: 305, 9: 140, 12: 12, 10: 56, 11: 23, 15: 2, 13: 5, 19: 1, 16: 1})
synonym counts = defaultdict(<class 'int'>, {2: 5278, 9: 2320, 8: 2952, 4: 5037, 3: 4530, 0: 5969, 1: 6023, 5: 4422, 15: 1579, 6: 3811, 7: 3412, 29: 323, 13: 2614, 10: 1966, 20: 991, 16: 1302, 38: 76, 24: 838, 12: 1677, 60: 137, 17: 1175, 11: 1458, 18: 1637, 22: 612, 21: 1452, 68: 31, 19: 537, 28: 334, 36: 293, 14: 1290, 37: 224, 27: 323, 39: 274, 23: 304, 26: 468, 33: 202, 41: 395, 34: 162, 52: 4, 61: 189, 53: 191, 54: 41, 32: 466, 46: 34, 31: 232, 25: 228, 43: 81, 49: 122, 44: 12, 35: 53, 42: 24, 58: 10, 30: 67, 40: 25, 50: 73, 47: 5, 48: 4, 65: 1})
successful perturbs = 62321
```
