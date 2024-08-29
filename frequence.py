import string
import re
fr = {}
def stat(text):
    for i in string.ascii_uppercase:
        fr[i] = round(text.count(i)/len(text) * 100, 5)
    letters = list(fr.keys())
    frequencies = list(fr.values())
    return dict(sorted(fr.items(),reverse=True, key=lambda item: item[1]))