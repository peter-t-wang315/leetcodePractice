# __Big O time__
# The big O time complexity of this algorithm is O(n) where n is the number of edges. This is because at most, each edge is iterated over twice. This is a reasonable time complexity as you have to iterate
# over each edge at least once to know how to traverse the tree.

# __Space complexity__
# The space complexity of this algorithm is O(n) where n is the size of edges. This is because we create a dictionary with every edge. This is a reasonable time complexity because the only way to lower 
# the space complexity one would have to sacrifice time complexity.


def minTime(n, edges, hasApple):
    tree = {}
    seen_before = set()
    for i in range(len(hasApple)):
        tree[i] = []
    for parent, child in edges:
        tree[child].append(parent)
        tree[parent].append(child)
        
    return findApplePaths(0, hasApple, tree, seen_before)


def findApplePaths(current, hasApple, tree, seen_before):
    time = 0
    seen_before.add(current)
    for branch in tree[current]:
        if branch in seen_before:
            continue
        time += findApplePaths(branch, hasApple, tree, seen_before)
    if (hasApple[current] == 1 or time != 0) and current != 0:
        time+=2

    return time


if __name__ == "__main__":
    print(minTime(4, [[0,2],[0,3],[1,2]], [False,True,False,False]))