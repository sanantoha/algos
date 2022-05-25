from collections import deque

def findLadders(beginWord, endWord, wordList):
    if not beginWord or not endWord or endWord not in wordList:
        return []

    paths = []

    adjList = {}
    for word in wordList:
        for i in range(len(word)):
            key = word[:i] + '*' + word[i + 1:]
            adjList[key] = adjList.get(key, []) + [word]

    queue = deque()
    queue.append((beginWord, [beginWord]))

    visited = set([beginWord])

    while queue:
        size = len(queue)

        currVisited = set([])

        while size > 0:
            size -= 1
            currWord, currWordSeq = queue.popleft()

            if currWord == endWord:
                paths.append(currWordSeq)
                continue

            for i in range(len(currWord)):
                key = currWord[:i] + '*' + currWord[i + 1:]
                for word in adjList.get(key, []):

                    if word not in visited:
                        currVisited.add(word)
                        queue.append((word, currWordSeq[:] + [word]))

        visited.update(currVisited)

    return paths


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    actual = findLadders(beginWord, endWord, wordList)
    print(actual)
    assert actual == [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]