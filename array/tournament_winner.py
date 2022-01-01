
# O(n) time | O(k) space - where n is number of competitions and k is number of teams
def tournament_winner(competitions, results):
    winner = ""
    points = {winner: 0}

    for i, competition in enumerate(competitions):
        home_team, away_team = competition
        res = results[i]

        winning_team = home_team if res == 1 else away_team

        curr_points = points.get(winning_team, 0)
        points[winning_team] = curr_points + 3
        if points[winning_team] > points[winner]:
            winner = winning_team

    return winner


if __name__ == '__main__':
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]

    results = [0, 0, 1]

    print(tournament_winner(competitions, results))
