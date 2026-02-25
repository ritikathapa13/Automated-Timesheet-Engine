# Automated Timesheet Engine
A simple backend system that stores employee work records in a SQLite database and generates an HTML report.
## PROJECT OVERVIEW
This project allows user to:
- Save employee details in a database.
- Check working hours using a validator function.(If working hours > 24.It will generate ValueError:"Humans can't work more than 24 hours").
- Automatically log activity when saving data that prints"New timesheet saved for[Name]"
- Generate an HTML report using Jinja2.
- Converts project codes to uppercase using JavaScript.
## Languages Used:
  - Python for creating Timesheet class.
  - SQLite3 for saving data into database.
  - Jinja2 for creating HTML template.
  - HTML for creating employee report and a employee form(frontend).
  - JavaScript for converting project codes to UpperCase.
## How to Run the Project:
  - Run the python script(python main.py).
  - This will Create the database,Insert employee records and generate an HTML report.
  - Now,Open the generated report(report.html).
  - The generated report displays.
