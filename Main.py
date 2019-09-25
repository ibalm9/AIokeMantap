from GeneticAlgorithm import GeneticAlgorithm
import time

startTime = time.time()

def function(x, y):
    # funkcja Rosenbrocka: (1-x)*(1-x) + 100*(y-x*x)*(y-x*x)
    return (1-x)*(1-x) + 100*(y-x*x)*(y-x*x)

numberOfPopulationMembers = 10
percentOfBestOnesToLive = 0.8
searchingSection = [-3, 3]

GA = GeneticAlgorithm(numberOfPopulationMembers, percentOfBestOnesToLive, searchingSection, function)

#wydrukowanie wyniku:
print ("Searching approximated minimum...")
minimumValue = GA.searchMinimum(iterations=1000)
minimumPoint = GA.getArgumentsOfMinimumValue()
print ("Found minimum ", minimumValue, " at point ", minimumPoint)
print("Searching time: %s seconds." % (time.time() - startTime))
