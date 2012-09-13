"""
Michael Palmer
Fall 2012
CSS 605
HW #1

Python Version   : 2.7.2
Editor           : IDLE 2.7.2
Operating System : Windows 7

For this assignment I have implemented a 3d TicTacToe game in Python. The board is 3 x 3 x 3.
I used the assignment to play with a number of features in Python including nested list comprehensions,
string formatting, dynamically callable functions and unit tests.

The example game included with the main function is:

  print "\nThree D Tic-Tac-Toe Demo:\n"
  mygame = threeDTicTacToe()
  mygame.move(XPLAYER,1,0,2)
  print mygame.prettyStr()
  mygame.move(OPLAYER,0,1,1)
  print mygame.prettyStr()
  mygame.move(XPLAYER,1,1,2)
  print mygame.prettyStr()
  mygame.move(OPLAYER,0,2,2)
  print mygame.prettyStr()
  mygame.move(XPLAYER,1,2,2)
  print mygame.prettyStr()
  
It should produce the following output:

Three D Tic-Tac-Toe Demo:


Game Board:
	- - -		- - X		- - -
	- - -		- - -		- - -
	- - -		- - -		- - -


Game Board:
	- - -		- - X		- - -
	- O -		- - -		- - -
	- - -		- - -		- - -


Game Board:
	- - -		- - X		- - -
	- O -		- - X		- - -
	- - -		- - -		- - -


Game Board:
	- - -		- - X		- - -
	- O -		- - X		- - -
	- - O		- - -		- - -


 Game Over. Winner: X


Game Board:
	- - -		- - X		- - -
	- O -		- - X		- - -
	- - O		- - X		- - -

  
"""

import unittest

EMPTY   = '-'
XPLAYER = 'X'
OPLAYER = 'O'
PLAYERS = [XPLAYER,OPLAYER]
VALIDVALUES = [EMPTY,XPLAYER,OPLAYER]

