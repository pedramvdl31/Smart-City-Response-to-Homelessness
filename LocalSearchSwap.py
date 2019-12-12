####################################################################
# LOCAL SEARCH ALGORITHM
####################################################################
import statistics
import funcs
import time
import AllData
# import scenarioData

weights = AllData.getWeight()
people = AllData.getPeople()
shelters = AllData.getShelter()

start_time = time.time()

def getLocalSearch(final_object):
    flag = True

    specialCounter = 0

    while ( flag ):

        flag = False

        m = 0
        valuneableIndex = None
        valuneableName = None
        vulnerableShelter = None

        for person in final_object:
            shelter = final_object[person]
            w = weights[people.index(person)][shelters.index(shelter)]
            if w>m:
                m=w
                valuneableName = person
                valuneableIndex = people.index(person)
                vulnerableShelter = shelter

        for key in range(len(people)):
            
            if valuneableIndex != key:
                
                SwapWeight = weights[ key ][ shelters.index(final_object[valuneableName]) ]
                _person = people[key]
                _personShelter = final_object[_person]
                _shelterIndex = shelters.index(_personShelter)
                _SwapWeight = weights[valuneableIndex][_shelterIndex]

                if SwapWeight<m and _SwapWeight<m:
                    specialCounter+=1
                    # print("******")
                    # print("COUNTER: "+str(specialCounter)+",\nMaximum assigned weight: "+str(m),"\nswapA: "+str(SwapWeight),"\nswapB: "+str(_SwapWeight) )
                    # print("******")
                    final_object[valuneableName] = _personShelter
                    final_object[ people[key] ] = vulnerableShelter
                    flag = True
                    break
                
    output = funcs.FinalObjectAnalysisLOCALSEARCH(final_object,weights,people,shelters)

    print(output)
    # print(final_object)
    # print("--- %s seconds ---" % (time.time() - start_time))