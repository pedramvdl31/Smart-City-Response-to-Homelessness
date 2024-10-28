####################################################################
# This is the algorithm that was proposed by Dr. Salimur.
# it will find the min and max of person's risks, subtract them
# and the person with highest risk the first choice 
####################################################################
import funcs
import AllData
import random

people = AllData.getPeople()
shelters = AllData.getShelter()

peopleDuplicate = AllData.getPeople()
sheltersDuplicate = AllData.getShelter()

sheltersCapacity = AllData.getCapacity()

goodnessOfFitArray = AllData.getWeight()
weightsDuplicate = AllData.getWeight()


final_object = {}


def getResults():

    while( len( people ) != 0):
        temp = []
        # For each person, for example 'A':[5,10,15]
        # find the min and max in the array and sutract
        # then save the result in the temp file for that
        # person so that at the end it looks like
        # A:10, B:5, C: 25. So C is more vulnerable.

        for i in range(len(people)):
            _min = min(goodnessOfFitArray[i])
            _max = max(goodnessOfFitArray[i])
            _subtract = _max - _min
            temp.append(_subtract)

        # Find the highest value in the temp object which is the person with highest risk
        highestRiskAmongAll = max(temp)
        mostValnerablePersonIndex = temp.index(highestRiskAmongAll)

        # Find the most vulnerable person best choice that is the highest goodnesssoffit and get that shelter
        while(True):
            mostValnerablePersonBestChoice = min( goodnessOfFitArray[ mostValnerablePersonIndex ] )
            mostValnerablePersonBestChoiceIndex = goodnessOfFitArray[mostValnerablePersonIndex].index(mostValnerablePersonBestChoice)
            mostValnerablePersonBestChoiceShelter = shelters[ mostValnerablePersonBestChoiceIndex ]
            mostValnerablePersonBestChoiceShelterIndex = shelters.index(mostValnerablePersonBestChoiceShelter)

            if sheltersCapacity[ mostValnerablePersonBestChoiceShelterIndex ]>0:
                break
            else:
                del shelters[mostValnerablePersonBestChoiceShelterIndex]
                del sheltersCapacity[mostValnerablePersonBestChoiceShelterIndex]
                for i in range(len(goodnessOfFitArray)):
                    del goodnessOfFitArray[i][mostValnerablePersonBestChoiceShelterIndex]



        #Assign that shelter to that person. we will redece the shelter capacity later
        final_object[ people[mostValnerablePersonIndex] ] = mostValnerablePersonBestChoiceShelter

        #reduce the capacity
        sheltersCapacity[ mostValnerablePersonBestChoiceShelterIndex ] = sheltersCapacity[ mostValnerablePersonBestChoiceShelterIndex ] - 1

        # since this person is assigned delete it, also delete athe corresponding goodnessoffit
        del people[mostValnerablePersonIndex]
        del goodnessOfFitArray[mostValnerablePersonIndex]

        #if shelter has no capacity the delete that too and all the coresponsing gooness of fit and capacity
        if ( sheltersCapacity[ mostValnerablePersonBestChoiceShelterIndex ] == 0 ):

            del shelters[mostValnerablePersonBestChoiceShelterIndex]
            del sheltersCapacity[mostValnerablePersonBestChoiceShelterIndex]
            for i in range(len(goodnessOfFitArray)):
                del goodnessOfFitArray[i][mostValnerablePersonBestChoiceShelterIndex]
    
    output = funcs.FinalObjectAnalysis(final_object,weightsDuplicate,peopleDuplicate,sheltersDuplicate)
    print(output)
    return final_object
