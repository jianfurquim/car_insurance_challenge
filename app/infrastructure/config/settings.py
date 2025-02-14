from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Car Insurance Premium"
    base_rate: float = 0.005  # 0.5%
    value_rate: float = 0.005  # 0.5% per $10,000
    coverage_percentage: float = 1.0  # 100%
    gis_rate_variation: float = 0.02  # ±2%

    class Config:
        env_file = ".env"


settings = Settings()
