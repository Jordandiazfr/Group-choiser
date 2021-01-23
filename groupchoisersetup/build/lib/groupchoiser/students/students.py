#!/usr/bin/env python
import random

with open('groupchoiser/eleves.txt') as x:
    names_list = x.read().split()


# is the name marked
def is_name_marked(student_name):
    return student_name[-1:] == "+"


def is_group_marked(group):
    for name in group:
        if is_name_marked(name):
            return True
    return False


class Students:
    """ The object students manipulates a list of students and helps forming groups of students
     being able of creating group taking in consideration  marked studens +  , or not !

     Marked stutents with plus '+' should not be paired with another marked students, unless the maximum
     number allowed is different than one.
      """
    def __init__(self):
        self.members = names_list
        self.len = len(names_list)
        self.all_groups = []
        self.group = {}

    # does the group contain a marked student?
    def dispatch_students(self, max_number_per_group):
        # iterate over the self.names_list
        remaining_students = list(self.members)
        # shuffle the list to avoid the same results at each run
        random.shuffle(remaining_students)
        # start a new group
        current_group = []
        # let<s take turns until no one remains.. someone may not be part of a group and alone but nobody likes him anyways
        while len(remaining_students) > 0:
            # take the first student from the list
            current_student = remaining_students.pop(0)
            if is_name_marked(current_student) and is_group_marked(current_group):
                # cant do anything : push if back at the end of the list
                remaining_students.append(current_student)
            else:
                if len(current_group) >= max_number_per_group:
                    # once we reach enought students, we close the group and create a new one
                    self.all_groups.append(current_group)
                    current_group = []
                # add the student to the current group
                current_group.append(current_student)
        # end while
        self.all_groups.append(current_group)
        return self.all_groups

    def groups_json(self):
        i = 1
        for groups in self.all_groups:
            self.group['Group#' + str(i)] = groups
            i += 1
