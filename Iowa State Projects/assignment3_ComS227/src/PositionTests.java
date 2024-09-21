import java.util.ArrayList;

import api.BodySegment;
import api.Cell;
import api.Direction;
import hw3.Lizard;

/**
 * Examples of using the LizardGame, GameFileUtil, and Lizard classes. The
 * main() method in this class only displays to the console. For the full game
 * GUI, run the ui.GameMain class.
 */
public class PositionTests {
	public static void main(String args[]) {

		Lizard liz1 = new Lizard(); // First Lizard
		Cell cell0 = new Cell(1, 1); // Tail segment
		Cell cell1 = new Cell(2, 1); // Middle segment
		Cell cell2 = new Cell(2, 2); // Head segment

		ArrayList<BodySegment> segments = new ArrayList<BodySegment>(); // Creates a new ArrayList object to contain the
																		// information we will pass to our lizard

		segments.add(new BodySegment(liz1, cell0));
		segments.add(new BodySegment(liz1, cell1));
		segments.add(new BodySegment(liz1, cell2));

		liz1.setSegments(segments);
		BodySegment middleSegment = liz1.getSegmentAt(cell1);

		// X-Coordinate of middle segment: 2 | B | M |
		// X-Coordinate of ahead segment: 2 |-------|
		// Y-Coordinate of middle segment: 1 | . | A |
		// Y-Coordinate of ahead segment: 2 |-------|

		Direction aheadDir = liz1.getDirectionToSegmentAhead(middleSegment);
		System.out.println("From the middle segment, ahead is " + aheadDir + ", expected DOWN."); // PASSED
		Direction behindDir = liz1.getDirectionToSegmentBehind(middleSegment);
		System.out.println("From the middle segment, behind is " + behindDir + ", expected LEFT."); // PASSED
		Direction headFacing = liz1.getHeadDirection();
		System.out.println("The head is pointing " + headFacing + ", expected DOWN."); // PASSED
		Direction tailFacing = liz1.getTailDirection();
		System.out.println("The head is pointing " + tailFacing + ", expected LEFT."); // PASSED

		System.out.println();

		Lizard liz2 = new Lizard(); // Second Lizard
		cell0 = new Cell(2, 2); // Tail segment
		cell1 = new Cell(1, 2); // Middle segment
		cell2 = new Cell(1, 1); // Head segment

		segments = new ArrayList<BodySegment>(); // Creates a new ArrayList object to contain the information we will
													// pass to our lizard

		segments.add(new BodySegment(liz2, cell0));
		segments.add(new BodySegment(liz2, cell1));
		segments.add(new BodySegment(liz2, cell2));

		liz2.setSegments(segments);
		middleSegment = liz2.getSegmentAt(cell1);

		// X-Coordinate of middle segment: 1 | A | . |
		// X-Coordinate of ahead segment: 1 |-------|
		// Y-Coordinate of middle segment: 2 | M | B |
		// Y-Coordinate of ahead segment: 1 |-------|

		aheadDir = liz2.getDirectionToSegmentAhead(middleSegment);
		System.out.println("From the middle segment, ahead is " + aheadDir + ", expected UP."); // PASSED
		behindDir = liz2.getDirectionToSegmentBehind(middleSegment);
		System.out.println("From the middle segment, behind is " + behindDir + ", expected RIGHT."); // PASSED
		headFacing = liz2.getHeadDirection();
		System.out.println("The head is pointing " + headFacing + ", expected UP.");
		tailFacing = liz2.getTailDirection();
		System.out.println("The head is pointing " + tailFacing + ", expected RIGHT.");

		System.out.println();

		Lizard liz3 = new Lizard(); // Third Lizard
		cell0 = new Cell(2, 1); // Tail segment
		cell1 = new Cell(1, 1); // Middle segment
		cell2 = new Cell(1, 2); // Head segment

		segments = new ArrayList<BodySegment>(); // Creates a new ArrayList object to contain the information we will
													// pass to our lizard

		segments.add(new BodySegment(liz3, cell0));
		segments.add(new BodySegment(liz3, cell1));
		segments.add(new BodySegment(liz3, cell2));

		liz3.setSegments(segments);
		middleSegment = liz3.getSegmentAt(cell1);

		// X-Coordinate of middle segment: 1 | M | B |
		// X-Coordinate of ahead segment: 1 |-------|
		// Y-Coordinate of middle segment: 2 | A | . |
		// Y-Coordinate of ahead segment: 1 |-------|

		aheadDir = liz3.getDirectionToSegmentAhead(middleSegment);
		System.out.println("From the middle segment, ahead is " + aheadDir + ", expected DOWN."); // PASSED
		behindDir = liz3.getDirectionToSegmentBehind(middleSegment);
		System.out.println("From the middle segment, behind is " + behindDir + ", expected RIGHT."); // PASSED
		headFacing = liz3.getHeadDirection();
		System.out.println("The head is pointing " + headFacing + ", expected DOWN.");
		tailFacing = liz3.getTailDirection();
		System.out.println("The head is pointing " + tailFacing + ", expected RIGHT.");

		System.out.println();

		Lizard liz4 = new Lizard(); // Fourth Lizard
		cell0 = new Cell(2, 1); // Tail segment
		cell1 = new Cell(2, 2); // Middle segment
		cell2 = new Cell(1, 2); // Head segment

		segments = new ArrayList<BodySegment>(); // Creates a new ArrayList object to contain the information we will
													// pass to our lizard

		segments.add(new BodySegment(liz4, cell0));
		segments.add(new BodySegment(liz4, cell1));
		segments.add(new BodySegment(liz4, cell2));

		liz4.setSegments(segments);
		middleSegment = liz4.getSegmentAt(cell1);

		// X-Coordinate of middle segment: 1 | . | B |
		// X-Coordinate of ahead segment: 1 |-------|
		// Y-Coordinate of middle segment: 2 | A | M |
		// Y-Coordinate of ahead segment: 1 |-------|

		aheadDir = liz4.getDirectionToSegmentAhead(middleSegment);
		System.out.println("From the middle segment, ahead is " + aheadDir + ", expected LEFT."); // PASSED
		behindDir = liz4.getDirectionToSegmentBehind(middleSegment);
		System.out.println("From the middle segment, behind is " + behindDir + ", expected UP."); // PASSED
		headFacing = liz4.getHeadDirection();
		System.out.println("The head is pointing " + headFacing + ", expected LEFT.");
		tailFacing = liz4.getTailDirection();
		System.out.println("The head is pointing " + tailFacing + ", expected UP.");

		System.out.println();

		Lizard liz5 = new Lizard(); // Fifth Lizard
		cell0 = new Cell(1, 2); // Tail segment
		cell1 = new Cell(1, 1); // Middle segment
		cell2 = new Cell(2, 1); // Head segment

		segments = new ArrayList<BodySegment>(); // Creates a new ArrayList object to contain the information we will
													// pass to our lizard

		segments.add(new BodySegment(liz5, cell0));
		segments.add(new BodySegment(liz5, cell1));
		segments.add(new BodySegment(liz5, cell2));

		liz5.setSegments(segments);
		middleSegment = liz5.getSegmentAt(cell1);

		// X-Coordinate of middle segment: 1 | M | A |
		// X-Coordinate of ahead segment: 1 |-------|
		// Y-Coordinate of middle segment: 2 | B | . |
		// Y-Coordinate of ahead segment: 1 |-------|

		aheadDir = liz5.getDirectionToSegmentAhead(middleSegment);
		System.out.println("From the middle segment, ahead is " + aheadDir + ", expected RIGHT."); // PASSED
		behindDir = liz5.getDirectionToSegmentBehind(middleSegment);
		System.out.println("From the middle segment, behind is " + behindDir + ", expected DOWN."); // PASSED
		headFacing = liz5.getHeadDirection();
		System.out.println("The head is pointing " + headFacing + ", expected RIGHT.");
		tailFacing = liz5.getTailDirection();
		System.out.println("The head is pointing " + tailFacing + ", expected DOWN.");
	}
}