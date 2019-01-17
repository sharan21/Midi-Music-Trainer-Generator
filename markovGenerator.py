# initializes T matrix and T name, and generates a markov chain of "totalSteps" notes according to T matrix



import numpy as np
import random as rm

numberOfStates = 12

noteStates = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
# 12 states
octaveStates = [1,2,3,4,5,6,7,8]
timeStates = [1,2,3,4]

transitionMatrix = []
# 144 elements

transitionName = []
# 144 elements


def getTransitionName(): # makes the T matrix from all possible states

    printBlanks()

    print("making t name matrix...")

    for i in range(0,numberOfStates,1):
        temporaryBuffer = []
        for j in range(0,numberOfStates,1):
            temporaryBuffer.append(str(noteStates[i]+noteStates[j]))

        transitionName.append(temporaryBuffer)
    print("done making the matrix, resultant:")
    print transitionName



def getTransitionMatrix(): # makes the T matrix from all possible states

    printBlanks()

    print("making the t prob matrix...")
    for i in range(0,numberOfStates,1):
        temporaryBuffer = []
        for j in range(0,numberOfStates,1):
            temporaryBuffer.append(float(0.083333333))

        transitionMatrix.append(temporaryBuffer)

    print("done making the matrix, resultant:")

    print transitionMatrix




def validateSum():
    printBlanks()
    print("validating the sum...")
    sum = 0

    for i in range(0, numberOfStates, 1):
        for j in range(0, numberOfStates, 1):
            sum += transitionMatrix[i][j]

    if(sum < 12):
        print("correct sum...")
    else:
        print("wrong sum...")

    print ("sum is", sum)


def generateMarkovChain(totalSteps):
    printBlanks()
    print("generating markov chain according to t matrix...")
    initialState = noteStates[0]
    print("Start state: " + initialState)

    stateList = [initialState]
    currentStep = 0
    currentProbabilty = 1

    while currentStep != totalSteps:

        for i in range(0, numberOfStates, 1):

            if initialState == noteStates[i]:
                change = np.random.choice(transitionName[i],replace=True,p=transitionMatrix[i])

                for j in range(0, numberOfStates, 1):
                    if change == transitionName[i][j]:
                        currentProbabilty = currentProbabilty * transitionMatrix[i][j]
                        stateList.append(noteStates[j])
                        initialState = noteStates[j]
                        break

                break

        currentStep += 1

    print("State list: " + str(stateList))
    print("End state after " + str(totalSteps) + " steps: " + initialState)
    print("Probability of the possible sequence of states: " + str(currentProbabilty))


def printBlanks():

    print ("")
    print ("")
    print ("")

# MAIN

getTransitionMatrix()
getTransitionName()

validateSum()

generateMarkovChain(3)
