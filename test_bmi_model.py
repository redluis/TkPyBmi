import unittest

from bmi_model import BmiModel

class TestBmiModel(unittest.TestCase):
    def setUp(self):
        self.bmiModel = BmiModel(65, 180)

    def test_find_bmi(self):
        self.assertEqual(
            self.bmiModel.find_bmi(),
            20.1
        )

    def test_find_conclusion(self):
        self.assertEqual(
            self.bmiModel.find_conclusion(18.2),
            'underweight'
        )

        self.assertEqual(
            self.bmiModel.find_conclusion(18.5),
            'normal weight'
        )

        self.assertEqual(
            self.bmiModel.find_conclusion(24),
            'normal weight'
        )

        self.assertEqual(
            self.bmiModel.find_conclusion(25),
            'overweight'
        )
        
        self.assertEqual(
            self.bmiModel.find_conclusion(29.8),
            'overweight'
        )

        self.assertEqual(
            self.bmiModel.find_conclusion(30),
            'obesity'
        )

        self.assertEqual(
            self.bmiModel.find_conclusion(69),
            'obesity'
        )

if __name__ == "__main__":
    unittest.main()
