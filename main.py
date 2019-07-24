names = ["", "", "", "", 0, 0, 0, 0]
jeff = [0, 0, 0, 0]
alist = ["", "", "", ""]
def red():
  z = 0
  x = 0
  while (x < 5):
    if (x > 2): 
      z = input("Enter 5 to end input cycle") 
    if (int(z) < 4):
      names[x] = input("Input Candidate Name")
    x = x +1 
def vote hicall(totalvotes):
  while (totalvotes < 5):
    x = 0
    while (x < 4):
      print(x + 1, ".", names[x])
      x = x + 1
    temp = input("Cast Your Vote with the relevant numeral code (1 - 4)")
    try:
      temp = int(temp) - 1
      names[temp + 4] = names[temp + 4] + 1
      totalvotes = totalvotes + 1
      print("You Voted for ", names[temp])
    except ValueError:
      print("Incorrect data type input, try again")
    print("TotalVotes = ", totalvotes)
  den = 4
  while (den < 8):
    alist[den - 4] = names[den]
    jeff[den - 4] = names[den - 4]
    den = den + 1 
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                temp2 = jeff[i]
                jeff[i] = jeff[i + 1]
                jeff[i + 1] = temp2
def xd():
  x = 3
  y = 1
  while (x > -1):
    print(y , ".", jeff[x])
    x = x -1
    y = y + 1
  print("NEW CLASS CAPTAIN ", jeff[0])
red()
votecall(0)
bubbleSort(alist)
xd()
