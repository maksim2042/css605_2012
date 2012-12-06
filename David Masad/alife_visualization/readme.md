Web-based visualization
=======================


Uses a Python Tornado server and [d3.js](http://d3js.org/) to visualize the ALife model. 

Needs [Tornado](http://www.tornadoweb.org/) installed to run.

###To run: 
1. Go into the directory and run 

    python clock_server.py

2.  Open a browser (Chrome or Safari, probably Firefox, almost certainly not IE) and navigate to: [http://127.0.0.1:8888/static/alifeviz.html]

To add agents, just open **clock_server.py** and edit the *launch_model()* function to create additional agents and add them into the *MODEL* object.

The server runs another tick of the model every 0.5 seconds.