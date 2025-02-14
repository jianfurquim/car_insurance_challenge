from app.domain.services.premium_calculator import PremiumCalculator
from app.domain.models.premium import PremiumDetails
from app.domain.models.car import Car


class CalculatePremium:
    def __init__(self, premium_calculator: PremiumCalculator):
        self.premium_calculator = premium_calculator

    def execute(self, car: Car) -> PremiumDetails:
        return self.premium_calculator.calculate_premium(car)
