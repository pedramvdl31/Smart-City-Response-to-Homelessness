import string
import random
import math
import sys

####################################################################
# This method will return the key of the value that is given in the
# dictionary. if the dictionary is dic={'A':[2],'B':[3]}, func(3)
# will return 'A'
####################################################################
def findKeyByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
            break
    return  listOfKeys

####################################################################
# This method will give the most vulnerable person, the first choice
# by push that choice into the final_object
####################################################################
def AssignThisPersonFirstChoice( final_object, scenario,  mostValnerablePerson ):
    final_object[ mostValnerablePerson ] = scenario[ mostValnerablePerson ][0]
    return final_object

####################################################################
# This method will go thorugh the scenario dictionary and delete
# every keys first value so 'A':[1,2,3] becomes 'A':[2,3]
####################################################################
def removeEveryonesFirstChoice(scenario):
    for i in scenario:
        scenario[i].pop(0)
    return scenario

####################################################################
# This method will return true if all the arrays in dictionary
# is empty, so that we know all people have been assigned a 
# shelter
####################################################################
def isEmptyDictionary( dic ):

    flag = True

    for i in dic.values():

        if ( len(i) != 0 ):

            flag = False

    return flag

####################################################################
# This method will delete the person given person from dictionary
# that is because he has been assigned a shelter already in previous
# line
####################################################################
def removeThisPersonFromScenario(scenario, person):
    scenario.pop(person)
    return scenario

####################################################################
# This method will sort all the shelter base on their risk
####################################################################
def sortAllArrayBasedOnRisk(scenario):
    for i in scenario:
        scenario[i].sort()
    return scenario

####################################################################
# This method calculate and return the overall sum
####################################################################
def sumOfAllElements(scenario):
    sum = 0
    for i in scenario:
        sum += scenario[i]
    return sum

####################################################################
# This method is returning the maximum risk
####################################################################
def maxRiskInObject(scenario):
    return max(scenario.values())

####################################################################
# This method is returning this persons chosen shelter index in 
# the initial scenario list. For example if we have
# A = {1, 7, 8} as initial list and the final list looks like
# A = 7 then the output of this function is 1 because 7 was the 
# 1 position in initial list
####################################################################
def ReturnPersonShelterIndexInScenario( scenario, person, shelterRisk ):
    return scenario[ person ].index(shelterRisk)

####################################################################
# This method is returning this persons chosen shelter index in 
# the initial scenario list. For example if we have
# A = {1, 7, 8} as initial list and the final list looks like
# A = 7 then the output of this function is 1 because 7 was the 
# 1 position in initial list
####################################################################
def AssignThisPersonMinChoice( final_object, scenario,  mostValnerablePerson ):

    final_object[ mostValnerablePerson ] = min(scenario[ mostValnerablePerson ])

    return final_object


####################################################################
# This method is returning this person risk index
####################################################################
def mostValnerablePersonMinRiskIndex(scenario,  mostValnerablePerson ):

    personMin = min(scenario[ mostValnerablePerson ])

    return ReturnPersonShelterIndexInScenario(scenario, mostValnerablePerson, personMin)


####################################################################
# This method will go thorugh the scenario dictionary and delete
# the given index from everyone
####################################################################
def removeThisIndexFromEveryones(scenario, index):
    for i in scenario:
        scenario[i].pop(index)
    return scenario


####################################################################
# This method will generate a random scenario length with
# random risks
####################################################################
def ReturnRandomScenario(shelterlen, peopleLen):


    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    scenarioOutput = {}
    array = []
    peopleName = list(string)
    

    for x in range(0, peopleLen):
        array.append(peopleName[x])
        # scenarioOutput[ peopleName[x] ] = []

        # for y in range(0, shelterlen):
        #     scenarioOutput[  peopleName[x] ].append( random.randint(0,200) )

    return scenarioOutput


####################################################################
# This method calculate and return the overall sum
####################################################################
def printResults(final_object,algorithmName):
    print(algorithmName+" Results")
    print(final_object)
    print("Overall Risk Sum")
    print(sumOfAllElements(final_object))
    print("Maximum Risk")
    print(maxRiskInObject(final_object))
    print("========================================")

####################################################################
# This method will go thorugh the final object (the result of algorithm)
# and return the minimum assigned weight and sum
####################################################################
def FinalObjectAnalysis(final_object,weights,people,shelters):
    # print(final_object)
    output = {}
    resultList = []
    for i in final_object:
        _thisWeight = weights[ people.index(i) ][ shelters.index(final_object[i]) ]
        resultList.append(_thisWeight)


    # print(resultList)
    _max = max(resultList)
    _sum = sum(resultList)
    output.update({'max':_max}) 
    output.update({'sum':_sum})

    return(output)

####################################################################
# This method will go thorugh the final object (the result of algorithm)
# and return the minimum assigned weight and sum
####################################################################
def FinalObjectAnalysisLOCALSEARCH(final_object,weights,people,shelters):
    output = {}
    resultList = []
    for i in final_object:
        _thisWeight = weights[ people.index(i) ][ shelters.index(final_object[i]) ]
        resultList.append(_thisWeight)
    # print(resultList)
    _max = max(resultList)
    _sum = sum(resultList)
    output.update({'max':_max}) 
    output.update({'sum':_sum})

    return(output)

def sd_calc(data):
    n = len(data)

    if n <= 1:
        return 0.0

    mean, sd = avg_calc(data), 0.0

    # calculate stan. dev.
    for el in data:
        sd += (float(el) - mean)**2
    sd = math.sqrt(sd / float(n-1))

    return sd

def avg_calc(ls):
    n, mean = len(ls), 0.0

    if n <= 1:
        return ls[0]

    # calculate average
    for el in ls:
        mean = mean + float(el)
    mean = mean / float(n)

    return mean

def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None