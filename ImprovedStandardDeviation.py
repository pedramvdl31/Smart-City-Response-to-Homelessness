####################################################################
# This is the Standard Deviation Algorithm proposed by Dr. Salimur.
# It prioritizes the individual with the highest disparity calculated
# as the standard deviation of risks minus the minimum risk value.
####################################################################

import funcs
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
    print("Running Algorithm: Standard Deviation Algorithm")
    print("=" * 50)

    while len(people) != 0:
        print("\n    " + "=" * 46)
        print(f"    Iteration {iteration}: Current Allocation Process")
        print("    " + "=" * 46)

        temp = []
        print("\n    --- Calculating Disparities (Std Dev - Min Risk) ---")
        
        # For each person, calculate their risk disparity
        for i in range(len(people)):
            if len(goodnessOfFitArray[i]) > 1:
                _standardDeviation = funcs.sd_calc(goodnessOfFitArray[i])
                _distanceFromAverage = _standardDeviation - min(goodnessOfFitArray[i])
                temp.append(_distanceFromAverage)
                print(f"    Person {people[i]}: Risk Array = {goodnessOfFitArray[i]}, "
                      f"Std Dev = {_standardDeviation:.2f}, Disparity = {_distanceFromAverage:.2f}")
            else:
                temp.append(goodnessOfFitArray[i][0])
                print(f"    Person {people[i]}: Only one risk value = {goodnessOfFitArray[i][0]}")

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
