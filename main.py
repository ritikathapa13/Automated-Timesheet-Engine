import sqlite3
from jinja2 import Environment, FileSystemLoader


def validate_hoursworked(hoursworked):
    if  hoursworked>24:
        raise ValueError("Humans cannot work more than 24 hours!")

def log_activity(func):
    def wrapper(self,*args,**kwargs):
        result=func(self,*args,**kwargs)
        print("New timesheet saved for[Name] ")
        return result
    return wrapper
    
    
class Timesheet:
   def __init__(self, employeename, date, hoursworked, projectcode):
      validate_hoursworked(hoursworked)
      self.employeename = employeename
      self.date=date
      self.hoursworked=hoursworked
      self.projectcode=projectcode 

   @log_activity
   def save(self):
         print("Saving to database")
         connection=sqlite3.connect('database.db')
         cursor=connection.cursor() 
         cursor.execute("CREATE TABLE IF NOT EXISTS TIMESHEET(employeename TEXT,date TEXT,hoursworked INTEGER,projectcode TEXT)")
         cursor.execute("INSERT INTO TIMESHEET (employeename,date,hoursworked,projectcode) VALUES(?,?,?,?)",(self.employeename, self.date, self.hoursworked, self.projectcode))
         connection.commit() 
         connection.close()
         print("Record saved successfully!")

def generate_report(employee_name):
    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    cursor.execute("SELECT date,hoursworked,projectcode FROM TIMESHEET WHERE employeename=?",(employee_name,)) 
    records=cursor.fetchall()
    conn.close() 

    env=Environment(loader=FileSystemLoader("."))
    template=env.get_template('report_template.html')
    output=template.render(name=employee_name, data=records)

    with open("report.html","w") as f:
        f.write(output)
    print("Report generated successfully!")  


if __name__ == "__main__":
      name = input("Enter employee name: ") 
      date = input("Enter date (DD/MM/YYYY): ")
      hours = int(input("Enter hours worked: ") )
      project = input("Enter project code: ").upper()   
      entry=Timesheet(name, date, hours, project)
      entry.save()
generate_report(name)










    


