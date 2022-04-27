def findrepeats(txt):
    seen = set()
    dupes = set()
    for char in txt:
        if char in seen:
            dupes.add(char)
        seen.add(char)
        
    return len(dupes)
print(findrepeats('1124443hhhikk'))