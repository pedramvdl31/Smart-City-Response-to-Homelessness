####################################################################
# This is the algorithm that was proposed by Dr. Salimur.
# it will find the min and max of person's risks, subtract them
# and the person with highest risk the first choice 
####################################################################
import funcs
import AllData
import random
import copy
# import scenarioData


people = AllData.people
shelters = AllData.shelters

n = capNum = 1300
# HOMELESS SHELTER WEIGHT GENERATOR
GOF = []
for x in range(0, n):
    GOF.insert(x,[])
    for y in range(0, n):
        GOF[x].append(random.randint(20,100))

goodnessOfFitArray = copy.deepcopy(GOF)

# sheltersCapacity = AllData.sheltersCapacity
weightsDuplicate = copy.deepcopy(GOF)


peopleDuplicate = AllData.peopleDuplicate
sheltersDuplicate = AllData.sheltersDuplicate

shelterNum = 1300
output = []
_sum = 0

for x in range(shelterNum):
    output.append(1)

outputCap = 0
for i in range(len(output)):
    outputCap = outputCap + output[i]

_sum = outputCap

flag = True

while flag:
    
    if _sum >= capNum:
        flag = False
    else:
        _index = random.randint(1,shelterNum-1)
        output[_index] = output[_index] + 1
        _sum = _sum + 1

outputCap = 0
for i in range(len(output)):
    outputCap = outputCap + output[i]

    
sheltersCapacity = output


final_object = {}


def getResults():

    # ************************
    # Shelter List Cleanup
    capzero = []
    for i in range(len(shelters)):
        cap = 0
        try:
            if sheltersCapacity[i]==0:
                capzero.append(i)
        except IndexError:
            capzero.append(i)
    firstIndex = capzero[0]
    lastIndex = capzero[len(capzero)-1]
    del shelters[firstIndex:lastIndex+1]
    for i in range(len(goodnessOfFitArray)):
        del goodnessOfFitArray[i][firstIndex:lastIndex+1]
    # Shelter List Cleanup END
    # ************************

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
