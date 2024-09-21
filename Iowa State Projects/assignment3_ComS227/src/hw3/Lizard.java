package hw3;

import static api.Direction.*;

import java.util.ArrayList;

import api.BodySegment;
import api.Cell;
import api.Direction;

/**
 * Represents a Lizard as a collection of body segments.
 */
public class Lizard {

	/**
	 * ArrayList object used to store the segments of this lizard
	 */
	private ArrayList<BodySegment> lizSegments;

	/**
	 * Constructs a Lizard object.
	 */
	public Lizard() {

	}

	/**
	 * Sets the segments of the lizard. Segments should be ordered from tail to
	 * head.
	 * 
	 * @param segments list of segments ordered from tail to head
	 */
	public void setSegments(ArrayList<BodySegment> segments) {
		lizSegments = new ArrayList<BodySegment>();
		for (BodySegment element : segments) {
			lizSegments.add(element);
		}
	}

	/**
	 * Gets the segments of the lizard. Segments are ordered from tail to head.
	 * 
	 * @return a list of segments ordered from tail to head
	 */
	public ArrayList<BodySegment> getSegments() {
		return lizSegments;
	}

	/**
	 * Gets the head segment of the lizard. Returns null if the segments have not
	 * been initialized or there are no segments.
	 * 
	 * @return the head segment
	 */
	public BodySegment getHeadSegment() {
		return lizSegments.get(lizSegments.size() - 1);
	}

	/**
	 * Gets the tail segment of the lizard. Returns null if the segments have not
	 * been initialized or there are no segments.
	 * 
	 * @return the tail segment
	 */
	public BodySegment getTailSegment() {
		return lizSegments.get(0);
	}

	/**
	 * Gets the segment that is located at a given cell or null if there is no
	 * segment at that cell.
	 * 
	 * @param cell to look for lizard
	 * @return the segment that is on the cell or null if there is none
	 */
	public BodySegment getSegmentAt(Cell cell) {
		for (int i = 0; i < lizSegments.size(); i++) { // Iterates through lizSegments
			BodySegment current = lizSegments.get(i);

			if (current.getCell().getCol() == cell.getCol()
					&& current.getCell().getRow() == cell.getRow()) { // Compares the currently selected cell to the provided cell
				return current;
			}
		}
		return null;
	}

	/**
	 * Get the segment that is in front of (closer to the head segment than) the
	 * given segment. Returns null if there is no segment ahead.
	 * 
	 * @param segment the starting segment
	 * @return the segment in front of the given segment or null
	 */
	public BodySegment getSegmentAhead(BodySegment segment) {
		int index = lizSegments.indexOf(segment);
		try {
			return lizSegments.get(index + 1);
		} catch (Exception E) {
			return null;
		}
	}

	/**
	 * Get the segment that is behind (closer to the tail segment than) the given
	 * segment. Returns null if there is not segment behind.
	 * 
	 * @param segment the starting segment
	 * @return the segment behind of the given segment or null
	 */
	public BodySegment getSegmentBehind(BodySegment segment) {
		int index = lizSegments.indexOf(segment);
		try {
			return lizSegments.get(index - 1);
		} catch (Exception E) {
			return null;
		}
	}

	/**
	 * Gets the direction from the perspective of the given segment point to the
	 * segment ahead (in front of) of it. Returns null if there is no segment ahead
	 * of the given segment.
	 * 
	 * @param segment the starting segment
	 * @return the direction to the segment ahead of the given segment or null
	 */
	public Direction getDirectionToSegmentAhead(BodySegment segment) {
		int index = lizSegments.indexOf(segment);
			try {

				int xCoordCurrent = lizSegments.get(index).getCell().getCol();
				int xCoordNext = lizSegments.get(index + 1).getCell().getCol();
				int yCoordCurrent = lizSegments.get(index).getCell().getRow();
				int yCoordNext = lizSegments.get(index + 1).getCell().getRow();

				if (yCoordCurrent > yCoordNext) {
					return UP;
				} else if (yCoordCurrent < yCoordNext) {
					return DOWN;
				} else if (xCoordCurrent > xCoordNext) {
					return LEFT;
				} else if (xCoordCurrent < xCoordNext) {
					return RIGHT;
				}
			} catch (Exception E) {
				return null;
			}
		return null;
	}

	/**
	 * Gets the direction from the perspective of the given segment point to the
	 * segment behind it. Returns null if there is no segment behind of the given
	 * segment.
	 * 
	 * @param segment the starting segment
	 * @return the direction to the segment behind of the given segment or null
	 */
	public Direction getDirectionToSegmentBehind(BodySegment segment) {
		int index = lizSegments.indexOf(segment);
		try {

			int xCoordCurrent = lizSegments.get(index).getCell().getCol();
			int xCoordNext = lizSegments.get(index - 1).getCell().getCol();
			int yCoordCurrent = lizSegments.get(index).getCell().getRow();
			int yCoordNext = lizSegments.get(index - 1).getCell().getRow();

			if (yCoordCurrent > yCoordNext) {
				return UP;
			} else if (yCoordCurrent < yCoordNext) {
				return DOWN;
			} else if (xCoordCurrent > xCoordNext) {
				return LEFT;
			} else if (xCoordCurrent < xCoordNext) {
				return RIGHT;
			}
		} catch (Exception E) {
			return null;
		}
		return null;
	}

	/**
	 * Gets the direction in which the head segment is pointing. This is the
	 * direction formed by going from the segment behind the head segment to the
	 * head segment. A lizard that does not have more than one segment has no
	 * defined head direction and returns null.
	 * 
	 * @return the direction in which the head segment is pointing or null
	 */
	public Direction getHeadDirection() {
		try {
			int temp = lizSegments.size();
			return getDirectionToSegmentAhead(lizSegments.get(temp - 2));

		} catch (Exception E) {
			return null;
		}
	}

	/**
	 * Gets the direction in which the tail segment is pointing. This is the
	 * direction formed by going from the segment ahead of the tail segment to the
	 * tail segment. A lizard that does not have more than one segment has no
	 * defined tail direction and returns null.
	 * 
	 * @return the direction in which the tail segment is pointing or null
	 */
	public Direction getTailDirection() {
		try {
			return getDirectionToSegmentBehind(lizSegments.get(1));
		} catch (Exception E) {
			return null;
		}
	}

	@Override
	public String toString() {
		String result = "";
		for (BodySegment seg : getSegments()) {
			result += seg + " ";
		}
		return result;
	}
}