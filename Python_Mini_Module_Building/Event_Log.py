#This function takes an event object as an argument and returns its date attribute. It's used to sort events by date.
def get_event_date(event):
  return event.date

"""
Sort Events: The events are sorted by date using the get_event_date function.
Initialize machines Dictionary: An empty dictionary machines is created to store the users logged into each machine.
Process Each Event: The function iterates through each event:
    If the machine is not already in the dictionary, it adds the machine with an empty set of users.
    If the event type is "login", the user is added to the set of users for that machine.
    If the event type is "logout", the user is removed from the set of users for that machine.
Return machines: The function returns the dictionary containing the current users for each machine.

"""
def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].remove(event.user)
  return machines

"""
This function takes the machines dictionary as an argument.
    It iterates through each machine and its users:
    If there are users logged into the machine, it joins the users into a comma-separated string.
    It prints the machine name followed by the list of users."""
def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

"""
This class represents an event with attributes for the date, type, machine name, and user.
The __init__ method initializes these attributes when an Event object is created.
"""
class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

#A list of Event objects is created with specific dates, types, machine names, and users.
events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
  Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
  Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
  Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
  Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

"""
The current_users function is called with the list of events to get the current users for each machine.
The generate_report function is called with the resulting dictionary to print the report.
"""
users = current_users(events)
print(users)

generate_report(users)