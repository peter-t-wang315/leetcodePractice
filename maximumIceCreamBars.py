# __Big O time__
# The Big O time complexity of this algorithm is O(n) where n is the size of costs. This is because we go through the entire list of items only 2 times which then boils 
# down to O(n). This is a reasonable time complexity as you have to go through the entire list of costs to know how many bars you can buy.

# __Space complexity__
# The space complexity of this algorithm is O(1). This is because the only variable being created is the barsBought which is a constant integer. This is the best
# space complexity as constant space is the best.

def maxIceCream(costs, coins):
    costs.sort()
    barsBought = 0
    for barCost in costs:
        if coins - barCost > 0:
            barsBought += 1
            coins -= barCost
        elif coins - barCost == 0:
            return barsBought + 1
        else:
            return barsBought
    return barsBought


if __name__ == "__main__":
    print(maxIceCream([1,3,2,4,1], 7))
