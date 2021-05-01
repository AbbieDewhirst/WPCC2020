# Abbie Dyck
# 110046150
def removePunctuation(line):
    return line.strip(" .,?;!:[]-")


dictionaryFile = open('dictionary.txt', 'r')
storyFile = open('story.txt', 'r')

dictionaryWords = dictionaryFile.read()
dictionaryWords = dictionaryWords.strip().split("\n")

story = storyFile.read()
story = story.strip().split("\n")
wordsInStory = []

for i in range(len(dictionaryWords)):
    dictionaryWords[i] = dictionaryWords[i].lower()

for i in range(len(story)):
    words = story[i].split(" ")
    for n in range(len(words)):
        words[n] = words[n].lower()
        words[n] = removePunctuation(words[n])
        wordsInStory.append(words[n])

wordsNotInDict = []

for i in range(len(wordsInStory)):
    if wordsInStory[i] not in dictionaryWords and wordsInStory[i] != '':
        wordsNotInDict.append(wordsInStory[i])

print("Words in story that are not in dictionary:")
print(wordsNotInDict)

storyFile.close()
dictionaryFile.close()
