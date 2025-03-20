clear

echo "Formatting..."
black simple_math/

echo "Linting..."
pylint simple_math/

echo "Testing..."
pytest tests/ --cov=simple_math/