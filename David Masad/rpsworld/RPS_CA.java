package rpsworld;

import sim.engine.SimState;
import sim.engine.Steppable;
import sim.field.grid.IntGrid2D;
import sim.util.Int2D;

public class RPS_CA implements Steppable {
	public IntGrid2D grid;
	
	public int resolution[][] = new int[3][3];
	
	
	public RPS_CA() {
		setup();
	}
	
	/**
	 * Set up the resolution array:
	 * 1 beats 0
	 * 2 beats 1
	 * 0 beats 2
	 */
	public void setup() {
		resolution[0][0] = 0;
		resolution[1][0] = 1;
		resolution[2][0] = 0;
		resolution[0][1] = 1;
		resolution[1][1] = 1;
		resolution[2][1] = 2;
		resolution[0][2] = 0;
		resolution[1][2] = 2;
		resolution[2][2] = 2;
	}
	
	public void step(SimState state) {
		RPSWorld rps_state = (RPSWorld)state;
		
		grid = rps_state.grid;
		int width = grid.getWidth();
		int height = grid.getHeight();
		int dx, dy;
		
		// Pick a cell and a neighbor at random:
		//int x = rps_state.random.nextInt(width);
		//int y = rps_state.random.nextInt(height);
		for(int x=0;x<grid.getWidth();x++) {
			for (int y=0;y<grid.getHeight();y++) {
				dx = rps_state.random.nextInt(3) - 1;
				dy = rps_state.random.nextInt(3) - 1;
				int x2 = grid.tx(x + dx);
				int y2 = grid.ty(y + dy);
				
				
				// Resolve cell outcomes:
				int a = grid.field[x][y];
				int b = grid.field[x2][y2];
				Int2D new_cells = resolve(a,b);
				grid.field[x][y] = new_cells.x;
				grid.field[x2][y2] = new_cells.y;
			}
		}
	}
	
	public Int2D resolve(int a, int b) {
		int new_a, new_b;
		new_a = resolution[a][b];
		new_b = resolution[b][a];
		return new Int2D(new_a, new_b);
		
	}
	
}
