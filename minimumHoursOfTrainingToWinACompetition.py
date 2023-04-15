# __Big O Time__
# The big O time complexity of this algorithm is O(n) where n is the size of list energy/experience as energy and experience are both size n. This is because to calculate the energy, the sum
# function runs through the entire energy list which is n. Then to calculate the total experience needed it runs through the experience list once and gives another n time. This gives us O(2n)
# which is just O(n). This is a reasonable time complexity as you will have to check each energy and experience at least once to make sure your initial numbers can beat the rest of the list.

# __Space Complexity__
# The space complexity of this algorithm is O(1). This is because there are only 2 integers being created and those do not rely on any sort of input size. This is a good space complexity as O(1) is
# the most optimal

def minNumberOfHours(initialEnergy, initialExperience, energy, experience):
    # Calculating total energy
    enemyEnergy = sum(energy)
    if enemyEnergy >= initialEnergy:
        output = enemyEnergy - initialEnergy + 1
    else:
        output = 0
    
    currentExperience = initialExperience
    for enemyExperience in experience:
        if currentExperience <= enemyExperience:
            output += enemyExperience-currentExperience+1
            currentExperience = enemyExperience+1+enemyExperience
        else:
            currentExperience += enemyExperience
    
    return output

if __name__ == "__main__":
    print(minNumberOfHours(7, 2, [1,1,1,1,1], [1,2,6,10,23]))

