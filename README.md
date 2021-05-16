# Minesweeper

A minesweeper game I made to develop my Python skills - currently a work in progress!

## Current files
 - Store: the 'Store' class, holds the data and functionality relating to the game's backend data storage. Allows the user to place mines, check if a cell is a mine, and check how many mines there are in the adjacent cells.
 - Visibility: the 'Visibility' class, holds data and functionality relating to the visibility of data in cells in the grid. Allows the user to check if a cell is visible, and make it visible if it is not. (If cells are visible, then the player is able to see how many mines there are near it).
 - Handle_input: validates and sanitises the user inputs, converts them into more usable formats.
 - UI_grid_creation: creates the grid which is printed to the player's command line as the UI.
 - Minesweeper_main: will pull the other files together to run the game.
