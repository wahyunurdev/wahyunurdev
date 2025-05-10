import sys
import difflib

r = open('2.txt', 'r', encoding="utf-8")
reference = r.readlines()

h = open('3.txt', 'r', encoding="utf-8")
hypothesis = h.readlines()

result = difflib.SequenceMatcher(None, reference, hypothesis)
blox = result.get_matching_blocks()
result.find_longest_match(0, len(reference), 0, len(hypothesis))
print(result.find_longest_match(0, len(reference), 0, len(hypothesis)))
print(result.ratio())

for x in blox:
    print(reference[x.a:x.a+x.size])

