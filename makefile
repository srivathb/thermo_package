black:
    black .
flake8:
    flake8 --exclude build .
pylint:
    pylint --ignore build .
test:
    pytest .
all: black flake8 pylint
