from bmi_model import BmiModel

class BmiController:
    def get_conclusion(self, mass, height):
        bmi_model = BmiModel(mass, height)
        bmi = bmi_model.find_bmi()
        conclusion = bmi_model.find_conclusion(bmi)
        return f'Your bmi is {bmi}. You have {conclusion}'
