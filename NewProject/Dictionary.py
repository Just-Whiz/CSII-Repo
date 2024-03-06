def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def most_common-words(freqs):
values = freqs.values()
best = max(values)
words = []
for k in freqs: 
    if freqs[k] == best
return 