class threeDTicTacToe(object):
    DIMENSIONS = 3
    ROWS       = 3
    COLUMNS    = 3
    def __init__(self):
        self.board = self.initboard()
        self.boardlocked = False
    def prettyStr(self):
        joinedrows = [[' '.join(self.board[j][i]) for i in range(0,self.ROWS)] for j in range(self.DIMENSIONS)]
        flattenedrows = [ joinedrows[y][x] for y in range(self.ROWS) for x in range(self.DIMENSIONS)]
        outputrows =[]
        outputrows.append('\nGame Board:\n')
        for x in range(self.DIMENSIONS):
            outputrows.append('\t{}\t\t{}\t\t{}\n'.format(flattenedrows[x],flattenedrows[x+3],flattenedrows[x+6]))
        return  ''.join(outputrows)
    def move(self,player,dimension,row,column):
        assert(player in PLAYERS)
        assert(dimension >=0 and dimension <= self.DIMENSIONS)
        assert(row>=0 and row <= self.ROWS)
        assert(column>=0 and column<= self.COLUMNS)
   
        if (self.board[dimension][row][column]==EMPTY and self.boardlocked ==False):
                 self.board[dimension][row][column]=player
        gameover = self.hasWinner()
        if (gameover[0] == True):
            print "\n Game Over. Winner: "+gameover[1]+'\n'
            self.boardlocked = True
    def hasWinner(self):
        checks = [ '_checkRowWin_',
                   '_checkColWin_',
                   '_checkVerticalWin_',
                   '_checkLayerDiagonalWin_',
                   '_checkDimensionDiagonalWin_']
        for x in checks:
            rtn = self.__getattribute__(x)()
            if rtn[0]==True: return rtn
        return False,EMPTY
                   
    def _checkRowWin_(self):
        for x in range(self.DIMENSIONS):
            for y in range(self.ROWS):
                rtn = self._checker_(self.board[x][y],self.COLUMNS)
                if rtn[0] ==True: return rtn
        return False,EMPTY
    def _checkColWin_(self):
        for x in range(self.DIMENSIONS):
            coldata = []
            for y in range(self.COLUMNS):
                for z in range(self.ROWS):
                    coldata.append(self.board[x][z][y])
            rtn = self._checker_(coldata,self.ROWS)
            if rtn[0] == True: return rtn
        return False,EMPTY
    def _checkVerticalWin_(self):
        for row in range(self.ROWS):
          for col in range(self.COLUMNS):
            dimdata=[]
            for dimension in range(self.DIMENSIONS):
                dimdata.append(self.board[dimension][row][col])
            rtn = self._checker_(dimdata,self.DIMENSIONS)
            if rtn[0] == True: return rtn
        return False,EMPTY
    def _checker_(self,itemlist,wincount):
        for player in PLAYERS:
            if (itemlist.count(player)==wincount):
                return True,player
        return False,EMPTY
    def _checkLayerDiagonalWin_(self):
        otherdiagonal = range(self.ROWS)
        otherdiagonal.reverse()
        itemstocheck = []
        for dimension in range(self.DIMENSIONS):
            upperdiag = []
            lowerdiag = []
            for row in range(self.ROWS):
                upperdiag.append(self.board[dimension][row][row])
                lowerdiag.append(self.board[dimension][row][otherdiagonal[row]])
            itemstocheck.extend([upperdiag])
            itemstocheck.extend([lowerdiag])
        for x in itemstocheck:
            rtn = self._checker_(x,self.ROWS)
            if rtn[0]== True: return rtn
        return False,EMPTY
                   
    def _checkDimensionDiagonalWin_(self):
         itemstocheck = []
         otherdimension = range(self.DIMENSIONS)
         otherdimension.reverse()
         #check-left-to-right
         for row in range(self.ROWS):
             upperdiag = []
             lowerdiag = []
             for col in range(self.COLUMNS):

                 lowerdiag.append(self.board[col][row][col])
                 upperdiag.append(self.board[otherdimension[col]][row][col])
             itemstocheck.extend([upperdiag])
             itemstocheck.extend([lowerdiag])

         #check-top-to-bottom
         for col in range(self.COLUMNS):
             upperdiag = []
             lowerdiag = []
             for row in range(self.ROWS):
                 lowerdiag.append(self.board[row][row][col])
                 upperdiag.append(self.board[otherdimension[row]][row][col])
             itemstocheck.extend([upperdiag])
             itemstocheck.extend([lowerdiag])

         #across upperleft to lower right
         upperdiag = []
         lowerdiag = []             
         for col in range(self.COLUMNS):
             lowerdiag.append(self.board[col][col][col])
             upperdiag.append(self.board[otherdimension[col]][col][col])
         itemstocheck.extend([upperdiag])
         itemstocheck.extend([lowerdiag])

         #across upper right to lower left
         upperdiag = []
         lowerdiag = []
         for col in range(self.COLUMNS):
             lowerdiag.append(self.board[otherdimension[col]][col][otherdimension[col]])
             upperdiag.append(self.board[col][col][otherdimension[col]])
         itemstocheck.extend([upperdiag])
         itemstocheck.extend([lowerdiag])           
                                  
         for x in itemstocheck:
            rtn = self._checker_(x,self.ROWS)
            if rtn[0]== True: return rtn
         return False,EMPTY       
    def initboard(self):
        # Playing with list comprehensions - a very concise declaration
        blankboard = [[[EMPTY for i in range(self.COLUMNS)] for j in range(self.ROWS)] for k in range(self.DIMENSIONS)]
        return blankboard

