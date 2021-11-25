from app import app
from models.event_list import *
from models.event import Event
from flask import render_template, request

@app.route("/events")
def index():
    return render_template("index.html", title="events", event_list=event_list)

@app.route("/events", methods=["POST"])
def add_event():
    event_name = request.form["name_of_event"]
    event_date = request.form["date"]
    event_number_of_guests = request.form["number_of_guests"]
    event_location = request.form["room_location"]
    event_description = request.form["description"]
    event_recurring = True
    if "recurring" in request.form:
        event_recurring = True
    else:
        event_recurring = False
    new_event = Event(event_name, event_date, event_number_of_guests, event_location, event_description,event_recurring)
    add_new_event(new_event)
    return index()

@app.route("/events/delete/", methods=["POST"])
def delete_event():
    delete_old_event(request.form["deleted_event"])
    return index()
    
