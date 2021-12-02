class BmiModel:
    def __init__(self, mass, height):
        if mass <= 0: 
            raise Exception('[Error] Incorrect mass value (<= 0)')
        if height <= 0: 
            raise Exception('[Error] Incorrect height value (<= 0)')
        self.mass = mass
        self.height = height / 100

    def find_bmi(self):
        return round(
            self.mass / (self.height ** 2), 1
        )

    def find_conclusion(self, bmi):
        if bmi < 18.5: 
            return 'underweight'
        if 18.5 <= bmi < 25: 
            return 'normal weight'
        if 25 <= bmi < 29.9: 
            return 'overweight'
        if bmi >= 30: 
            return 'obesity'
