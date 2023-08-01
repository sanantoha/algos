
# O(n * log(n)) time | O(1) space
def optimalFreelancing(jobs):
    LENGTH_OF_WEEK = 7
    profit = 0
    jobs.sort(key=lambda job: job['payment'], reverse=True)

    timeline = [False] * LENGTH_OF_WEEK

    for job in jobs:
        maxTime = min(job['deadline'], LENGTH_OF_WEEK)
        for time in reversed(range(maxTime)):
            if not timeline[time]:
                profit += job['payment']
                timeline[time] = True
                break

    return profit


if __name__ == '__main__':
    input = [{"deadline": 1, "payment": 1}]
    actual = optimalFreelancing(input)
    print(actual)
    assert actual == 1

    input = [
        {
            "deadline": 2,
            "payment": 2
        },
        {
            "deadline": 4,
            "payment": 3
        },
        {
            "deadline": 5,
            "payment": 1
        },
        {
            "deadline": 7,
            "payment": 2
        },
        {
            "deadline": 3,
            "payment": 1
        },
        {
            "deadline": 3,
            "payment": 2
        },
        {
            "deadline": 1,
            "payment": 3
        }
    ]
    actual = optimalFreelancing(input)
    print(actual)
    assert actual == 13