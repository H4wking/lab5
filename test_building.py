import unittest
from classroom import Classroom
from building import AcademicBuilding


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
classroom_008 = Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]
building = AcademicBuilding('Kozelnytska st. 2a', classrooms)


class AcademicBuildingTest(unittest.TestCase):
    def test_total_equipment(self):
        self.assertEqual(AcademicBuilding.total_equipment(building), [('PC', 2), ('projector', 2), \
('mic', 1), ('TV', 1)])

    def test___str__(self):
        self.assertEqual(AcademicBuilding.__str__(building), "Kozelnytska st. 2a\n\
Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.\n\
Classroom 007 has a capacity of 12 persons and has the following equipment: TV.\n\
Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.\n")


if __name__ == "__main__":
    unittest.main()