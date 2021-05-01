# Abbie Dyck
# 110046150

def palindrome(string):
    if len(string) < 2:
        return True
    else:
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
        else:
            return False


print(palindrome(str("racecar")))
