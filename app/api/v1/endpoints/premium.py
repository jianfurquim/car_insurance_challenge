from app.domain.models.car import Car
from app.domain.models.premium import PremiumDetails
from fastapi import APIRouter

from app.use_cases.calculate_premium import CalculatePremium
from app.domain.services.premium_calculator import PremiumCalculator

router = APIRouter()


@router.post("/calculate-premium", response_model=PremiumDetails)
def calculate_premium(car: Car):
    premium_calculator = PremiumCalculator()
    use_case = CalculatePremium(premium_calculator)
    return use_case.execute(car)
