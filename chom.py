#!/usr/bin/env python

from fileinput import input as stdin
from json import dumps, loads

def get_text_from_stdin():
    text = []
    for line in stdin([]):
        text.append(line.rstrip())
    while text and not text[0].startswith('{'):
        text = text[1:]
    return '\n'.join(text)

def replace_annoying_chars(text):
    t = text
    replacements = [
        ("'", '"'),
        ('u"', '"'),
        ("True", '"True"'),
        ("False", '"False"'),
        ("None", '"None"'),
        ("<", '"<'),
        (">", '>"'),
        ]

    for a, b in replacements:
        t = t.replace(a, b)
    return t


if __name__ == '__main__':
    from sys import argv
    text = get_text_from_stdin()
    text = replace_annoying_chars(text)
    obj = loads(text)
    for key in argv[1:]:
        try:
            obj = obj[key]
        except TypeError:
            obj = obj[int(key)]

    print dumps(obj, sort_keys=True, indent=2)
