from datetime import datetime
from app.domain.models.car import Car
from app.domain.models.premium import PremiumDetails
from app.infrastructure.config.settings import settings


class PremiumCalculator:
    @staticmethod
    def calculate_rate(car: Car) -> float:
        current_year = datetime.now().year
        age = current_year - car.year
        rate_from_age = age * settings.base_rate
        rate_from_value = (car.value // 10000) * settings.value_rate
        total_rate = rate_from_age + rate_from_value
        return total_rate

    @staticmethod
    def calculate_premium(car: Car) -> PremiumDetails:
        rate = PremiumCalculator.calculate_rate(car)
        base_premium = car.value * rate
        deductible_discount = base_premium * car.deductible_percentage
        final_premium = base_premium - deductible_discount + car.broker_fee

        base_policy_limit = car.value * settings.coverage_percentage
        deductible_value = base_policy_limit * car.deductible_percentage
        final_policy_limit = base_policy_limit - deductible_value

        return PremiumDetails(
            applied_rate=rate,
            policy_limit=final_policy_limit,
            calculated_premium=final_premium,
            deductible_value=deductible_value,
        )
