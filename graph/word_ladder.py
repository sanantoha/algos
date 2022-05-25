from collections import deque

# O(l ^ 2 * n) time | O(l ^ 2 * m) space
def ladderLength(beginWord, endWord, wordList):

    if not beginWord or not endWord or endWord not in wordList:
        return 0

    adjList = {}

    for word in wordList:
        for i in range(len(word)):
            key = word[:i] + '*' + word[i + 1:]
            adjList[key] = adjList.get(key, []) + [word]


    queue = deque()
    queue.append((beginWord, 1))
    visited = {beginWord}

    while queue:
        currWord, level = queue.popleft()

        for i in range(len(currWord)):
            key = currWord[:i] + '*' + currWord[i + 1:]
            for word in adjList.get(key, []):
                if endWord == word:
                    return level + 1

                if word not in visited:
                    visited.add(word)
                    queue.append((word, level + 1))


    return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    actual = ladderLength(beginWord, endWord, wordList)
    print(actual)
    assert actual == 5