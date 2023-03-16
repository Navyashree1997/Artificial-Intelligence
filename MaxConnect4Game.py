import copy
import random
import sys

class maxConnect4Game:
    def __init__(self):
        self.gameBoard = [[0 for i in range(7)] for j in range(6)]
        self.onGoingTurn = 1
        self.player1Score = 0
        self.player2Score = 0
        self.boardPieces = 0
        self.gameFile = None
        self.utility = None
        random.seed()

    def checkPieceCount(self):
        self.boardPieces = sum(1 for row in self.gameBoard for piece in row if piece)

    def printGameBoard(self):
        print( '-----------------')
        for i in range(6):
            print ('',)
            for j in range(7):       
                print(self.gameBoard[i][j],end=' ')
                
    def printGameBoardToFile(self):
        for row in self.gameBoard:
            self.gameFile.write(''.join(str(col) for col in row) + '\r\n')
        self.gameFile.write('%s\r\n' % str(self.onGoingTurn))

    
    def playPiece(self, column):
        if not self.gameBoard[0][column]:
            for i in range(5, -1, -1):
                if not self.gameBoard[i][column]:
                    self.gameBoard[i][column] = self.onGoingTurn
                    self.boardPieces += 1
                    return 1

   
    def aiPlay(self, depth, machine):
        self.furtherMoves(depth - 1, machine)
        column = self.bestMoveAlgo(machine)
        result = self.playPiece(column)
        if not result:
            self.aiPlay(depth, machine)
        else:
            print('\n\nmove %d: Player %d, column %d\n' % (self.boardPieces, self.onGoingTurn, column+1))
        return
    def countScore(self):
        self.player1Score = 0
        self.player2Score = 0
        for row in self.gameBoard:
            # Check player 1
            if row[0:4] == [1]*4:
                self.player1Score += 1
            if row[1:5] == [1]*4:
                self.player1Score += 1
            if row[2:6] == [1]*4:
                self.player1Score += 1
            if row[3:7] == [1]*4:
                self.player1Score += 1
            # Check player 2
            if row[0:4] == [2]*4:
                self.player2Score += 1
            if row[1:5] == [2]*4:
                self.player2Score += 1
            if row[2:6] == [2]*4:
                self.player2Score += 1
            if row[3:7] == [2]*4:
                self.player2Score += 1

        # Check vertically
        for j in range(7):
            # Check player 1
            if (self.gameBoard[0][j] == 1 and self.gameBoard[1][j] == 1 and
                   self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][j] == 1 and self.gameBoard[2][j] == 1 and
                   self.gameBoard[3][j] == 1 and self.gameBoard[4][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1 and
                   self.gameBoard[4][j] == 1 and self.gameBoard[5][j] == 1):
                self.player1Score += 1
            # Check player 2
            if (self.gameBoard[0][j] == 2 and self.gameBoard[1][j] == 2 and
                   self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][j] == 2 and self.gameBoard[2][j] == 2 and
                   self.gameBoard[3][j] == 2 and self.gameBoard[4][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2 and
                   self.gameBoard[4][j] == 2 and self.gameBoard[5][j] == 2):
                self.player2Score += 1

        # Check diagonally

        # Check player 1
        if (self.gameBoard[2][0] == 1 and self.gameBoard[3][1] == 1 and
               self.gameBoard[4][2] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][0] == 1 and self.gameBoard[2][1] == 1 and
               self.gameBoard[3][2] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][1] == 1 and self.gameBoard[3][2] == 1 and
               self.gameBoard[4][3] == 1 and self.gameBoard[5][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][0] == 1 and self.gameBoard[1][1] == 1 and
               self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][1] == 1 and self.gameBoard[2][2] == 1 and
               self.gameBoard[3][3] == 1 and self.gameBoard[4][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1 and
               self.gameBoard[4][4] == 1 and self.gameBoard[5][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][1] == 1 and self.gameBoard[1][2] == 1 and
               self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][2] == 1 and self.gameBoard[2][3] == 1 and
               self.gameBoard[3][4] == 1 and self.gameBoard[4][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1 and
               self.gameBoard[4][5] == 1 and self.gameBoard[5][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][2] == 1 and self.gameBoard[1][3] == 1 and
               self.gameBoard[2][4] == 1 and self.gameBoard[3][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][4] == 1 and
               self.gameBoard[3][5] == 1 and self.gameBoard[4][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][4] == 1 and
               self.gameBoard[2][5] == 1 and self.gameBoard[3][6] == 1):
            self.player1Score += 1

        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][2] == 1 and
               self.gameBoard[2][1] == 1 and self.gameBoard[3][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][4] == 1 and self.gameBoard[1][3] == 1 and
               self.gameBoard[2][2] == 1 and self.gameBoard[3][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][2] == 1 and
               self.gameBoard[3][1] == 1 and self.gameBoard[4][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][5] == 1 and self.gameBoard[1][4] == 1 and
               self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][4] == 1 and self.gameBoard[2][3] == 1 and
               self.gameBoard[3][2] == 1 and self.gameBoard[4][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1 and
               self.gameBoard[4][1] == 1 and self.gameBoard[5][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][6] == 1 and self.gameBoard[1][5] == 1 and
               self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][5] == 1 and self.gameBoard[2][4] == 1 and
               self.gameBoard[3][3] == 1 and self.gameBoard[4][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1 and
               self.gameBoard[4][2] == 1 and self.gameBoard[5][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][6] == 1 and self.gameBoard[2][5] == 1 and
               self.gameBoard[3][4] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][5] == 1 and self.gameBoard[3][4] == 1 and
               self.gameBoard[4][3] == 1 and self.gameBoard[5][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][6] == 1 and self.gameBoard[3][5] == 1 and
               self.gameBoard[4][4] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1

        # Check player 2
        if (self.gameBoard[2][0] == 2 and self.gameBoard[3][1] == 2 and
               self.gameBoard[4][2] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][0] == 2 and self.gameBoard[2][1] == 2 and
               self.gameBoard[3][2] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][1] == 2 and self.gameBoard[3][2] == 2 and
               self.gameBoard[4][3] == 2 and self.gameBoard[5][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][0] == 2 and self.gameBoard[1][1] == 2 and
               self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][1] == 2 and self.gameBoard[2][2] == 2 and
               self.gameBoard[3][3] == 2 and self.gameBoard[4][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2 and
               self.gameBoard[4][4] == 2 and self.gameBoard[5][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][1] == 2 and self.gameBoard[1][2] == 2 and
               self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][2] == 2 and self.gameBoard[2][3] == 2 and
               self.gameBoard[3][4] == 2 and self.gameBoard[4][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2 and
               self.gameBoard[4][5] == 2 and self.gameBoard[5][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][2] == 2 and self.gameBoard[1][3] == 2 and
               self.gameBoard[2][4] == 2 and self.gameBoard[3][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][4] == 2 and
               self.gameBoard[3][5] == 2 and self.gameBoard[4][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][4] == 2 and
               self.gameBoard[2][5] == 2 and self.gameBoard[3][6] == 2):
            self.player2Score += 1

        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][2] == 2 and
               self.gameBoard[2][1] == 2 and self.gameBoard[3][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][4] == 2 and self.gameBoard[1][3] == 2 and
               self.gameBoard[2][2] == 2 and self.gameBoard[3][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][2] == 2 and
               self.gameBoard[3][1] == 2 and self.gameBoard[4][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][5] == 2 and self.gameBoard[1][4] == 2 and
               self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][4] == 2 and self.gameBoard[2][3] == 2 and
               self.gameBoard[3][2] == 2 and self.gameBoard[4][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2 and
               self.gameBoard[4][1] == 2 and self.gameBoard[5][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][6] == 2 and self.gameBoard[1][5] == 2 and
               self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][5] == 2 and self.gameBoard[2][4] == 2 and
               self.gameBoard[3][3] == 2 and self.gameBoard[4][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2 and
               self.gameBoard[4][2] == 2 and self.gameBoard[5][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][6] == 2 and self.gameBoard[2][5] == 2 and
               self.gameBoard[3][4] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][5] == 2 and self.gameBoard[3][4] == 2 and
               self.gameBoard[4][3] == 2 and self.gameBoard[5][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][6] == 2 and self.gameBoard[3][5] == 2 and
               self.gameBoard[4][4] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1

    def withinRange(self, depth, machine):
            self.children = []
            for gameColumn in range(0, 7):
                if not self.gameBoard[0][gameColumn]:
                    child = maxConnect4Game()
                    child.gameBoard = copy.deepcopy(self.gameBoard)
                    if self.onGoingTurn == 1:
                        child.onGoingTurn = 2
                    elif self.onGoingTurn == 2:
                        child.onGoingTurn = 1
                    child.evaluation = 0
                    child.boardPieces = self.boardPieces + 1

                    if machine == self.onGoingTurn:
                        maxConnect4Game.evalComputer(self,machine,child)
                        break
                    else:
                        maxConnect4Game.propGameboard(self,child,gameColumn)

            for child in self.children:
                child.furtherMoves(depth - 1, machine)   

    def furtherMoves(self, depth, machine):
        if depth >= 0 and self.boardPieces < 42:
            maxConnect4Game.withinRange(self, depth, machine)   
        else: 
            self.countScore()
            if machine == 1:
                self.utility = self.player1Score - self.player2Score + self.evaluation
            else:
                self.utility = self.player2Score - self.player1Score + self.evaluation


   
    def evalComputer(self,machine,child):
        self.evaluationAlgo(machine)
        child.column = self.bestMove["column"]
        child.gameBoard[self.bestMove["row"]][self.bestMove["column"]] = self.onGoingTurn
        child.evaluation = self.bestMove["utility"]
        self.children.append(child)

    def propGameboard(self,child,gameColumn):
         for i in range(5, -1, -1):
            if not child.gameBoard[i][gameColumn]:
                child.column = gameColumn
                child.gameBoard[i][gameColumn] = self.onGoingTurn
                self.children.append(child)
                break
                            
    def minMaxAlgo(self, machine):
        if self.utility is not None:
            return self.utility

        elif self.onGoingTurn!=machine:
            value = 999
            for child in self.children:
                value = min(value, child.minMaxAlgo(machine))
        elif self.onGoingTurn == machine:
            value = -999
            for child in self.children:
                value = max(value, child.minMaxAlgo(machine))
        
        self.utility = value
        return self.utility

    def alphaBetaAlgo(self, machine, alpha, beta):
        if self.utility is not None:
            return self.utility

        elif self.onGoingTurn != machine:
            value = 999
            for child in self.children:
                value = min(value, child.alphaBetaAlgo(machine, alpha, beta))
                if beta <= alpha:
                    self.utility = value
                    return self.utility
                else:
                    beta = min(value, beta)
        elif self.onGoingTurn == machine:
            value = -999
            for child in self.children:
                value = max(value, child.alphaBetaAlgo(machine, alpha, beta))
                if alpha >= beta:
                    self.utility = value
                    return self.utility
                else:
                    alpha = max(alpha, value)
        self.utility = value
        return self.utility

    def bestMoveAlgo(self, machine):
        alpha = -999
        beta  = 999
        value = self.alphaBetaAlgo(machine, alpha, beta)
        for child in self.children:
            if child.utility == value:
                return child.column

    def evaluationAlgo(self, machine):
        if machine == 1:
            opposition = 2
        else:
            opposition = 1
        playableMoves = []
        for column in range(0, 7):
            if not self.gameBoard[0][column]:
                for row in range(5, -1, -1):
                    if not self.gameBoard[row][column]:
                        playableMoves.append({
                            "row": row,
                            "column": column
                        })
                        break
        
        if len(playableMoves) > 0:
            maxConnect4Game.playableMove(self,playableMoves,opposition,machine)
            if self.win >= self.loose and self.win != -1:
                self.bestMove = {
                    "row" : self.winBestMove["row"],
                    "column" : self.winBestMove["column"],
                    "utility" : self.win * 4
                }
            elif self.win < self.loose:
                self.bestMove = {
                    "row" : self.looseBestMove["row"],
                    "column" : self.looseBestMove["column"],
                    "utility" : self.loose * 4
                }
            elif self.probMax > 0:
                self.bestMove = {
                    "row" : self.probMove["row"],
                    "column" : self.probMove["column"],
                    "utility" : self.probMax
                }
            else:
                self.bestMove = {
                    "row" : self.randomMove["row"],
                    "column" : self.randomMove["column"],
                    "utility" : 0
                }
        else:
            self.bestMove = None

    def playableMove(self,playableMoves,opposition,machine):
            self.loose = -1
            self.win = -1
            self.probMax = -1
            self.looseBestMove = None
            self.winBestMove = None
            self.probMove = None
            self.randomMove = playableMoves[random.randrange(0, len(playableMoves))] # NEed to correct this
            for move in playableMoves:
                looseCount = 0
                winCount = 0
                probCounter = 0
                if move["column"] >=0:
                    if move["column"] + 3 <= 6:
                        column_max = move["column"] + 3
                    else:
                        column_max = 6
                if move["column"] >=0:
                    if move["column"] - 3 >= 0:
                        column_min = move["column"] - 3
                    else:
                        column_min = 0                
                current_row = self.gameBoard[move["row"]][:]
                current_row[move["column"]] = opposition
                for i in range(column_min, column_max - 2, 1):
                    if current_row[i:i+4] == [opposition]*4:
                        looseCount += 1
                
                current_row[move["column"]] = machine
                for i in range(column_min, column_max - 2, 1):
                    if current_row[i:i+4] == [machine]*4:
                        winCount += 1
                    try:
                        if current_row[i:i+4].index(opposition) >= 0:
                            pass
                    except:
                        probCounter += 1                                
                maxConnect4Game.verticalCheck(self,move,opposition,machine, looseCount,winCount,probCounter )                                        
                maxConnect4Game.diagnoalRight(self,move,opposition,machine, looseCount,winCount,probCounter)                    
                maxConnect4Game.diagonalLeft(self,move,opposition,machine, looseCount,winCount,probCounter)                                        
                if looseCount != 0 and looseCount > self.loose:
                    self.loose = looseCount
                    self.looseBestMove = move

                if winCount != 0 and winCount > self.win:
                    self.win = winCount
                    self.winBestMove = move

                if probCounter != 0 and probCounter > self.probMax:
                    self.probMax = probCounter
                    self.probMove = move


    
    def verticalCheck(self,move,opposition, machine, looseCount,winCount,probCounter ):
                if move["row"] + 3 <= 5:                    
                    if self.gameBoard[move["row"] + 3][move["column"]] == machine and self.gameBoard[move["row"] + 2][move["column"]] == machine and self.gameBoard[move["row"] + 1][move["column"]] == machine:
                        winCount += 1
                    
                    if self.gameBoard[move["row"] + 3][move["column"]] == opposition and self.gameBoard[move["row"] + 2][move["column"]] == opposition and self.gameBoard[move["row"] + 1][move["column"]] == opposition:
                        looseCount += 1
                        
                    probArray = []
                    probArray.append(self.gameBoard[move["row"] + 3][move["column"]])
                    probArray.append(self.gameBoard[move["row"] + 2][move["column"]])
                    probArray.append(self.gameBoard[move["row"] + 1][move["column"]])
                    try:
                        if probArray.index(opposition) >= 0:
                            pass
                    except:
                        probCounter += 1
                
    def diagnoalRight(self,move,opposition,machine, looseCount,winCount,probCounter):
                rowEnd = move["row"]
                columnEnd = move["column"]
                i = 3
                while i != 0 and rowEnd != 5 and columnEnd != 6:
                    rowEnd = rowEnd + 1
                    columnEnd = columnEnd + 1
                    i = i - 1

                rowStart = move["row"]
                columnStart = move["column"]
                i = -3
                while i != 0 and rowStart != 0 and columnStart != 0:
                    rowStart = rowStart - 1
                    columnStart = columnStart - 1
                    i = i - 1
            
                rowStartSave = rowStart
                rowEndSave = rowEnd
                columnStartSave = columnStart
                columnEndSave = columnEnd
                maxConnect4Game.diagonalRightComputerPlay(self,move,machine,rowStart,rowEnd,columnStart,probCounter,opposition,winCount)            

                rowStart = rowStartSave
                rowEnd = rowEndSave
                columnStart = columnStartSave
                columnEnd = columnEndSave
                maxConnect4Game.diagonalRightOppositionPlay(self,move,machine,rowStart,rowEnd,columnStart,probCounter, opposition,looseCount )                

    def diagonalLeft(self,move,opposition,machine, looseCount,winCount,probCounter):
                rowEnd = move["row"]
                columnEnd = move["column"]
                i = 3
                while i != 0 and rowEnd != 5 and columnEnd != 0:
                    rowEnd = rowEnd + 1
                    columnEnd = columnEnd - 1
                    i = i - 1

                rowStart = move["row"]
                columnStart = move["column"]
                i = -3
                while i != 0 and rowStart != 0 and columnStart != 6:
                    rowStart = rowStart - 1
                    columnStart = columnStart + 1
                    i = i - 1

                rowStartSave = rowStart
                rowEndSave = rowEnd
                columnStartSave = columnStart
                columnEndSave = columnEnd                
                maxConnect4Game.diagonalLeftComputerPlay(self,move,machine,rowStart,rowEnd,columnStart,probCounter,opposition,winCount)                
                
                rowStart = rowStartSave
                rowEnd = rowEndSave
                columnStart = columnStartSave
                columnEnd = columnEndSave                
                maxConnect4Game.diagonalLeftOppositionPlay(self, move, machine, rowStart, rowEnd, columnStart, probCounter, opposition,looseCount)
    
    def diagonalRightComputerPlay(self,move,machine,rowStart,rowEnd,columnStart,probCounter,opposition,winCount):
                currentBoardMap = copy.deepcopy(self.gameBoard)
                currentBoardMap[move["row"]][move["column"]] = machine
                while rowStart <= rowEnd - 3:
                    if currentBoardMap[rowStart][columnStart] == machine and currentBoardMap[rowStart+1][columnStart+1] == machine and currentBoardMap[rowStart+2][columnStart+2] == machine and currentBoardMap[rowStart+3][columnStart+3] == machine:
                        winCount += 1 
                    probArray = []
                    probArray.append(currentBoardMap[rowStart+3][columnStart+3])
                    probArray.append(currentBoardMap[rowStart+2][columnStart+2])
                    probArray.append(currentBoardMap[rowStart+1][columnStart+1])
                    probArray.append(currentBoardMap[rowStart][columnStart])
                    rowStart = rowStart + 1
                    columnStart = columnStart + 1
                    try:
                        if probArray.index(opposition) >= 0:
                            pass
                    except:
                        probCounter += 1
    
    def diagonalRightOppositionPlay(self,move,machine,rowStart,rowEnd,columnStart,probCounter,opposition,looseCount):
                currentBoardMap = copy.deepcopy(self.gameBoard)
                currentBoardMap[move["row"]][move["column"]] = opposition
                while rowStart <= rowEnd - 3:
                    if currentBoardMap[rowStart][columnStart] == opposition and currentBoardMap[rowStart+1][columnStart+1] == opposition and currentBoardMap[rowStart+2][columnStart+2] == opposition and currentBoardMap[rowStart+3][columnStart+3] == opposition:
                        looseCount += 1 

                    rowStart = rowStart + 1
                    columnStart = columnStart + 1

    def diagonalLeftComputerPlay(self,move,machine,rowStart,rowEnd,columnStart,probCounter,opposition,winCount):
                currentBoardMap = copy.deepcopy(self.gameBoard)
                currentBoardMap[move["row"]][move["column"]] = machine
                while rowStart <= rowEnd - 3:
                    if currentBoardMap[rowStart][columnStart] == machine and currentBoardMap[rowStart+1][columnStart-1] == machine and currentBoardMap[rowStart+2][columnStart-2] == machine and currentBoardMap[rowStart+3][columnStart-3] == machine:
                        winCount += 1 

                    probArray = []
                    probArray.append(currentBoardMap[rowStart+3][columnStart-3])
                    probArray.append(currentBoardMap[rowStart+2][columnStart-2])
                    probArray.append(currentBoardMap[rowStart+1][columnStart-1])
                    probArray.append(currentBoardMap[rowStart][columnStart])

                    rowStart = rowStart + 1
                    columnStart = columnStart - 1

                    try:
                        if probArray.index(opposition) >= 0:
                            pass
                    except:
                        probCounter += 1
    
    def diagonalLeftOppositionPlay(self,move,machine,rowStart,rowEnd,columnStart,probCounter,opposition,looseCount):
                currentBoardMap = copy.deepcopy(self.gameBoard)
                currentBoardMap[move["row"]][move["column"]] = opposition
                while rowStart <= rowEnd - 3:
                    if currentBoardMap[rowStart][columnStart] == opposition and currentBoardMap[rowStart+1][columnStart-1] == opposition and currentBoardMap[rowStart+2][columnStart-2] == opposition and currentBoardMap[rowStart+3][columnStart-3] == opposition:
                        looseCount += 1 
                    rowStart = rowStart + 1
                    columnStart = columnStart - 1
    