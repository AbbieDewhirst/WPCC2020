# Abbie Dyck
# 110046150
# I am aware that this program isn't complete. Yes, it's possible I procrastinated with these programs
# and didn't give myself enough time to finish. Hopefully q1 and q2 are correct, and I can do better on the bonus
# (that is if I don't procrastinate again and actually get them done)
# If you're still reading here, thanks for being a marker for WPCC. I appreciate that you all have volunteered your time
# for the rest of us to gain some experience.

def fixedChecker(match):
    details = match.split(",")
    details[1], details[2], details[4], details[5] = int(details[1]), int(details[2]), int(details[4]), int(details[5])
    details = organizeMatches(details)
    if checkScore(details) and checkRank(details) and betsCheck(details):
        return details
    return []


def organizeMatches(match):
    teamOneRank = rank.index(match[team1])
    teamTwoRank = rank.index(match[team2])

    if teamOneRank < teamTwoRank:
        teamOneCopy = match[:team2]
        match[team1], match[score1], match[bets1] = match[team2], match[score2], match[bets2]
        match[team2], match[bets2], match[bets2] = teamOneCopy[0], teamOneCopy[1], teamOneCopy[2]

    return match


def checkScore(match):
    return match[score1] > match[score2]


def checkRank(match):
    teamOneRank = rank.index(match[team1])
    teamTwoRank = rank.index(match[team2])

    if teamOneRank - teamTwoRank >= 10:
        return True
    return False


def betsCheck(match):
    return (match[bets1] / (match[bets1] + match[bets2])) > 0.8


team1, score1, bets1, team2, score2, bets2 = 0, 1, 2, 3, 4, 5

rankFile = open("ranks.txt", "r")
rank = rankFile.read()
rank = rank.strip().split("\n")

matchesFile = open("matches.txt", "r")
matches = matchesFile.read()
matches = matches.strip().split("\n")

print("FIXED MATCHES:")
print("Underdog\t\t Rank\tScore  Bets    vs Favourite\t\t   Rank   Score  Bets")

rankFile.close()
matchesFile.close()
