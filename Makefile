define USAGE
swanChallenge Flask app

Commands:
	setup       Install Python dependencies
	run         Run app in dev environment
	clean       Clean pycache
endef

export USAGE
help:
	@echo "$$USAGE"

setup: requirements.txt
    pip install -r requirements.txt

run:
    python app.py

clean:
    rm -rf __pycache__