package hw3;

import java.util.ArrayList;
import java.util.Scanner;

import java.io.File;
import api.BodySegment;
import api.Cell;
import api.Exit;
import api.Wall;

/**
 * Utility class with static methods for loading game files.
 */
public class GameFileUtil {
	/**
	 * Loads the file at the given file path into the given game object. When the
	 * method returns the game object has been modified to represent the loaded
	 * game.
	 * 
	 * @param filePath the path of the file to load
	 * @param game     the game to modify
	 */
	public static void load(String filePath, LizardGame game) {

		/*
		 * --- FORMAT FOR FILES ---
		 * (This will be using example 2 to describe the format)
		 *
		 * Section 1: Grid dimensions (width)x(height)
		 * 8x8
		 * 
		 * 
		 * Section 2: Grid layout (Walls (W) and Exits (E))
		 * _ _ W _ _ W W _ . <- End of the grid
		 * _ W W W _ _ _ W .
		 * _ _ _ _ _ _ _ _ .
		 * _ W W W W W W _ .
		 * _ _ _ _ _ _ _ E .
		 * _ W W W W W _ W .
		 * _ _ _ W _ _ _ W .
		 * _ _ _ W _ _ W _ .
		 * 
		 * Section 3: Lizards (x1,y1) (x2,y2)...
		 * L 5,1 6,1 6,2 5,2 4,2 3,2 2,2
		 * L 1,2 0,2 0,3 0,4 1,4 2,4 3,4 4,4 5,4 6,4 6,5 6,6 5,6 4,6
		 */
		
		try {
			File file = new File(filePath); // Step 1: retrieve the file to be used
			Scanner s = new Scanner(file);

			String line = s.nextLine();

			String[] dimensions = line.split("x"); // Step 2: collect the dimensions of the grid from the file
			int width = Integer.parseInt(dimensions[0]);
			int height = Integer.parseInt(dimensions[1]);

			game.resetGrid(width, height); // Step 3: create the game of dimensions width x height
			// System.out.println(game); // DEBUG- was game constructed correctly? PASSED

			for (int i = 0; i < height; i++) {
				line = s.nextLine(); // Step 4: collect the next line's data

				for (int j = 0; j < width; j++) { // Step 5: collect each character in the line
					char token = line.charAt(j);

					if (token == ' ') { // There is no object at these coordinates
						continue;
					} else if (token == '.') { // This is the end of this row
						break;
					} else if (token == 'W') { // There is a wall at these coordinates
						Cell thisCell = game.getCell(j, i);
						Wall thisWall = new Wall(thisCell);
						thisCell.placeWall(thisWall);
					} else if (token == 'E') { // There is an exit at these coordinates
						Cell thisCell = game.getCell(j, i);
						Exit thisExit = new Exit(thisCell);
						thisCell.placeExit(thisExit);
					} else { // There is some other token unitended to be there
						s.close();
						throw new RuntimeException();
					}
				}
			}
			// System.out.println(game); // DEBUG- was game edited correctly? PASSED

			while (s.hasNextLine()) { // Step 6: add all lizards, if any, to the grid
				line = s.nextLine();
				String[] coordinates = line.split(" ");
				
				Lizard thisLizard = new Lizard();
				ArrayList<BodySegment> theseSegments = new ArrayList<>();

				for (int i = 0; i < coordinates.length; i++) {
					String element = coordinates[i];
					
					if (element.equals("L")) { // The first element in each array will be this string, which we don't need
						continue;
					} else { // Every other element will take the format (x),(y)
						String[] values = element.split(",");
						theseSegments.add(new BodySegment(thisLizard, game.getCell(Integer.parseInt(values[0]), Integer.parseInt(values[1]))));
					}
				}
				thisLizard.setSegments(theseSegments);
				game.addLizard(thisLizard);
				thisLizard = new Lizard();
				theseSegments = new ArrayList<BodySegment>();
			}
			s.close();
			// System.out.println(game); // DEBUG- were lizards added correctly? PASSED

		} catch (Exception E) {
			E.printStackTrace();
			return;
		}
	}
}