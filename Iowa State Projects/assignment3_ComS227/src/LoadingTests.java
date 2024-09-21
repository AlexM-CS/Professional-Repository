import static api.Direction.*;

import java.util.ArrayList;

import api.BodySegment;
import api.Cell;
import api.Direction;
import hw3.GameFileUtil;
import hw3.Lizard;
import hw3.LizardGame;
import ui.GameConsole;

public class LoadingTests {
	public static void main(String[] args) {
		
		// ----------------------------------------------------
        // TEST 1 - examples/game1.txt
        // ----------------------------------------------------
        // loadGame1();
        // ----------------------------------------------------
        // TEST 2 - examples/game2.txt
        // ----------------------------------------------------
        // loadGame2();
			
	}
	
	private static void loadGame1() {
		LizardGame game = new LizardGame(0, 0);
		
		GameFileUtil.load("examples/game1.txt", game);
		System.out.println(game);
		System.out.println("Expected the output to be identical to the layout given in 'examples/game1.txt'.");
		System.out.println("Expected a lizard at 2,2 3,2 4,2");
	}
	
	private static void loadGame2() {
		LizardGame game = new LizardGame(0, 0);
		
		GameFileUtil.load("examples/game2.txt", game);
		System.out.println(game);
		System.out.println("Expected the output to be identical to the layout given in 'examples/game2.txt'.");
		System.out.println("Expected a lizard at 5,1 6,1 6,2 5,2 4,2 3,2 2,2");
		System.out.println("Expected a lizard at 1,2 0,2 0,3 0,4 1,4 2,4 3,4 4,4 5,4 6,4 6,5 6,6 5,6 4,6");	
	}
}