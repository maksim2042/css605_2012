package rpsworld;

import sim.engine.SimState;
import sim.field.grid.IntGrid2D;

public class RPSWorld extends SimState {

	/**
	 * @param args
	 */
	
	public int gridWidth = 100;
	public int gridHeight = 100;
	public IntGrid2D grid;
	public RPS_CA ca;
	
	public RPSWorld(long seed) {
		super(seed);
	}
	
	public void start() {
		super.start();
		grid = new IntGrid2D(gridWidth, gridHeight);
		setupGrid();
		ca = new RPS_CA();
		schedule.scheduleRepeating(ca);
	}
	
	public void setupGrid() {
		for(int x = 0; x<gridWidth;x++) {
			for(int y = 0; y < gridHeight; y++) {
				int type = random.nextInt(3);
				grid.field[x][y] = type;
			}
		}			
	}
	
	public static void main(String[] args) {
		RPSWorld model = new RPSWorld(System.currentTimeMillis());
		model.start();
	}
	
}
