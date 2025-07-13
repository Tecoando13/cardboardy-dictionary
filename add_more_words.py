import json

with open("./data/stabledictionary.json", "r") as f:
    dictionary = json.load(f)

with open("Unattested words.txt", "r") as f:
    unattested_words = f.read().splitlines()

unattested_words = [l.strip().split(" - ") for l in unattested_words]

for word, definition in unattested_words:
    dictionary[word] = [{"definition": definition, "tags": ["unverified"]}]

with open("./data/latestdictionary.json", "w") as f:
    json.dump(dictionary, f, indent=2, ensure_ascii=False)