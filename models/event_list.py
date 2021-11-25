from models.event import Event

event_1 = Event("Julia's Wedding","2021-11-23", 57, "room_5", "wedding", False)
event_2 = Event("COP31", "2026-07-10",5000, "room_3", "conference", True)

event_list = [event_1,event_2]

def add_new_event(event):
    event_list.append(event)

def delete_old_event(event_name):
    event_to_delete = None
    for event in event_list:
        if event_name == event.name_of_event:
            event_to_delete = event
            break
    if event_to_delete:
        event_list.remove(event_to_delete)
    else: 
        return "Not found..."
