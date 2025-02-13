
# Car Insurance Challenge


## Features

- **Dynamic Rate Calculation**:
  - Adjusts the insurance rate based on the car's age and value.
  - For every year since the car was produced, add 0.5% to the rate.
  - For every $10,000 of the car’s value, add another 0.5% to the rate.

- **Premium Calculation**:
  - Calculates the base premium, deductible discount, and final premium.
  - Includes a broker's fee in the final premium.

- **Policy Limit Calculation**:
  - Determines the base policy limit and adjusts it based on the deductible percentage.

- **GIS Adjustment (Optional)**:
  - Integrates with a Geographic Information System (GIS) to adjust the rate based on the car's registration location (optional bonus feature).

- **Highly Configurable**:
  - All calculation parameters are configurable via environment variables or a configuration file.

---

## Technologies Used

- **Python 3.12**: Core programming language.
- **FastAPI**: Framework for building the RESTful API.
- **Pydantic**: Data validation and settings management.
- **Docker**: Containerization for easy deployment.
- **Docker Compose**: Orchestration for multi-container setups.
- **Pytest**: Testing framework for unit and integration tests.

---

## Getting Started

### Prerequisites

- **Docker**: Install Docker from [here](https://docs.docker.com/get-docker/).
- **Docker Compose**: Install Docker Compose from [here](https://docs.docker.com/compose/install/).
- **Python 3.12** (optional, for local development).

---