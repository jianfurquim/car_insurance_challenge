from pydantic import BaseModel


class PremiumDetails(BaseModel):
    applied_rate: float
    policy_limit: float
    calculated_premium: float
    deductible_value: float
