# __Big O Time__
# The big O time complexity of this algorithm is O(n+m) where n is the amount of roads and m is the amount of cities. This is because we iterate over every road and then
# city as well when checking which towns connect to 1 and making sure we don't revisit a city. This is a reasonable time complexity as you have to check every road
# and city to check which is A) the shortest path B) a connecting city from 1 to n.

# __Space Complexity__
# The space complexity of this algorithm is O(n) where n is the amount of paths. This is because we create a dictionary of all cities and their paths. This is a reasonable
# space complexity as you have to know which paths actually connect 1-n. My way of doing this was creating an extra dictionary that acts as a tree.

from typing import DefaultDict
import math

def minScore(n, roads):
    connections = DefaultDict(list)
    for a,b,distance in roads:
        connections[a].append([b,distance])
        connections[b].append([a,distance])
    
    minimum = [math.inf]
    visited = set()

    def dfs(node):
        visited.add(node)

        for city, distance in connections[node]:
            minimum[0] = min(minimum[0], distance)
            if city not in visited:
                dfs(city)

    dfs(1)

    return minimum[0]

if __name__ == "__main__":
    print(minScore(7,[[1,3,1484],[3,2,3876],[2,4,6823],[6,7,579],[5,6,4436],[4,5,8830]]))