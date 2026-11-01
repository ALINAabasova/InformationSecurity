#!/usr/bin/env python3
import sys
import itertools

def mutate(word):
    out = {word, word.lower(), word.upper(), word.capitalize()}
    leet = word.lower().replace("a", "@").replace("o", "0").replace("i", "1").replace("e", "3")
    out.add(leet)
    return out

def generate(first, last, birth_year):
    base = set()
    for w in (first, last):
        base |= mutate(w)
    base |= {birth_year, birth_year[-2:]}
    results = set(base)
    suffixes = ["", "123", "!", "@", birth_year, birth_year[-2:], "1"]
    for w in base:
        for s in suffixes:
            results.add(w + s)
    for a, b in itertools.permutations([first, last, birth_year], 2):
        results.add(a + b)
        results.add(a.capitalize() + b)
    return sorted(r for r in results if r)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: gen_wordlist.py <first> <last> <birth_year>")
        sys.exit(1)
    for pw in generate(sys.argv[1], sys.argv[2], sys.argv[3]):
        print(pw)
