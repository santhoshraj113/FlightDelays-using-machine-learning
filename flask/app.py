from flask import *
import time as time
import pickle

with open('flight.pkl', 'rb') as file:
    model = pickle.load(file)

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/result",methods=["POST"])
def result():
    number=int(request.form["fltnum"])
    month=int(request.form["month"])
    dayofmonth=int(request.form["dayofmonth"])
    dayofweek=int(request.form["dayofweek"])
    origin=request.form["origin"]
    if(origin=="atl"):
        origin=0
    elif(origin=="dtw"):
        origin=1
    elif(origin=="jfk"):
        origin=2
    elif(origin=="msp"):
       origin=3
    elif(origin=="sea"):
       origin=4
    destination=request.form["destination"]
    if(destination=="atl"):
        destination=0
    elif(destination=="dtw"):
        destination=1
    elif(destination=="jfk"):
        destination=2
    elif(destination=="msp"):
        destination=3
    elif(destination=="sea"):
        destination=4
    dept=int(request.form["dept"])
    arrdept=int(request.form["arrtime"])
    actdept=int(request.form["acttime"])
    dept15=int(dept)-int(actdept)
    print("working")
    total=[[number,month,dayofmonth,dayofweek,origin,destination,dept15,arrdept]]
    y_pred=model.predict(total)

    if(y_pred==[0.]):
        ans="THE FLIGHT WILL BE ON TIME"
        show=0
    else:
        ans="THE FLIGHT WILL BE DELAYED"
        show=1
    print(ans)
    return render_template("result.html",ans=ans,show=show)

if __name__=="__main__":
    app.run()