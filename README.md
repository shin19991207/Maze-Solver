# Maze-Solver
A maze solving algorithm in python with BFS that finds the shortest solution to Robert Abbott's Alice Mazes (https://www.logicmazes.com/alice.html), given an input text file representation of the maze.

## Input Text File Representation of an Alice Maze
- The location of a cell in the maze should be written in the format *(row#, column#)*. Both row number and column number start from 0.
- The first line states the width (number of columns) of the maze.
- The second line specifies the start location in the format *“s=(row#,column#)”* (without the quotations marks and any spaces).
- The third line specifies the goal location in the format *“g=(row#, column#)”*.
- Starting on the forth line, each line represents a row of the maze with width number of cells.
Each cell, except the goal location, is written in the format *“color:(direction)”*, where *color* is color of the arrow(s) and *direction* is the direction(s) of the arrow(s) in the cell.
Each cell representation is separated by a single space.
  – *color* should be one of b, r, or y, which represents black, red, or yellow, respectively.
  – There are 8 possible directions and each should be written as one of the following abbr.
  
  | abbr. | description |
  | ----- | ----------- |
  | l | left |
  | r | right |
  | u | up |
  | d | down |
  | ur | up right|
  | ul | up left |
  | dr | down right |
  | dl | down left |

  – If there is more than one arrow in a cell, separate each direction with a single comma. The order does not matter.
  – If the cell is the goal location, simply write *"goal"* (without the quotation marks).
  
- An example representation of [this small maze](https://github.com/shin19991207/Maze-Solver/blob/main/docs/example_maze.png) is as below:

  <img src="https://github.com/shin19991207/Maze-Solver/blob/main/docs/example_maze.png" width="200">
  
  ```
  3
  s=(2,0)
  g=(0,1)
  r:(r,dr,d) goal y:(dl) 
  b:(u) b:(u) b:(dl) 
  b:(u,r) b:(r) b:(u)
  ```
