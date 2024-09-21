package hw3;

import static api.Direction.*;

import java.util.ArrayList;

import api.Cell;
import api.BodySegment;	
import api.Direction;
import api.Exit;
import api.ScoreUpdateListener;
import api.ShowDialogListener;
import api.Wall;

/**
 * Class that models a game.
 */
public class LizardGame {
	
	/**
	 * An ArrayList used for storing the lizards on a given grid
	 */
	private ArrayList<Lizard> lizards = new ArrayList<>();
	
	/*
	 * An ArrayList comprised of cells making up the grid
	 */
	private ArrayList<Cell> grid;
	
	/**
	 * Integer representing the number of columns on a grid
	 */
	private int boardWidth;
	
	/**
	 * Integer representing the number of rows on a grid
	 */
	private int boardHeight;
	
	/**
	 * Used to display dialog to the user
	 */
	private ShowDialogListener dialogListener;
	
	/**
	 * Used to show information about the number of lizards to the user
	 */
	private ScoreUpdateListener scoreListener;

	/**
	 * Constructs a new LizardGame object with given grid dimensions.
	 * 
	 * @param width  number of columns
	 * @param height number of rows
	 */
	public LizardGame(int width, int height) {

		this.boardWidth = width;
		this.boardHeight = height;

		grid = new ArrayList<>();
		Cell tempCell;

		for (int i = 0; i < width; i++) { // Iterates (width) times
			for (int j = 0; j < height; j++) { // Iterates (height) times

				tempCell = new Cell(i, j);
				grid.add(tempCell);

			}
		}
	}

	/**
	 * Get the grid's width.
	 * 
	 * @return width of the grid
	 */
	public int getWidth() {
		return boardWidth;
	}

	/**
	 * Get the grid's height.
	 * 
	 * @return height of the grid
	 */
	public int getHeight() {
		return boardHeight;
	}

	/**
	 * Adds a wall to the grid.
	 * <p>
	 * Specifically, this method calls placeWall on the Cell object associated with
	 * the wall (see the Wall class for how to get the cell associated with the
	 * wall). This class assumes a cell has already been set on the wall before
	 * being called.
	 * 
	 * @param wall to add
	 */
	public void addWall(Wall wall) {
		wall.getCell().placeWall(wall);
	}

	/**
	 * Adds an exit to the grid.
	 * <p>
	 * Specifically, this method calls placeExit on the Cell object associated with
	 * the exit (see the Exit class for how to get the cell associated with the
	 * exit). This class assumes a cell has already been set on the exit before
	 * being called.
	 * 
	 * @param exit to add
	 */
	public void addExit(Exit exit) {
		exit.getCell().placeExit(exit);
	}

	/**
	 * Gets a list of all lizards on the grid. Does not include lizards that have
	 * exited.
	 * 
	 * @return lizards list of lizards
	 */
	public ArrayList<Lizard> getLizards() {
		return lizards;
	}

	/**
	 * Adds the given lizard to the grid.
	 * <p>
	 * The scoreListener to should be updated with the number of lizards.
	 * 
	 * @param lizard to add
	 */
	public void addLizard(Lizard lizard) {
		lizards.add(lizard);
		ArrayList<BodySegment> segments = lizard.getSegments();

		for (int i = 0; i < segments.size(); i++) {
			segments.get(i).getCell().placeLizard(lizard);
		}	
		
		if (this.scoreListener != null) {
			scoreListener.updateScore(lizards.size());
		}
	}

	/**
	 * Removes the given lizard from the grid. Be aware that each cell object knows
	 * about a lizard that is placed on top of it. It is expected that this method
	 * updates all cells that the lizard used to be on, so that they now have no
	 * lizard placed on them.
	 * <p>
	 * The scoreListener to should be updated with the number of lizards using
	 * updateScore().
	 * 
	 * @param lizard to remove
	 */
	public void removeLizard(Lizard lizard) {
		lizards.remove(lizard);
		ArrayList<BodySegment> segments = lizard.getSegments();
		for (int i = 0; i < segments.size(); i++) {
			segments.get(i).getCell().removeLizard();
		}
		
		if (this.scoreListener != null) {
			scoreListener.updateScore(lizards.size());
		}
	}
	
