import random

with open("eleves.txt") as x:
    names_list = x.read().split()


class Students:
    """ The object students manipulates a list of students and helps forming groups of students
     being able of creating group taking in consideration  marked studens +  , or not !

     Marked stutents with plus '+' should not be paired with another marked students, unless the maximum
     number allowed is different than one.

      ---------- Attributtes -------

      .members = a list of names from eleves.txt
      .names = a clone list from members who is gonna be manipulated for the methods
      .len = the number of members in eleves.txt
      .max_marked_members =  The maximum number of marked members allowed in the same group, default 1.
      .group = the final group distribution

      ----------- Methods ----------

      """

    def __init__(self):
        self.members = names_list
        self.names = self.members
        self.len = len(names_list)
        self.max_marked_members = 1
        self.sub_group = []
        self.group = {}


    def is_marked(self, member) -> bool:
        """Determine if a student has the + mark so it cannot be paired with others with the same mark"""
        index = self.members.index(member)
        if self.members[index][-1:] == "+":
            return True
        return False

    def num_of_marked(self):
        marked = 0
        for names in self.members:
            if self.is_marked(names):
                marked += 1
        return marked

    def delete(self, name):
        """Deletes a selected student from the selection list (a cloned list) """
        self.names.remove(name)

    # TO FIXXXXX START #

    def make_sub_group_marked(self, num_of_members) -> list:
# Input make a group of 2 persons
        """Makes a little group with conforming the num_of_members input and taking in consideration the + mark"""
        marked = 0
        marked_sub_group = []
        # Get the total number of marked people:
        total_marked = self.num_of_marked()  #1
        for i in range(20):
            # Until we dont have two members
            selection = random.choice(self.names)
            print(selection)
            if self.is_marked(selection) and marked < 1:
                marked_sub_group.append(selection)
                self.delete(selection)
                marked += 1
            if marked > 0:
                marked_sub_group.append(selection)
            if len(marked_sub_group) == num_of_members:
                break
# Expected  output, marked person with one unmarked
        return marked_sub_group

    # TO FIXXXXX  END #

    def make_group_marked(self, number_of_members):
        """ Make the final group of students supposing there is at least one marked """
        number_of_groups = self.len // number_of_members
        for i in range(1, number_of_groups):
            self.group['Group #'+str(i)] = self.make_sub_group_marked(number_of_members)
        return self.group

    def make_group_not_marked(self, number_of_members):
        """ Make the group of students when there is not marked students """
        n_of_group = 1
        while self.names:
            for _ in range(number_of_members):
                if not self.names:
                    break
                picked = random.choice(self.names)
                self.sub_group.append(picked)
                self.delete(picked)
            self.group['Group #' + str(n_of_group)] = self.sub_group
            self.sub_group = []
            n_of_group += 1
        return self.group


    def make_groups(self, number_of_members):
        """ This is the final group creator, it will detect if the group has a marked member or not and call
        the right method """
        marked = self.num_of_marked()
        if marked == 0:
            total = self.make_group_not_marked(number_of_members)
        if marked > 0:
            total = self.make_group_marked(number_of_members)
        return total

