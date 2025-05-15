# Calculator API

Welcome to our Calculator API project! This is a simple yet powerful calculator service that helps you perform basic math operations through API calls. We've built it with simplicity and best practices in mind.

## What Can This API Do?

Think of it as your pocket calculator, but accessible through the internet! You can:
- Add numbers together
- Subtract one number from another
- Multiply numbers
- Divide numbers (and yes, we handle division by zero gracefully!)

## Getting Started

### Running Locally
First, make sure you have Python 3.9 or newer installed. Then:

1. Clone this repository:
   ```bash
   git clone https://github.com/eligosleyak/Calculator-12FactorApp.git
   cd Calculator-12FactorApp
   ```

2. Set up your workspace:
   ```bash
   python -m venv .venv

   # For Windows users:
   .venv\Scripts\activate

   # For Mac or Linux users:
   source .venv/bin/activate
   ```

3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the API:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

### Using Docker
If you prefer using Docker, it's straightforward:
```bash
# Build the image
docker build -t calculator-api .

# Run the container
docker run -d -p 8000:8000 calculator-api
```

## Try It Out

Here are some examples to get you started:

```bash
# Say hello to the API
curl http://localhost:8000/
# Returns: {"message": "Welcome to the CalculatorAPI"}

# Add 5 and 3
curl http://localhost:8000/add/5/3
# Returns: {"result": 8}

# Multiply 6 and 7
curl http://localhost:8000/multiply/6/7
# Returns: {"result": 42}
```

## Running Tests

### Locally
```bash
pytest
```

### In Docker
```bash
# Run tests in a new container with verbose output
docker run calculator-api pytest -v
```

## How We Follow the 12-Factor App Methodology

We've built this application following the twelve-factor app methodology, which helps us create maintainable and scalable software. Here's how we implement each factor:

1. **Codebase**
   - Single codebase in version control
   - Same code goes everywhere

2. **Dependencies**
   - All dependencies are explicitly declared in requirements.txt
   - Virtual environment ensures isolation
   ```python
   # requirements.txt
   fastapi>=0.68.0,<0.69.0
   uvicorn>=0.15.0,<0.16.0
   ```

3. **Configuration**
   - Configuration is stored in the environment
   - No hard-coded config values in the code

4. **Backing Services**
   - Ready for external service attachment
   - Services can be swapped without code changes

5. **Build, Release, Run**
   - Build and run stages are separated in our Dockerfile
   ```dockerfile
   # Build stage
   FROM python:3.9-slim as build
   # Run stage
   FROM build as production
   ```

6. **Processes**
   - Application runs statelessly
   - Each request stands alone

7. **Port Binding**
   - Self-contained service on port 8000
   - No external web servers needed
   ```python
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

8. **Concurrency**
   - Scales through Docker containers
   - Each process is independent

9. **Disposability**
   - Quick startup and graceful shutdown
   - Containerized for easy replacement

10. **Development/Production Parity**
    - Same dependencies everywhere
    - Docker ensures consistent environments

11. **Logs**
    - All logs go to stdout
    - FastAPI handles request logging

12. **Admin Processes**
    - One-off admin tasks run in same environment
    - Uses same code and configuration

## Project Structure
```
calculator-api/
├── app/
│   └── main.py          # Core application logic
├── tests/
│   └── test_calculator.py  # Making sure everything works
├── Dockerfile           # Container configuration
├── requirements.txt     # Project dependencies
└── README.md           # You're reading this now
```