	/**
	 * Removes the previous lizard from the grid, resets its segments,
	 * then adds it back. This is done inside of this helper method in
	 * order to avoid triggering the scoreListener during this process.
	 * 
	 * @param lizard
	 * @param newSegments
	 */
	private void updateLizard(Lizard lizard, ArrayList<BodySegment> newSegments) {
		ArrayList<BodySegment> segments = lizard.getSegments();
		for (int i = 0; i < segments.size(); i++) {
			segments.get(i).getCell().removeLizard();
		}
		
		lizard.setSegments(newSegments);
		segments = lizard.getSegments();

		for (int i = 0; i < segments.size(); i++) {
			segments.get(i).getCell().placeLizard(lizard);
		}
	}

	/**
	 * Gets the cell for the given column and row.
	 * <p>
	 * If the column or row are outside of the boundaries of the grid the method
	 * returns null.
	 * 
	 * @param col column of the cell
	 * @param row of the cell
	 * @return the cell or null
	 */
	public Cell getCell(int col, int row) {
		for (int i = 0; i < grid.size(); i++) {
			Cell testCell = grid.get(i);
			if ((col == testCell.getCol()) && (row == testCell.getRow())) {
				return testCell;
			}
		}
		return null;
	}

	/**
	 * Gets the cell that is adjacent to (one over from) the given column and row,
	 * when moving in the given direction. For example (1, 4, UP) returns the cell
	 * at (1, 3).
	 * <p>
	 * If the adjacent cell is outside of the boundaries of the grid, the method
	 * returns null.
	 * 
	 * @param col the given column
	 * @param row the given row
	 * @param dir the direction from the given column and row to the adjacent cell
	 * @return the adjacent cell or null
	 */
	public Cell getAdjacentCell(int col, int row, Direction dir) {
		if (dir == UP) { // The adjacent cell upwards is located at (x, y-1)
			try {
				return getCell(col, (row - 1));
			} catch (Exception E) {
				return null;
			}
		} else if (dir == DOWN) { // The adjacent cell downwards is located at (x, y+1)
			try {
				return getCell(col, (row + 1));
			} catch (Exception E) {
				return null;
			}
		} else if (dir == LEFT) { // The adjacent cell to the left is located at (x-1, y)
			try {
				return getCell((col - 1), row);
			} catch (Exception E) {
				return null;
			}
		} else { // The adjacent cell to the right is located at (x+1, y)
			try {
				return getCell((col + 1), row);
			} catch (Exception E) {
				return null;
			}
		}
	}

	/**
	 * Resets the grid. After calling this method the game should have a grid of
	 * size width x height containing all empty cells. Empty means cells with no
	 * walls, exits, etc.
	 * <p>
	 * All lizards should also be removed from the grid.
	 * 
	 * @param width  number of columns of the resized grid
	 * @param height number of rows of the resized grid
	 */
	public void resetGrid(int width, int height) {
		if (lizards.size() != 0) { // Removes all lizards, if any exist
			lizards.clear();
		}

		this.boardWidth = width;
		this.boardHeight = height;

		grid = new ArrayList<>();
		Cell tempCell;

		for (int i = 0; i < width; i++) { // Iterates (width) times
			for (int j = 0; j < height; j++) { // Iterates (height) times
				tempCell = new Cell(i, j);
				grid.add(tempCell);
			}
		}
	}

	/**
	 * Returns true if a given cell location (col, row) is available for a lizard to
	 * move into. Specifically the cell cannot contain a wall or a lizard. Any other
	 * type of cell, including an exit is available.
	 * 
	 * @param row of the cell being tested
	 * @param col of the cell being tested
	 * @return true if the cell is available, false otherwise
	 */
	public boolean isAvailable(int col, int row) {
		Cell testCell = getCell(col, row);
		if (testCell != null) {
			return (testCell.getWall() == null) && (testCell.getLizard() == null);
		}
		return false;
	}

