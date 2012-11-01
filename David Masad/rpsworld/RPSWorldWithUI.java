package rpsworld;

import java.awt.Color;

import javax.swing.JFrame;

import sim.display.Console;
import sim.display.Controller;
import sim.display.Display2D;
import sim.display.GUIState;
import sim.portrayal.grid.FastValueGridPortrayal2D;
import sim.util.gui.SimpleColorMap;

public class RPSWorldWithUI extends GUIState {
	JFrame displayFrame;
	Display2D display;
	FastValueGridPortrayal2D gridPortrayal = new FastValueGridPortrayal2D();
	
	public RPSWorldWithUI() {
		super(new RPSWorld(System.currentTimeMillis()));
	}
	
	public void start() {
		super.start();
		setupPortrayals();
		display.reset();
	}
	
	public void setupPortrayals() {
		gridPortrayal.setField(((RPSWorld)state).grid);
		SimpleColorMap colormap = new SimpleColorMap(
				new Color[] {Color.blue, Color.red, Color.green});
		gridPortrayal.setMap(colormap);
	}
	
	public void init(Controller c) {
		super.init(c);
		
		RPSWorld world = (RPSWorld)state;
		display = new Display2D(400, 400, this);
		displayFrame = display.createFrame();
		c.registerFrame(displayFrame);
		display.attach(gridPortrayal, "Cells");
		displayFrame.setVisible(true);
	}

	
	public static void main(String[] args) {
		RPSWorldWithUI model = new RPSWorldWithUI();
		Console c = new Console(model);
		c.setVisible(true);
	}
}