class testgame(unittest.TestCase):
     def getsuite(self):
         suite = unittest.TestSuite()
         suite.addTest(testgame('test_init'))
         suite.addTest(testgame('test_move'))
         suite.addTest(testgame('test_noRowWin'))
         suite.addTest(testgame('test_rowXWin'))
         suite.addTest(testgame('test_rowOWin'))
         suite.addTest(testgame('test_noColWin'))
         suite.addTest(testgame('test_colXWin'))
         suite.addTest(testgame('test_colOWin'))
         suite.addTest(testgame('test_noVertWin'))
         suite.addTest(testgame('test_vertXWin'))
         suite.addTest(testgame('test_vertOWin'))
         suite.addTest(testgame('test_noLayerDiagonalWin'))
         suite.addTest(testgame('test_xLayerDiagonalWin'))
         suite.addTest(testgame('test_oLayerDiagonalWin'))
         suite.addTest(testgame('test_noDimDiagonalWin'))
         suite.addTest(testgame('test_leftRightDimXDiagonalWin'))
         suite.addTest(testgame('test_leftRightDimODiagonalWin'))
         suite.addTest(testgame('test_topToBottomDimODiagonalWin'))
         suite.addTest(testgame('test_topToBottomDimXDiagonalWin'))
         suite.addTest(testgame('test_upperleftDimXDiagonalWin'))                    
         suite.addTest(testgame('test_lowerleftDimODiagonalWin'))
         suite.addTest(testgame('test_upperrightDimXDiagonalWin'))                    
         suite.addTest(testgame('test_lowerrightDimODiagonalWin'))
         suite.addTest(testgame('test_winner'))

         
         return suite
        
     def runTest(self):
         runner = unittest.TextTestRunner(verbosity=2)
         suite = self.getsuite()
         result = runner.run(suite)
    
     def setUp(self):
         self.game = threeDTicTacToe()

     def test_winner(self):
         self.game.move(OPLAYER,0,2,0)
         self.game.move(OPLAYER,1,1,1)
         self.game.move(OPLAYER,2,0,2)                                 
         print self.game.prettyStr()        
         self.assertEqual(self.game.hasWinner(),(True,OPLAYER))

     def test_lowerrightDimODiagonalWin(self):
         self.game.move(OPLAYER,0,2,0)
         self.game.move(OPLAYER,1,1,1)
         self.game.move(OPLAYER,2,0,2)                                 
         print self.game.prettyStr()
         self.assertEqual(self.game._checkDimensionDiagonalWin_(),(True,OPLAYER))           

     def test_upperrightDimXDiagonalWin(self):
         self.game.move(XPLAYER,0,0,2)
         self.game.move(XPLAYER,1,1,1)
         self.game.move(XPLAYER,2,2,0)                                 
         print self.game.prettyStr()
         self.assertEqual(self.game._checkDimensionDiagonalWin_(),(True,XPLAYER))                               


     def test_lowerleftDimODiagonalWin(self):
         self.game.move(OPLAYER,2,0,0)
         self.game.move(OPLAYER,1,1,1)
         self.game.move(OPLAYER,0,2,2)                                 
         print self.game.prettyStr()
         self.assertEqual(self.game._checkDimensionDiagonalWin_(),(True,OPLAYER))           

     def test_upperleftDimXDiagonalWin(self):
         self.game.move(XPLAYER,0,0,0)
         self.game.move(XPLAYER,1,1,1)
         self.game.move(XPLAYER,2,2,2)                                 
         print self.game.prettyStr()
         self.assertEqual(self.game._checkDimensionDiagonalWin_(),(True,XPLAYER))                               

     def test_topToBottomDimXDiagonalWin(self):
         self.game.move(XPLAYER,0,2,1)
         self.game.move(XPLAYER,1,1,1)
         self.game.move(XPLAYER,2,0,1)                                 
         print self.game.prettyStr()
         self.assertEqual(self.game._checkDimensionDiagonalWin_(),(True,XPLAYER))                                     

     def test_topToBottomDimODiagonalWin(self):
         self.game.move(OPLAYER,0,0,2)
         self.game.move(OPLAYER,1,1,2)
         self.game.move(OPLAYER,2,2,2)                                 
         print self.game.prettyStr()
         self.assertEqual(self.game._checkDimensionDiagonalWin_(),(True,OPLAYER))
                                  
     def test_leftRightDimODiagonalWin(self):
         self.game.move(OPLAYER,0,2,2)
         self.game.move(OPLAYER,1,2,1)
         self.game.move(OPLAYER,2,2,0)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkDimensionDiagonalWin_(),(True,OPLAYER))          

     def test_leftRightDimXDiagonalWin(self):
         self.game.move(XPLAYER,0,0,0)
         self.game.move(XPLAYER,1,0,1)
         self.game.move(XPLAYER,2,0,2)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkDimensionDiagonalWin_(),(True,XPLAYER))       

     def test_noDimDiagonalWin(self):
         self.game.move(OPLAYER,0,0,0)
         self.game.move(OPLAYER,1,1,1)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkDimensionDiagonalWin_(),(False,EMPTY))         

     def test_oLayerDiagonalWin(self):
         self.game.move(OPLAYER,2,0,0)
         self.game.move(OPLAYER,2,1,1)
         self.game.move(OPLAYER,2,2,2)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkLayerDiagonalWin_(),(True,OPLAYER))

     def test_xLayerDiagonalWin(self):
         self.game.move(XPLAYER,0,0,2)
         self.game.move(XPLAYER,0,1,1)
         self.game.move(XPLAYER,0,2,0)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkLayerDiagonalWin_(),(True,XPLAYER))

     def test_noLayerDiagonalWin(self):
         self.game.move(OPLAYER,0,0,0)
         self.game.move(OPLAYER,0,1,1)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkLayerDiagonalWin_(),(False,EMPTY))

     def test_vertOWin(self):
         self.game.move(OPLAYER,0,2,0)
         self.game.move(OPLAYER,1,2,0)
         self.game.move(OPLAYER,2,2,0)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkVerticalWin_(),(True,OPLAYER))

     def test_vertXWin(self):
         self.game.move(XPLAYER,0,1,1)
         self.game.move(XPLAYER,1,1,1)
         self.game.move(XPLAYER,2,1,1)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkVerticalWin_(),(True,XPLAYER))

     def test_noVertWin(self):
         self.game.move(OPLAYER,0,1,2)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkVerticalWin_(),(False,EMPTY))

     def test_colOWin(self):
         self.game.move(XPLAYER,2,2,2)
         self.game.move(OPLAYER,0,0,0)
         self.game.move(OPLAYER,0,1,0)
         self.game.move(OPLAYER,0,2,0)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkColWin_(),(True,OPLAYER))

     def test_colXWin(self):
         self.game.move(OPLAYER,0,1,1)
         self.game.move(XPLAYER,1,0,2)
         self.game.move(XPLAYER,1,1,2)
         self.game.move(XPLAYER,1,2,2)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkColWin_(),(True,XPLAYER))

     def test_noColWin(self):
         self.game.move(OPLAYER,1,2,2)
         self.game.move(XPLAYER,2,2,2)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkColWin_(),(False,EMPTY))

     def test_noRowWin(self):
         self.game.move(XPLAYER,2,1,1)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkRowWin_(),(False,EMPTY))

     def test_rowXWin(self):
         for x in range(self.game.COLUMNS):
             self.game.move(XPLAYER,0,1,x)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkRowWin_(),(True,XPLAYER))

     def test_rowOWin(self):
         for y in range(self.game.COLUMNS):
             self.game.move(OPLAYER,1,2,y)
         print self.game.prettyStr()
         self.assertEqual(self.game._checkRowWin_(),(True,OPLAYER))

     def test_init(self):
         blankboard = [[['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']], [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']], [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]]
         print self.game.prettyStr()
         self.assertEqual(self.game.board,blankboard)

     def test_move(self):
         board = self.game.initboard()
         board[0][2][1] = XPLAYER
         self.game.move(XPLAYER,0,2,1)
         print self.game.prettyStr()
         self.assertEqual(self.game.board,board)

if __name__ == '__main__':
  print "\nThree D Tic-Tac-Toe Demo:\n"
  mygame = threeDTicTacToe()
  mygame.move(XPLAYER,1,0,2)
  print mygame.prettyStr()
  mygame.move(OPLAYER,0,1,1)
  print mygame.prettyStr()
  mygame.move(XPLAYER,1,1,2)
  print mygame.prettyStr()
  mygame.move(OPLAYER,0,2,2)
  print mygame.prettyStr()
  mygame.move(XPLAYER,1,2,2)
  print mygame.prettyStr()
