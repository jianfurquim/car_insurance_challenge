from pydantic import BaseModel


class Car(BaseModel):
    make: str
    model: str
    year: int
    value: float
    deductible_percentage: float
    broker_fee: float
    registration_location: str = None
