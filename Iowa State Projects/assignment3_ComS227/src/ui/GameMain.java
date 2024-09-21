package ui;

import java.awt.EventQueue;
import java.util.ArrayList;

import javax.swing.JFrame;

import hw3.LizardGame;
import hw3.Lizard;
import api.Cell;
import api.BodySegment;

public class GameMain extends JFrame {
	private static final long serialVersionUID = 1L;

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					GameMain frame = new GameMain();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	public GameMain() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 400, 400);
		
		LizardGame game = new LizardGame(10, 10);
		Lizard liz = new Lizard();
		Cell cell0 = new Cell(0, 0);
		Cell cell1 = new Cell(0, 1);
		Cell cell2 = new Cell(0, 2);
		
		ArrayList<BodySegment> segments = new ArrayList<>();
		segments.add(new BodySegment(liz, cell0));
		segments.add(new BodySegment(liz, cell1));
		segments.add(new BodySegment(liz, cell2));
		liz.setSegments(segments);
		game.addLizard(liz);
		
		
		GridViz playGrid = new GridViz(game);
		GamePanel gamePanel = new GamePanel(game);
		setContentPane(gamePanel);
	
		gamePanel.setPlayGrid(playGrid);
		game.setListeners(gamePanel, gamePanel);
	}
}
