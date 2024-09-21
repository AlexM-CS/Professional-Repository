import static api.Direction.*;

import java.util.ArrayList;

import api.BodySegment;
import api.Cell;
import api.Exit;
import api.Wall;
import hw3.Lizard;
import hw3.LizardGame;
import ui.GameConsole;

public class GameTests {
    public static void main(String[] args) {
        // ----------------------------------------------------
        // TEST 1 - Board Dimensions, Objects
        // ----------------------------------------------------
        // test1();
        // ----------------------------------------------------
        // TEST 2 - Adding and Removing Lizards
        // ----------------------------------------------------
        // test2();
        // ----------------------------------------------------
        // TEST 3 - Moving Lizard's Head and Exit Testing
        // ----------------------------------------------------
        // test3();
        // ----------------------------------------------------
        // TEST 4 - Moving Lizard's Tail and Wall Testing
        // ----------------------------------------------------
        // test4();
        // ----------------------------------------------------
        // TEST 5 - Moving Lizard's Middle and Out-of-Bounds Testing
        // ----------------------------------------------------
        // test5();
        // ----------------------------------------------------
        // TEST 6 - Moving Multiple Lizards and Testing Lizard Collision
        // ----------------------------------------------------
        // test6();
        // ----------------------------------------------------
        // TEST 7 - Testing Game Ending Sequence
        // ----------------------------------------------------
        // test7();
    }

    private static void test1() {
        LizardGame game = new LizardGame(4, 4);
        System.out.println(game);
        System.out.println("The board's width is " + game.getWidth() + ", expected 4."); // PASSED
        System.out.println("The board's height is " + game.getHeight() + ", expected 4."); // PASSED

        game.resetGrid(2, 2);
        System.out.println("The board's width is " + game.getWidth() + ", expected 6."); // PASSED
        System.out.println("The board's height is " + game.getHeight() + ", expected 6."); // PASSED

        Wall wall = new Wall(game.getCell(0, 0));
        game.addWall(wall);
        System.out.println(game);
        System.out.println("Expected a wall at 0, 0"); // PASSED

        Exit exit = new Exit(game.getCell(1, 0));
        game.addExit(exit);
        System.out.println(game);
        System.out.println("Expected a wall at 0, 0 & an exit at 1, 0"); // PASSED

        game.resetGrid(3, 3);
        System.out.println(game);
        System.out.println("The board's width is " + game.getWidth() + ", expected 3."); // PASSED
        System.out.println("The board's height is " + game.getHeight() + ", expected 3."); // PASSED
        System.out.println("Expected no walls or exits."); // PASSED
    }

    private static void test2() {
        LizardGame game = new LizardGame(4, 4);
        Lizard liz1 = new Lizard();

        Cell cell0 = new Cell(0, 0);
        Cell cell1 = new Cell(1, 0);
        Cell cell2 = new Cell(2, 0);
        Cell cell3 = new Cell(3, 0);

        ArrayList<BodySegment> segments1 = new ArrayList<>();
        segments1.add(new BodySegment(liz1, cell0));
        segments1.add(new BodySegment(liz1, cell1));
        segments1.add(new BodySegment(liz1, cell2));
        segments1.add(new BodySegment(liz1, cell3));
        liz1.setSegments(segments1);

        game.addLizard(liz1);
        System.out.println(game);
        System.out.println("Expected a lizard at 0,0 1,0 2,0 3,0"); // PASSED

        Lizard liz2 = new Lizard();

        Cell cell4 = new Cell(0, 3);
        Cell cell5 = new Cell(1, 3);
        Cell cell6 = new Cell(2, 3);
        Cell cell7 = new Cell(3, 3);

        ArrayList<BodySegment> segments2 = new ArrayList<>();
        segments2.add(new BodySegment(liz1, cell4));
        segments2.add(new BodySegment(liz1, cell5));
        segments2.add(new BodySegment(liz1, cell6));
        segments2.add(new BodySegment(liz1, cell7));
        liz2.setSegments(segments2);

        game.addLizard(liz2);
        System.out.println(game);
        System.out.println("List of lizards: " + game.getLizards());
        System.out.println("Expected a lizard at 0,0 1,0 2,0 3,0"); // PASSED
        System.out.println("Expected a lizard at 0,3 1,3 2,3 3,3"); // PASSED

        game.removeLizard(liz2);
        System.out.println(game);
        System.out.println("List of lizards: " + game.getLizards());
        System.out.println("Expected a lizard at 0,0 1,0 2,0 3,0"); // PASSED

        game.removeLizard(liz1);
        System.out.println(game);
        System.out.println("List of lizards: " + game.getLizards());
        System.out.println("Expected no lizards"); // PASSED
    }

