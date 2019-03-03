class Classroom():
    """Class for classroom representation."""
    def __init__(self, number, capacity, equipment):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self):
        """
        (Classroom) -> str
        :return: string representation of Classroom object.
        """
        return "Classroom {} has a capacity of {} \
persons and has the following equipment: {}.".format(self.number, self.capacity, ", ".join(self.equipment))

    def is_larger(classroom1, classroom2):
        """
        (Classroom, Classroom) -> bool
        :return: True if first classroom is larger, False otherwise.
        """
        return classroom1.capacity > classroom2.capacity

    def equipment_differences(classroom1, classroom2):
        """
        (Classroom, Classroom) -> list
        :return: difference in classrooms' equipment.
        """
        difference = []
        for i in classroom1.equipment:
            if i not in classroom2.equipment:
                difference.append(i)
        return difference

    def __repr__(self):
        """
        (Classroom) -> str
        :return: representation of Classroom object.
        """
        return "Classroom('{}', {}, {})".format(self.number, self.capacity, self.equipment)


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])