	/**
	 * Move the lizard specified by its body segment at the given position (col,
	 * row) one cell in the given direction. The entire body of the lizard must move
	 * in a snake like fashion, in other words, each body segment pushes and pulls
	 * the segments it is connected to forward or backward in the path of the
	 * lizard's body. The given direction may result in the lizard moving its body
	 * either forward or backward by one cell.
	 * <p>
	 * The segments of a lizard's body are linked together and movement must always
	 * be "in-line" with the body. It is allowed to implement movement by either
	 * shifting every body segment one cell over or by creating a new head or tail
	 * segment and removing an existing head or tail segment to achieve the same
	 * effect of movement in the forward or backward direction.
	 * <p>
	 * If any segment of the lizard moves over an exit cell, the lizard should be
	 * removed from the grid.
	 * <p>
	 * If there are no lizards left on the grid the player has won the puzzle the
	 * the dialog listener should be used to display (see showDialog) the message
	 * "You win!".
	 * <p>
	 * // REQUIREMENT 1 // SOLVED
	 * It is possible that the given direction is not in-line with the body of the
	 * lizard (as described above), in that case this method should do nothing.
	 * <p>
	 * // REQUIREMENT 2 // SOLVED
	 * It is possible that the given column and row are outside the bounds of the
	 * grid, in that case this method should do nothing.
	 * <p>
	 * // REQUIREMENT 3 // SOLVED
	 * It is possible that there is no lizard at the given column and row, in that
	 * case this method should do nothing.
	 * <p>
	 * // REQUIREMENT 4 // SOLVED
	 * It is possible that the lizard is blocked and cannot move in the requested
	 * direction, in that case this method should do nothing.
	 * <p>
	 * <b>Developer's note: You may have noticed that there are a lot of details
	 * that need to be considered when implementing this method. It is highly
	 * recommend to explore how you can use the public API methods of this class,
	 * Grid and Lizard (hint: there are many helpful methods in those classes that
	 * will simplify your logic here) and also create your own private helper
	 * methods. Break the problem into smaller parts are work on each part
	 * individually.</b>
	 * 
	 * @param col the given column of a selected segment
	 * @param row the given row of a selected segment
	 * @param dir the given direction to move the selected segment
	 */
	public void move(int col, int row, Direction dir) {
		Cell currentCell = getCell(col, row);
		Cell cellToMoveTo = getAdjacentCell(col, row, dir);

		if (moveChecks(currentCell, cellToMoveTo)) {
			Lizard lizardOnCell = currentCell.getLizard();
			BodySegment headSegment = lizardOnCell.getHeadSegment();
			BodySegment tailSegment = lizardOnCell.getTailSegment();
			ArrayList<BodySegment> segments = lizardOnCell.getSegments();
			ArrayList<BodySegment> newSegments = new ArrayList<>();

			if ((currentCell.getCol() == headSegment.getCell().getCol())
					&& (currentCell.getRow() == headSegment.getCell().getRow())) {
				// The user is attempting to move the head

				if (isAvailable(cellToMoveTo.getCol(), cellToMoveTo.getRow())) { // The cell is available to move into
					headIsMoving(col, row, dir, lizardOnCell, segments, newSegments);
					
				} else if (dir == lizardOnCell.getDirectionToSegmentBehind(headSegment)) { // Check to see if the head is moving "in-line" backwards
					tailIsMoving(tailSegment.getCell().getCol(), tailSegment.getCell().getRow(), lizardOnCell.getTailDirection(), lizardOnCell, segments, newSegments);
					
				} else { // Cell is not available, method does nothing
					return;
				}

			} else if ((currentCell.getCol() == tailSegment.getCell().getCol())
					&& (currentCell.getRow() == tailSegment.getCell().getRow())) {
				// The user is attempting to move the tail

				if (isAvailable(cellToMoveTo.getCol(), cellToMoveTo.getRow())) { // The cell is available to move into
					tailIsMoving(col, row, dir, lizardOnCell, segments, newSegments);
					
				} else if (dir == lizardOnCell.getDirectionToSegmentAhead(tailSegment)) { // Check to see if the tail is moving "in-line" forwards
					headIsMoving(headSegment.getCell().getCol(), headSegment.getCell().getRow(), lizardOnCell.getHeadDirection(), lizardOnCell, segments, newSegments);
					
				} else { // Cell is not available, method does nothing
					return;
				}

			} else { // The user is attempting to move a middle segment
				BodySegment middleSegment = lizardOnCell.getSegmentAt(currentCell);

				if (dir == lizardOnCell.getDirectionToSegmentAhead(middleSegment)) {
					// Check to see if the attempted movement is "in-line" going forwards

					Direction headDirection = lizardOnCell.getHeadDirection();
					Cell headCell = getCell(headSegment.getCell().getCol(), headSegment.getCell().getRow());

					for (int i = 0; i < (segments.size() - 1); i++) {
						newSegments.add(segments.get((i + 1)));
					}
					
					middleIsMoving(headCell, headDirection, lizardOnCell, segments, newSegments);

				} else if (dir == lizardOnCell.getDirectionToSegmentBehind(middleSegment)) {
					// Check to see if the movement is "in-line" going backwards

					Direction tailDirection = lizardOnCell.getTailDirection();
					Cell tailCell = getCell(tailSegment.getCell().getCol(), tailSegment.getCell().getRow());
					
					middleIsMoving(tailCell, tailDirection, lizardOnCell, segments, newSegments);
					
					for (int i = 1; i < segments.size(); i++) { // Adds all other cells after the tail is added
						newSegments.add(segments.get(i - 1));
					}
				} else { // Movement is not "in-line": method does nothing
					return;
				}
			}

			for (int i = 0; i < newSegments.size(); i++) { // Makes sure the new segment list is correct
				if (newSegments.get(i) == null) {
					return;
				}
			}
			
			updateLizard(lizardOnCell, newSegments);

			for (int i = 0; i < newSegments.size(); i++) { // Checks to see if any cells of the lizard are on exits
				Cell lizardCell = newSegments.get(i).getCell();

				if (lizardCell.getExit() != null) { // There IS an exit on this cell
					removeLizard(lizardOnCell);

					if ((lizards.size() == 0) && (this.dialogListener != null)) { // There are no remaining lizards
						dialogListener.showDialog("You win!");
					}
				}
			}
		}
	}
	