    private static void test3() {
        LizardGame game = new LizardGame(3, 3);
        Lizard liz = new Lizard();
        ArrayList<BodySegment> segments = new ArrayList<>();
        Cell cell0 = new Cell(0, 0);
        Cell cell1 = new Cell(1, 0);
        Cell cell2 = new Cell(2, 0);
        segments.add(new BodySegment(liz, cell0));
        segments.add(new BodySegment(liz, cell1));
        segments.add(new BodySegment(liz, cell2));
        liz.setSegments(segments);
        game.addLizard(liz);
        Exit exit = new Exit(game.getCell(2, 2));
        game.addExit(exit);

        System.out.println(game);
        System.out.println("Expected a lizard at 0,0 1,0 2,0"); // PASSED
        System.out.println("Expected an exit at 2,2"); // PASSED

        game.move(2, 0, DOWN); // Try moving the head down
        System.out.println(game);
        System.out.println("Expected a lizard at 1,0 2,0 2,1"); // PASSED
        System.out.println("Expected an exit at 2,2"); // PASSED

        game.move(2, 1, LEFT); // Try moving the head left
        System.out.println(game);
        System.out.println("Expected a lizard at 2,0 2,1 1,1"); // PASSED
        System.out.println("Expected an exit at 2,2"); // PASSED

        game.move(1, 1, UP); // Try moving the head up
        System.out.println(game);
        System.out.println("Expected a lizard at 2,1 1,1 1,0"); // PASSED
        System.out.println("Expected an exit at 2,2"); // PASSED

        game.move(1, 0, RIGHT); // Try moving the head right
        System.out.println(game);
        System.out.println("Expected a lizard at 1,1 1,0 2,0"); // PASSED
        System.out.println("Expected an exit at 2,2"); // PASSED

        game.move(2, 0, DOWN);
        game.move(2, 1, DOWN); // Try moving the head into the exit
        System.out.println(game);
        System.out.println("Expected no lizards"); // PASSED
        System.out.println("Expected an exit at 2,2"); // PASSED
        
        LizardGame game2 = new LizardGame(4, 1);
        liz = new Lizard();
        segments = new ArrayList<>();
        cell0 = new Cell(1, 0);
        cell1 = new Cell(2, 0);
        cell2 = new Cell(3, 0);
        segments.add(new BodySegment(liz, cell0));
        segments.add(new BodySegment(liz, cell1));
        segments.add(new BodySegment(liz, cell2));
        liz.setSegments(segments);
        game2.addLizard(liz);
        
        System.out.println(game2);
        System.out.println("Expected a lizard at 1,0 2,0 3,0"); // PASSED
        
        game2.move(3, 0, LEFT); // Try moving the head backwards into itself
        System.out.println(game2);
        System.out.println("Expected a lizard at 0,0 1,0 2,0"); // PASSED
    }

