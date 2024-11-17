####################################################################
# LOCAL SEARCH ALGORITHM
####################################################################
import statistics
import funcs
import time
import AllData

weights = AllData.getWeight()
people = AllData.getPeople()
shelters = AllData.getShelter()

def getLocalSearch(final_object):
    print("\n" + "=" * 40)
    print("         LOCAL SEARCH ALGORITHM         ")
    print("=" * 40)

    start_time = time.time()

    flag = True
    iteration = 0  # Count iterations
    specialCounter = 0

    while flag:
        iteration += 1
        flag = False

        m = 0
        valuneableIndex = None
        valuneableName = None
        vulnerableShelter = None

        # Find the person with the maximum assigned weight
        for person in final_object:
            shelter = final_object[person]
            w = weights[people.index(person)][shelters.index(shelter)]
            if w > m:
                m = w
                valuneableName = person
                valuneableIndex = people.index(person)
                vulnerableShelter = shelter

        # Attempt to swap assignments
        for key in range(len(people)):
            if valuneableIndex != key:
                SwapWeight = weights[key][shelters.index(final_object[valuneableName])]
                _person = people[key]
                _personShelter = final_object[_person]
                _shelterIndex = shelters.index(_personShelter)
                _SwapWeight = weights[valuneableIndex][_shelterIndex]

                if SwapWeight < m and _SwapWeight < m:
                    specialCounter += 1
                    print(f"\nIteration {iteration}: Swap Found")
                    print(f"  Counter: {specialCounter}")
                    print(f"  Max Assigned Weight: {m}")
                    print(f"  Swap A Weight: {SwapWeight}")
                    print(f"  Swap B Weight: {_SwapWeight}")
                    print(f"  Swapping '{valuneableName}' and '{_person}'")
                    final_object[valuneableName] = _personShelter
                    final_object[_person] = vulnerableShelter
                    flag = True
                    break

    output = funcs.FinalObjectAnalysisLOCALSEARCH(final_object, weights, people, shelters)

    # Print the final results
    print("\n" + "-" * 40)
    print(f"FINAL OBJECTIVE RESULTS (After Local Search):\n{output}")
    print(f"Total Iterations: {iteration}")
    print(f"Execution Time: {time.time() - start_time:.6f} seconds")
    print("=" * 40)

    return output
