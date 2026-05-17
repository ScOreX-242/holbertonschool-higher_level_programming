from task_00_intro import generate_invitations

with open('template.txt') as f:
    template = f.read()

guests = [
    {
        "name": "John",
        "event_title": "Tech Meetup",
        "event_date": "2023-09-10",
        "event_location": "Berlin"
    },
    {
        "name": "Emma",
        "event_title": "Web Dev Workshop",
        "event_date": "2023-10-05",
        "event_location": "London"
    },
    {
        "name": "Liam",
        "event_title": "Startup Pitch",
        "event_date": None,
        "event_location": "Amsterdam"
    }
]

generate_invitations(template, guests)
