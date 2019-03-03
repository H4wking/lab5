import unittest
from classroom import Classroom


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])


class ClassroomTest(unittest.TestCase):
    def test_is_larger(self):
        self.assertEqual(Classroom.is_larger(classroom_016, classroom_007), True)

    def test_equipment_differences(self):
        self.assertEqual(Classroom.equipment_differences(classroom_016, classroom_007), ['PC', 'projector', 'mic'])

    def test___str__(self):
        self.assertEqual(Classroom.__str__(classroom_016), "Classroom 016 has a capacity of 80 persons and has the \
following equipment: PC, projector, mic.")

    def test___repr__(self):
        self.assertEqual(Classroom.__repr__(classroom_016), "Classroom('016', 80, ['PC', 'projector', 'mic'])")


if __name__ == "__main__":
    unittest.main()