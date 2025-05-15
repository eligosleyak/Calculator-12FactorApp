# Calculator API

A FastAPI-based Calculator API that provides basic arithmetic operations through RESTful endpoints. This project demonstrates a simple yet robust implementation of a microservice using modern Python web frameworks and Docker containerization.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- RESTful API endpoints
- Docker support
- Comprehensive test suite

## API Endpoints

- `GET /` - Welcome message
- `GET /add/{a}/{b}` - Add two numbers
- `GET /subtract/{a}/{b}` - Subtract second number from first
- `GET /multiply/{a}/{b}` - Multiply two numbers
- `GET /divide/{a}/{b}` - Divide first number by second (with zero division protection)

## Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized deployment)
- Git

## Local Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd calculator-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On Unix or MacOS
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

The API will be available at `http://localhost:8000`

## Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t calculator-api .
   ```

2. Run the container:
   ```bash
   docker run -d -p 8000:8000 calculator-api
   ```

The API will be available at `http://localhost:8000`

## Testing

Run the test suite using pytest:
```bash
pytest
```

## API Usage Examples

### Add Numbers
```bash
curl http://localhost:8000/add/5/3
# Response: {"result": 8}
```

### Subtract Numbers
```bash
curl http://localhost:8000/subtract/10/4
# Response: {"result": 6}
```

### Multiply Numbers
```bash
curl http://localhost:8000/multiply/6/7
# Response: {"result": 42}
```

### Divide Numbers
```bash
curl http://localhost:8000/divide/20/5
# Response: {"result": 4.0}
```

## Project Structure

```
calculator-api/
├── app/
│   └── main.py          # Main application file with API endpoints
├── tests/
│   └── test_calculator.py  # Test suite
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
├── conftest.py         # Pytest configuration
└── README.md           # Project documentation
```

## Dependencies

- FastAPI (>= 0.68.0, < 0.69.0) - Web framework
- Uvicorn (>= 0.15.0, < 0.16.0) - ASGI server
- Pytest (>= 6.2.4, < 6.3.0) - Testing framework
- HTTPX (>= 0.18.2, < 0.19.0) - HTTP client for testing
- Requests (>= 2.28.0) - HTTP library for testing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Notes

- The API uses integer inputs for all operations
- Division by zero is handled with an appropriate error response
- All endpoints return JSON responses
- The Docker container runs on port 8000 by default
