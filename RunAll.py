import ImprovedStandardDeviation
import ImprovedMedianAlgo
import ImprovedAverageAlgo
import ImprovedMinMaxAlgo
import LocalSearchSwap
import time

print("========================================")
start_time = time.time()
print('stdev')
final_object = ImprovedStandardDeviation.getResults()
print('With Local Search')
LocalSearchSwap.getLocalSearch(final_object)
print("\n------")
print('median')
final_object = ImprovedMedianAlgo.getResults()
print('With Local Search')
LocalSearchSwap.getLocalSearch(final_object)
print("\n------")
print('minmax')
final_object = ImprovedMinMaxAlgo.getResults()
print('With Local Search')
LocalSearchSwap.getLocalSearch(final_object)
print("\n------")
print('average')
final_object = ImprovedAverageAlgo.getResults()
print('With Local Search')
LocalSearchSwap.getLocalSearch(final_object)
print("------\n")

print("--- %s seconds ---" % (time.time() - start_time))
print("========================================")







