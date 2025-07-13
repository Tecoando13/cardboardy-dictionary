import json

with open("data/dictionary.json", "r") as file:
    dict_data = json.load(file)

dictionary2 = {}

suffixes = dict_data["suffixes"]
suffixes = list(suffixes.keys())

for suffix in suffixes:
    suffix2 = "-" + suffix
    definitions = dict_data["suffixes"][suffix]
    definitions2 = []

    for definition in definitions:
        definition2 = []
        tags = []
        if definition[0].isdigit():
            definition = " ".join(definition.split(" ")[1:])
        
        words = definition.split(" ")
        for word in words:
            if word.startswith("<") and word.endswith(">"):
                tags.append(word[1:-1])
            else:
                if "|" in word:
                    word = word.split("|")[-1]
                definition2.append(word)
        definition2 = " ".join(definition2)
        definitions2.append({"definition": definition2, "tags": tags})

    dictionary2[suffix2] = definitions2

for entry in dict_data["words"]:
    definitions = dict_data["words"][entry]
    definitions2 = []

    for definition in definitions:
        definition2 = []
        tags = []
        if definition[0].isdigit():
            definition = " ".join(definition.split(" ")[1:])
        
        words = definition.split(" ")
        for word in words:
            if word.startswith("<") and word.endswith(">"):
                tags.append(word[1:-1])
            else:
                if "|" in word:
                    word = word.split("|")[-1]
                definition2.append(word)
        definition2 = " ".join(definition2)
        definitions2.append({"definition": definition2, "tags": tags})

    dictionary2[entry] = definitions2
    print(entry)

with open("data/dictionary2.json", "w") as file:
    json.dump(dictionary2, file, indent=4, ensure_ascii=False)  # Ensure proper formatting and encoding
print("Dictionary conversion completed successfully.")