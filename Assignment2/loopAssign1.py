# Abbie Dyck
# 110046150

originalText = input()
reversedText = ""

for i in range(1, len(originalText) + 1):
    reversedText += originalText[len(originalText) - i]
print(reversedText)
