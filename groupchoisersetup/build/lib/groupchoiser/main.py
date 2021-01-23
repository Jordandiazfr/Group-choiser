#!/usr/bin/env python
from .students.students import Students
import json
import logging
import os
import pathlib

logfile = pathlib.Path(f'{os.getcwd()}/logs.log')
logging.basicConfig(filename=logfile, format='%(asctime)s: %(levelname)s: %(message)s', level=logging.DEBUG,
                    datefmt='[%Y-%m-%d %H:%M:%S]')

def main():
    # Create a new instance of student class
    students = Students()

    # Make groups of N students
    try:
        x = int(input("How many students per group?"))
    except ValueError:
        print("Please insert a number from 0 to %d" % students.len)
        return main()
    groups = students.dispatch_students(x)

    # Create a variable where we create a JSON objet
    students.groups_json()
    x = students.group
    print(x)
    out = json.dumps(x)

    logging.debug('Object parsed into JSON ')

    with open("groups.json", mode="w") as result:
        final_object = result.write(out)

        logging.debug('JSON outputted ')


if __name__ == '__main__':
    main()

