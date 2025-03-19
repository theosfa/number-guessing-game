LF = b'\x0A' # \n Перевод на следующую строку

from random import randint
import sys
import shutil

# screen_size = shutil.get_terminal_size()
# sys.stdout.buffer.write(LF*screen_size.lines)

class Ngg():
    def __init__(self) -> None:
        self.level = 0
        self.attempts = 0
        self.tries = []
        self.number = 0
        self.ml = { -1 : "less", 1 : "more", 0 : "exact"}
        self.limit = 100
        self.print = "Choose level of game : "
    
    def checkLevel(self, level : str) -> bool:
        possible = ["1", "2", "3", "4"]
        return True if level in possible else False
        
    def setLevel(self, new_level : str) -> None:
        self.level = new_level
        match new_level:
            case "1":
                self.attempts = 5
            case "2":
                self.attempts = 3
            case "3":
                self.attempts = 1
            case "4":
                self.attempts = 1_000_000_000_000_000
        self.setPrint("Number you want to try : ")
        self.createNumber()
    
    def createNumber(self) -> None:
        self.number = randint(1, 100)
    
    def addTry(self, guess_number : int, equals : int) -> None:
        self.tries.append((guess_number, self.ml[equals]))
        self.attempts-=1
    
    def setNumber(self, new_number : int) -> None:
        self.number = new_number
    
    def setPrint(self, new_print : str) -> None:
        self.print = new_print
    
    def getPrint(self) -> str:
        return self.print

    def getAttempts(self) -> int:
        return self.attempts
    
    def checkIfGuess(self, guess_number : int) -> int:
        n_return = 0
        
        if self.number < guess_number:
            n_return = -1
        elif self.number > guess_number:
            n_return = 1
        
        self.addTry(guess_number, n_return)
        return n_return

    def printTries(self) -> None:
        print("\tYour attempts :")
        for i, el in enumerate(self.tries):
            print(f"\t{i+1} : {el[0]} - {el[1]}")

    def printWelcome(self) -> None:
        print('''
\t****************************
\t&                          &
\t&      WELCOME TO NGG      &
\t&                          &
\t****************************
              ''')
        self.printRules()
    
    def printGame(self) -> None:
        print('''
\t****************************
\t&                          &
\t&     TRY TO GUESS !!!     &
\t&                          &
\t****************************
              ''')
        self.printTries()
        screen_size = shutil.get_terminal_size()
        sys.stdout.buffer.write(LF*(screen_size.lines-9-len(self.tries)))
        
    def printCongrats(self) -> None:
        print('''
\t****************************
\t&                          &
\t&       YOU WIN !!!        &
\t&                          &
\t****************************
              ''')
        self.printTries()
        screen_size = shutil.get_terminal_size()
        sys.stdout.buffer.write(LF*(screen_size.lines-9-len(self.tries)))
    
    def printLose(self) -> None:
        print('''
\t****************************
\t&                          &
\t&       YOU LOSE !!!       &
\t&                          &
\t****************************
              ''')
        self.printTries()
        screen_size = shutil.get_terminal_size()
        sys.stdout.buffer.write(LF*(screen_size.lines-9-len(self.tries)))
    
    def printRules(self) -> None:
        print('''
    Rules :
    \t1. Do not cheat!
    \t2. Have fun)
    \t3. To leave type \'exit\'
    What to do:
    \tChoose level of game:
    \t\t1 - Game easy(5 attempts)
    \t\t2 - Game medium(3 attempts)
    \t\t3 - Game hard(1 attempts)
    \t\t4 - Game god(infinite attempts)
    \tTry to guess
              ''')
        screen_size = shutil.get_terminal_size()
        sys.stdout.buffer.write(LF*(screen_size.lines-21))
        
         

def main(args : list[str]) -> None:
    print(shutil.get_terminal_size())
    ngg = Ngg()
    q = True
    while q:
        ngg.printWelcome()
        inp = input(ngg.getPrint())
        if ngg.checkLevel(inp):
            ngg.setLevel(inp)
            q = False
    q = True
    while q:
        ngg.printGame()
        inp = input(ngg.getPrint())
        if inp == "exit":
            q = False
        if ngg.checkIfGuess(int(inp)) == 0:
            ngg.printCongrats()
            q = False
        elif ngg.getAttempts() <= 0:
            ngg.printLose()
            q = False