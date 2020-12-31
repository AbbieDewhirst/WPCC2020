# Abbie Dyck
# 110046150

originalText = input()
lastChar = ""
endText = ""

for i in originalText:
    if lastChar == " " and i == " ":
        i = ""
    else:
        lastChar = i
        endText += i
print(endText)