    private static void test4() {
        LizardGame game = new LizardGame(3, 3);
        Lizard liz = new Lizard();
        Cell cell0 = new Cell(0, 0);
        Cell cell1 = new Cell(1, 0);
        Cell cell2 = new Cell(2, 0);
        ArrayList<BodySegment> segments = new ArrayList<>();
        segments.add(new BodySegment(liz, cell0));
        segments.add(new BodySegment(liz, cell1));
        segments.add(new BodySegment(liz, cell2));
        liz.setSegments(segments);
        game.addLizard(liz);

        Wall wall = new Wall(game.getCell(2, 2));
        game.addWall(wall);

        System.out.println(game);
        System.out.println("Expected a lizard at 0,0 1,0 2,0"); // PASSED
        System.out.println("Expected a wall at 2,2"); // PASSED

        game.move(0, 0, DOWN);
        System.out.println(game);
        System.out.println("Expected a lizard at 0,1 0,0 1,0"); // PASSED
        System.out.println("Expected a wall at 2,2"); // PASSED

        game.move(0, 1, RIGHT);
        System.out.println(game);
        System.out.println("Expected a lizard at 1,1 0,1 0,0"); // PASSED
        System.out.println("Expected a wall at 2,2"); // PASSED

        game.move(1, 1, UP);
        System.out.println(game);
        System.out.println("Expected a lizard at 1,0 1,1 0,1"); // PASSED
        System.out.println("Expected a wall at 2,2"); // PASSED

        game.move(1, 0, RIGHT);
        game.move(2, 0, DOWN);
        game.move(2, 1, LEFT);
        System.out.println(game);
        System.out.println("Expected a lizard at 1,1 2,1 2,0"); // PASSED
        System.out.println("Expected a wall at 2,2"); // PASSED

        game.move(1, 1, DOWN);
        game.move(1, 2, RIGHT); // This move should get stopped by the wall
        System.out.println(game);
        System.out.println("Expected a lizard at 1,2 1,1 2,1"); // PASSED
        System.out.println("Expected a wall at 2,2"); // PASSED

        game.removeLizard(liz);
        
        LizardGame game2 = new LizardGame(4, 1);
        liz = new Lizard();
        segments = new ArrayList<>();
        cell0 = new Cell(0, 0);
        cell1 = new Cell(1, 0);
        cell2 = new Cell(2, 0);
        segments.add(new BodySegment(liz, cell0));
        segments.add(new BodySegment(liz, cell1));
        segments.add(new BodySegment(liz, cell2));
        liz.setSegments(segments);
        game2.addLizard(liz);
        
        System.out.println(game2);
        System.out.println("Expected a lizard at 0,0 1,0 2,0"); // PASSED
        
        game2.move(0, 0, RIGHT); // Try moving the tail forwards into itself
        System.out.println(game2);
        System.out.println("Expected a lizard at 1,0 2,0 3,0"); // PASSED
    }

    private static void test5() {
        LizardGame game = new LizardGame(5, 3);
        Lizard liz = new Lizard();
        Cell cell0 = new Cell(1, 1);
        Cell cell1 = new Cell(2, 1);
        Cell cell2 = new Cell(3, 1);
        ArrayList<BodySegment> segments = new ArrayList<>();
        segments.add(new BodySegment(liz, cell0));
        segments.add(new BodySegment(liz, cell1));
        segments.add(new BodySegment(liz, cell2));
        liz.setSegments(segments);
        game.addLizard(liz);

        System.out.println(game);
        System.out.println("Expected a lizard at 1,1 2,1 3,1"); // PASSED

        game.move(2, 1, UP); // This move should be stopped, since it is not "in-line"
        System.out.println(game);
        System.out.println("Expected a lizard at 1,1 2,1 3,1"); // PASSED

        game.move(2, 1, DOWN); // This move should be stopped, since it is not "in-line"
        System.out.println(game);
        System.out.println("Expected a lizard at 1,1 2,1 3,1"); // PASSED

        game.move(2, 1, RIGHT); // Moving in the direction of the head
        System.out.println(game);
        System.out.println("Expected a lizard at 2,1 3,1 4,1"); // PASSED

        game.move(3, 1, LEFT); // Moving in the direction of the tail
        System.out.println(game);
        System.out.println("Expected a lizard at 1,1 2,1 3,1"); // PASSED

        game.move(2, 1, LEFT);
        game.move(1, 1, LEFT); // This move should be stopped, since it is out of bounds
        System.out.println(game);
        System.out.println("Expected a lizard at 0,1 1,1 2,1"); // PASSED

        game.move(0, 1, UP);
        game.move(0, 0, UP); // This move should be stopped, since it is out of bounds
        System.out.println(game);
        System.out.println("Expected a lizard at 0,0 0,1 1,1"); // PASSED

        game.move(1, 1, DOWN);
        game.move(1, 2, DOWN); // This move should be stopped, since it is out of bounds
        System.out.println(game);
        System.out.println("Expected a lizard at 0,1 1,1 1,2"); // PASSED

        game.move(1, 2, RIGHT);
        game.move(2, 2, RIGHT);
        game.move(3, 2, RIGHT);
        game.move(4, 2, RIGHT); // This move should be stopped, since it is out of bounds
        System.out.println(game);
        System.out.println("Expected a lizard at 2,2 3,2 4,2");
    }

