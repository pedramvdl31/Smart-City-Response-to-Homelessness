####################################################################
# This is the Median Algorithm proposed by Dr. Salimur.
# It prioritizes individuals based on the disparity calculated as 
# the difference between the median risk value and the minimum risk.
####################################################################

import funcs
import statistics
import AllData

people = AllData.getPeople()
shelters = AllData.getShelter()

peopleDuplicate = AllData.getPeople()
sheltersDuplicate = AllData.getShelter()

sheltersCapacity = AllData.getCapacity()

goodnessOfFitArray = AllData.getWeight()
weightsDuplicate = AllData.getWeight()

final_object = {}

def getResults():
    iteration = 1

    print("\n" + "=" * 50)
    print("Running Algorithm: Median Algorithm")
    print("=" * 50)

    while len(people) != 0:
        print("\n    " + "=" * 46)
        print(f"    Iteration {iteration}: Current Allocation Process")
        print("    " + "=" * 46)

        temp = []
        print("\n    --- Calculating Disparities (Median - Min Risk) ---")

        # For each person, calculate their disparity
        for i in range(len(people)):
            _median = statistics.median(goodnessOfFitArray[i])
            _distanceFromAverage = _median - min(goodnessOfFitArray[i])
            temp.append(_distanceFromAverage)
            print(f"    Person {people[i]}: Risk Array = {goodnessOfFitArray[i]}, "
                  f"Median = {_median}, Min = {min(goodnessOfFitArray[i])}, Disparity = {_distanceFromAverage}")

        print("\n    --- Disparity Calculations ---")
        for idx, val in enumerate(temp):
            print(f"    Person {people[idx]}: Disparity = {val:.2f}")

        # Find the person with the highest disparity
        highestRiskAmongAll = max(temp)
        mostValnerablePersonIndex = temp.index(highestRiskAmongAll)
        print(f"\n    Person with highest disparity: {people[mostValnerablePersonIndex]}")

        # Assign a shelter to the most vulnerable person
        while True:
            mostValnerablePersonBestChoice = min(goodnessOfFitArray[mostValnerablePersonIndex])
            mostValnerablePersonBestChoiceIndex = goodnessOfFitArray[mostValnerablePersonIndex].index(mostValnerablePersonBestChoice)
            mostValnerablePersonBestChoiceShelter = shelters[mostValnerablePersonBestChoiceIndex]
            mostValnerablePersonBestChoiceShelterIndex = shelters.index(mostValnerablePersonBestChoiceShelter)

            if sheltersCapacity[mostValnerablePersonBestChoiceShelterIndex] > 0:
                break
            else:
                print(f"    Shelter {mostValnerablePersonBestChoiceShelter} is full. Removing it from consideration.")
                del shelters[mostValnerablePersonBestChoiceShelterIndex]
                del sheltersCapacity[mostValnerablePersonBestChoiceShelterIndex]
                for i in range(len(goodnessOfFitArray)):
                    del goodnessOfFitArray[i][mostValnerablePersonBestChoiceShelterIndex]

        # Record assignment
        final_object[people[mostValnerablePersonIndex]] = mostValnerablePersonBestChoiceShelter
        print(f"    Assigned Person {people[mostValnerablePersonIndex]} to Shelter {mostValnerablePersonBestChoiceShelter}")

        # Reduce the shelter's capacity
        sheltersCapacity[mostValnerablePersonBestChoiceShelterIndex] -= 1

        # Remove the assigned person
        del people[mostValnerablePersonIndex]
        del goodnessOfFitArray[mostValnerablePersonIndex]

        # Remove shelter if capacity is zero
        if sheltersCapacity[mostValnerablePersonBestChoiceShelterIndex] == 0:
            print(f"    Shelter {mostValnerablePersonBestChoiceShelter} is now full. Removing it from the pool.")
            del shelters[mostValnerablePersonBestChoiceShelterIndex]
            del sheltersCapacity[mostValnerablePersonBestChoiceShelterIndex]
            for i in range(len(goodnessOfFitArray)):
                del goodnessOfFitArray[i][mostValnerablePersonBestChoiceShelterIndex]

        iteration += 1

    print("\n" + "=" * 50)
    print("Final Assignment Results")
    print("=" * 50)
    output = funcs.FinalObjectAnalysis(final_object, weightsDuplicate, peopleDuplicate, sheltersDuplicate)
    return final_object, output
