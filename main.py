import flask
import os
import random

app = flask.Flask(__name__)



@app.route('/') #python decorator
def index():
    musiclist = ["Chief Keef","SahBabii","Pop Smoke","Bizzy Banks","Sheff G"]
    musicpics = ["./static/chiefkeef.jpg", "./static/sahbabii.jpg", "./static/popsmoke.jpg", "./static/bizzybanks.jpg","./static/bizzybanks.jpg"]
  
    return flask.render_template(
        "index.html",
        # HTML variable = python variable 
        entirelist=musiclist,
        piclist=musicpics,
        listlen = len(musiclist)
       
    )


    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)