    private static void test6() {
        LizardGame game = new LizardGame(5, 5);
        Lizard liz1 = new Lizard();
        Lizard liz2 = new Lizard();
        Cell cell0 = new Cell(1, 1);
        Cell cell1 = new Cell(2, 1);
        Cell cell2 = new Cell(3, 1);
        ArrayList<BodySegment> segments1 = new ArrayList<>();
        segments1.add(new BodySegment(liz1, cell0));
        segments1.add(new BodySegment(liz1, cell1));
        segments1.add(new BodySegment(liz1, cell2));
        liz1.setSegments(segments1);
        game.addLizard(liz1);

        Cell cell3 = new Cell(1, 3);
        Cell cell4 = new Cell(2, 3);
        Cell cell5 = new Cell(3, 3);
        ArrayList<BodySegment> segments2 = new ArrayList<>();
        segments2.add(new BodySegment(liz2, cell3));
        segments2.add(new BodySegment(liz2, cell4));
        segments2.add(new BodySegment(liz2, cell5));
        liz2.setSegments(segments2);
        game.addLizard(liz2);

        System.out.println(game);
        System.out.println("Expected a lizard at 1,1 2,1 3,1"); // PASSED
        System.out.println("Expected a lizard at 1,3 2,3 3,3"); // PASSED

        game.move(1, 1, LEFT);
        game.move(1, 3, LEFT);
        System.out.println(game);
        System.out.println("Expected a lizard at 0,1 1,1 2,1"); // PASSED
        System.out.println("Expected a lizard at 0,3 1,3 2,3"); // PASSED

        game.move(0, 1, DOWN);
        game.move(0, 3, UP); // This move should be stopped by the other lizard
        System.out.println(game);
        System.out.println("Expected a lizard at 0,2 0,1 1,1"); // PASSED
        System.out.println("Expected a lizard at 0,3 1,3 2,3"); // PASSED
    }

    private static void test7() {
        LizardGame game = new LizardGame(4, 4);
        Lizard liz = new Lizard();
        Cell cell0 = new Cell(0, 0);
        Cell cell1 = new Cell(1, 0);
        Cell cell2 = new Cell(2, 0);
        ArrayList<BodySegment> segments = new ArrayList<>();
        segments.add(new BodySegment(liz, cell0));
        segments.add(new BodySegment(liz, cell1));
        segments.add(new BodySegment(liz, cell2));
        liz.setSegments(segments);
        game.addLizard(liz);

        Exit exit = new Exit(game.getCell(3, 0));
        game.addExit(exit);

        GameConsole gc = new GameConsole();
        game.setListeners(gc, gc);

        System.out.println(game);
        game.move(2, 0, RIGHT);
        System.out.println("Expected a message saying the number of lizards is now 0."); // PASSED
        System.out.println("Expected a message saying that the game has been won."); // PASSED
    }
}