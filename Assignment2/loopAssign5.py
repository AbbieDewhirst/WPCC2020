# Abbie Dyck
# 110046150

word = input()
word = word + word[0]

out = ""

for i in range(len(word)):
    out += word[len(word) - i - 1]

print(word)

for i in range(1, len(word) - 1):
    print(out[i], end=" " * (len(word) - 2))
    print(word[i])

print(out)
