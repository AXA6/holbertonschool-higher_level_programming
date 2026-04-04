def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Check empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check empty attendees
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):

        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        output = template
        output = output.replace("{name}", str(name))
        output = output.replace("{event_title}", str(event_title))
        output = output.replace("{event_date}", str(event_date))
        output = output.replace("{event_location}", str(event_location))

        filename = f"output_{i}.txt"

        with open(filename, "w") as file:
            file.write(output)