	/**
	 * Helper function used to move the head of the lizard
	 * 
	 * @param col the column of the head's corresponding cell
	 * @param row the row of the head's corresponding cell
	 * @param dir the direction the head is trying to move
	 * @param lizard the lizard to be moved
	 * @param segments an ArrayList of the lizard's segments before it is moved
	 * @param newSegments an ArrayList of the lizard's segments after it is moved
	 */
	private void headIsMoving(int col, int row, Direction dir, Lizard lizard, ArrayList<BodySegment> segments, ArrayList<BodySegment> newSegments) {
		for (int i = 0; i < (segments.size() - 1); i++) { // Adds every cell before the head is added
			newSegments.add(segments.get((i + 1)));
		}
		if (dir == UP) { // The head is trying to move up: (x, (y - 1))
			newSegments.add(new BodySegment(lizard, getCell(col, (row - 1))));
		} else if (dir == DOWN) { // The head is trying to move down: (x, (y + 1))
			newSegments.add(new BodySegment(lizard, getCell(col, (row + 1))));
		} else if (dir == LEFT) { // The head is trying to move left: ((x - 1), y)
			newSegments.add(new BodySegment(lizard, getCell((col - 1), row)));
		} else { // The head is trying to move right: ((x + 1), y)
			newSegments.add(new BodySegment(lizard, getCell((col + 1), row)));
		}
	}
	
	/**
	 * Helper function used to move the tail of the lizard
	 * 
	 * @param col the column of the tail's corresponding cell
	 * @param row the row of the tail's corresponding cell
	 * @param dir the direction the tail is trying to move
	 * @param lizard the lizard to be moved
	 * @param segments an ArrayList of the lizard's segments before it is moved
	 * @param newSegments an ArrayList of the lizard's segments after it is moved
	 */
	private void tailIsMoving(int col, int row, Direction dir, Lizard lizard, ArrayList<BodySegment> segments, ArrayList<BodySegment> newSegments) {
		if (dir == UP) { // The tail is trying to move up: (x, (y - 1))
			newSegments.add(new BodySegment(lizard, getCell(col, (row - 1))));
		} else if (dir == DOWN) { // The tail is trying to move down: (x, (y + 1))
			newSegments.add(new BodySegment(lizard, getCell(col, (row + 1))));
		} else if (dir == LEFT) { // The tail is trying to move left: ((x - 1), y)
			newSegments.add(new BodySegment(lizard, getCell((col - 1), row)));
		} else { // The tail is trying to move right: ((x + 1), y)
			newSegments.add(new BodySegment(lizard, getCell((col + 1), row)));
		}
		for (int i = 1; i < segments.size(); i++) { // Adds all other cells after the tail is added
			newSegments.add(segments.get(i - 1));
		}
	}
	
