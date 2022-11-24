#Holds all nodes with a unique index
nodeList = []
#Keeps track of where it is in the tree
currentNode = 0
gameOver = False

#These nodes make up a tree data structure to keep the data organized
class Node:
  def __init__(self, data):
    self.data = data
    self.no = None
    self.yes = None
    self.number = len(nodeList)

#Creates a new node and adds it to the end of nodeList
def addNode(animal):
  newNode = Node(animal)
  nodeList.append(newNode)

#If an animal was guessed, and it was incorrect, the player is prompted to create a new question to be added.
def getNewQuestion():
  global nodeList
  global gameOver
  validResponse = False
  print("\nI'm sorry, I do not know what your animal is.")
  animal = input("What was your animal?\n")
  question = input("\nPlease type a yes/no question where the answer for your animal (%s) is different than the answer for a(n) %s\n" % (animal, nodeList[currentNode].data))
  while validResponse == False:
    answer = input("\nNow please answer the question  you just submitted (%s) for your animal (%s).\n" % (question, animal))
    #If the answer to the created question for the new animal is yes, add it to the yes branch of the tree
    if answer[0].lower() == "y":
      validResponse = True
      addNode(nodeList[currentNode].data)
      noAnswer = nodeList[-1]
      addNode(animal)
      yesAnswer = nodeList[-1]
      nodeList[currentNode].no = noAnswer
      nodeList[currentNode].yes = yesAnswer
      nodeList[currentNode].data = question
      gameOver = True
    #If the answer to the created question for the new animal is no, add it to the no branch of the tree
    elif answer[0].lower() =="n":
      validResponse = True
      addNode(nodeList[currentNode].data)
      yesAnswer = nodeList[-1]
      addNode(animal)
      noAnswer = nodeList[-1]
      nodeList[currentNode].no = noAnswer
      nodeList[currentNode].yes = yesAnswer
      nodeList[currentNode].data = question
      gameOver = True
    else:
      print("Please enter either y(es) or n(o)")

#If the current node is a question node, ask the player the question
def askQuestion():
  global currentNode
  validResponse = False
  question = nodeList[currentNode].data
  while validResponse == False:
    answer = input("\n" + question + "\n")
    if answer == "":
      print("Please enter either y(es) or n(o)")
      continue
    #If player answer is yes, follow the "yes" path of the tree
    if answer[0].lower() == "y":
      print(nodeList[currentNode].yes.number)
      currentNode = nodeList[currentNode].yes.number
      validResponse = True
    #If player answer is no, follow the "no" path of the tree
    elif answer[0].lower() == "n":
      print(nodeList[currentNode].no.number)
      currentNode = nodeList[currentNode].no.number
      validResponse = True
    else:
      print("Please enter either y(es) or n(o)")

#If the current node is an animal node, ask the player if the guess is correct
def guessAnimal():
  global gameOver
  validResponse = False
  animalToGuess = nodeList[currentNode].data
  while validResponse == False:
    answer = input("\nIs your animal a(n) %s?\n" % (animalToGuess))
    if answer[0].lower() == "y":
      validResponse = True
      gameOver = True
      print("I guessed correct!\n")
    #If the guess was incorrect, get a new question
    elif answer[0].lower() == "n":
      validResponse = True
      getNewQuestion()
    else:
      print("Please enter either y(es) or n(o)")

#Gets the root of the tree created
def initializeGame():
  print("I don't know anything yet...")
  startingAnimal = input("Please input an animal to start:\n")
  addNode(startingAnimal)
  
def play():
  global gameOver
  global currentNode
  initializeGame()
  while gameOver == False:
    validResponse = False
    print("\n\n\nPlease think of a new animal.")
    #If both node paths = none, it must be an animal node
    if nodeList[currentNode].no == None and nodeList[currentNode].yes == None:
      guessAnimal()
    #Otherwise it is a question node
    else:
      askQuestion()
    if gameOver == True:
        while validResponse == False:
          replay = input("\nDo you want to continue?\n")
          if replay[0].lower() == "y":
            gameOver = False
            currentNode = 0
            validResponse = True
          elif replay[0].lower() == "n":
            validResponse = True
          else:
            print("Please enter either y(es) or n(o)")

play()