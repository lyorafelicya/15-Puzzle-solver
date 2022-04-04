from puzzleSolver import *

# Main Program
def Main():
    cont = "Y"
    while(cont == "Y" or cont == "y"):
        print("=================================================")
        print("                15 PUZZLE SOLVER                 ")
        print("=================================================")
        print(" Welcome to 15-Puzzle Solver!")
        print(" Which input method would you like to use?")
        print(" 1. Text File")
        print(" 2. Random by program")
        choice = int(input(" >> "))

        # assume choice input and filename is always valid
        if(choice == 1):
            filename = input(" Enter name of the file (with .txt) : ")
            puzzle = np.loadtxt("../test/"+ filename, dtype=int)
        else:
            default = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
            random.shuffle(default)
            puzzle = np.array(default).reshape(4,4)  

        print("==============  INITIAL STATE   =================")
        printMatrix(puzzle)
        print("=================================================")
        printLess(puzzle)
        print("=================================================")
        if(isSolveable(puzzle)):
            print("This puzzle is solveable. Solving puzzle...")

            print()
            print("---------------")
            print(" Your Puzzle ")
            print("---------------")
            printMatrix(puzzle)
            print("---------------")
            
            start = time.time()
            node = solve(puzzle)
            end = time.time()
            totalTime = end - start

            print()
            print("Puzzle solved successfully!")
            print("Time taken               : " + str(totalTime) + " seconds")    
            print("Number of nodes expanded : " + str(node))
            print()
        else:
            print("This puzzle is not solveable!")
            print()
        cont = input("Do you want to try another puzzle? (Y/N) : ")
    print("Okay bye~ Thankyou!\n")
    
if __name__ == "__main__":
    Main()