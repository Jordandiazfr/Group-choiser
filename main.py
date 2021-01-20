from students import Students
import pathlib
import os
import logging
import json

logfile = pathlib.Path(f'{os.getcwd()}/logs.log')
logging.basicConfig(filename=logfile, format='%(asctime)s: %(levelname)s: %(message)s', level=logging.DEBUG,
                    datefmt='[%Y-%m-%d %H:%M:%S]')

# Create a new instance of student class
students = Students()

# Make groups of N students
groups = students.dispatch_students(3)

# Create a variable where we create a JSON objet
out = json.dumps(students.groups_json())

logging.debug('Object parsed into JSON ')

with open("groups.json", mode="w") as result:
    final_object = result.write(out)

    logging.debug('JSON outputted ')