	/**
	 * Helper function used to move a middle segment of the lizard
	 * 
	 * @param col the column of the segment's corresponding cell
	 * @param row the row of the segment's corresponding cell
	 * @param dir the direction the segment is trying to move
	 * @param lizard the lizard to be moved
	 * @param segments an ArrayList of the lizard's segments before it is moved
	 * @param newSegments an ArrayList of the lizard's segments after it is moved
	 */
	private void middleIsMoving(Cell segmentCell, Direction segmentDir, Lizard lizard, ArrayList<BodySegment> segments, ArrayList<BodySegment> newSegments) {
		if (segmentDir == UP) { // The tail is trying to move up
			if (isAvailable(segmentCell.getCol(), (segmentCell.getRow() - 1))) {
				newSegments.add(
						new BodySegment(lizard, getCell(segmentCell.getCol(), (segmentCell.getRow() - 1))));
			} else { // Cell is occupied, either by a wall or lizard
				return;
			}
		} else if (segmentDir == DOWN) { // The tail is trying to move down
			if (isAvailable(segmentCell.getCol(), (segmentCell.getRow() + 1))) {
				newSegments.add(
						new BodySegment(lizard, getCell(segmentCell.getCol(), (segmentCell.getRow() + 1))));
			} else { // Cell is occupied, either by a wall or lizard
				return;
			}
		} else if (segmentDir == LEFT) { // The tail is trying to move left
			if (isAvailable((segmentCell.getCol() - 1), segmentCell.getRow())) {
				newSegments.add(
						new BodySegment(lizard, getCell((segmentCell.getCol() - 1), segmentCell.getRow())));
			} else { // Cell is occupied, either by a wall or lizard
				return;
			}
		} else { // The tail is trying to move right
			if (isAvailable((segmentCell.getCol() + 1), segmentCell.getRow())) {
				newSegments.add(
						new BodySegment(lizard, getCell((segmentCell.getCol() + 1), segmentCell.getRow())));
			} else { // Cell is occupied, either by a wall or lizard
				return;
			}
		}
	}
	
	/**
	 * Helper method used to do various boolean checks related to lizard movement
	 * 
	 * @param currentCell the current cell to be moved
	 * @param cellToMoveTo the adjacent to to be moved to
	 * @return boolean if currentCell and cellToMoveTo exist, and if there is a lizard present on currentCell
	 */
	private boolean moveChecks(Cell currentCell, Cell cellToMoveTo) {
		return (currentCell != null) && (currentCell.getLizard() != null) && (cellToMoveTo != null);
	}

	/**
	 * Sets callback listeners for game events.
	 * 
	 * @param dialogListener listener for creating a user dialog
	 * @param scoreListener  listener for updating the player's score
	 */
	public void setListeners(ShowDialogListener dialogListener, ScoreUpdateListener scoreListener) {
		this.dialogListener = dialogListener;
		this.scoreListener = scoreListener;
	}

	/**
	 * Load the game from the given file path
	 * 
	 * @param filePath location of file to load
	 */
	public void load(String filePath) {
		GameFileUtil.load(filePath, this);
	}

	@Override
	public String toString() {
		String str = "---------- GRID ----------\n";
		str += "Dimensions:\n";
		str += getWidth() + " " + getHeight() + "\n";
		str += "Layout:\n";
		for (int y = 0; y < getHeight(); y++) {
			if (y > 0) {
				str += "\n";
			}
			for (int x = 0; x < getWidth(); x++) {
				str += getCell(x, y);
			}
		}
		str += "\nLizards:\n";
		for (Lizard l : getLizards()) {
			str += l;
		}
		str += "\n--------------------------\n";
		return str;
	}
}