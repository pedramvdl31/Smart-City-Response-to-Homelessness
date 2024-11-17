import ImprovedStandardDeviation
import ImprovedMedianAlgo
import ImprovedAverageAlgo
import ImprovedMinMaxAlgo
import LocalSearchSwap
import time

# Placeholder for results
results = []

# Standard Deviation Algorithm
start_time = time.time()
final_object, output_stdev = ImprovedStandardDeviation.getResults()
local_search_stdev = LocalSearchSwap.getLocalSearch(final_object)
execution_time_stdev = time.time() - start_time
results.append(("Standard Deviation", output_stdev, local_search_stdev, execution_time_stdev))

# Median Algorithm
start_time = time.time()
final_object, output_median = ImprovedMedianAlgo.getResults()
local_search_median = LocalSearchSwap.getLocalSearch(final_object)
execution_time_median = time.time() - start_time
results.append(("Median", output_median, local_search_median, execution_time_median))

# Min-Max Algorithm
start_time = time.time()
final_object, output_minmax = ImprovedMinMaxAlgo.getResults()
local_search_minmax = LocalSearchSwap.getLocalSearch(final_object)
execution_time_minmax = time.time() - start_time
results.append(("Min-Max", output_minmax, local_search_minmax, execution_time_minmax))

# Average Algorithm
start_time = time.time()
final_object, output_avg = ImprovedAverageAlgo.getResults()
local_search_avg = LocalSearchSwap.getLocalSearch(final_object)
execution_time_avg = time.time() - start_time
results.append(("Average", output_avg, local_search_avg, execution_time_avg))

# Display all results in a single table
print("\n" + "=" * 85)
print("                       FINAL OUTPUT SUMMARY                       ")
print("=" * 85)
print(f"{'Algorithm':<20}{'Output':<30}{'Local Search Output':<30}{'Execution Time (s)':<15}")
print("-" * 85)
for algorithm, output, local_search_output, exec_time in results:
    print(f"{algorithm:<20}{str(output):<30}{str(local_search_output):<30}{exec_time:.6f}")
print("=" * 85)
