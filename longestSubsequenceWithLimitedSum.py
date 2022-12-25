# __Big O time__
# The big O time of this algorithm is O(n^2) where n is the size of the largest inputted list. This is because we go through every item in nums len(queries) times. This time complexity is ok and can possible
# be improved on as O(n^2) can be reduced to something like O(logn) or O(n). TBH I'm not going to think much harder because it is Christmas.

# __Space complexity__
# The space complexity for this algorithm is O(n) where n is the size of queries. This is because our answers return value has to have an answer for every item in queries. This is a good space complexity
# for this question because you have to return an answer for every query

def answerQueries(nums, queries):
    nums.sort()
    answer = []
    subsequenceCount = 0
    for queriedNum in queries:
        for num in nums:
            if queriedNum - num >= 0:
                queriedNum -= num
                subsequenceCount += 1
        answer.append(subsequenceCount)
        subsequenceCount = 0
    return answer


if __name__ == "__main__":
    print(answerQueries([1,4,5,2,1,1,1,1], [8,4,21]))