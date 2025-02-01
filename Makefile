# craete virtial env to work with
.venv:
	python3 -m venv .venv &> /dev/null

# installs requirements for running installation
.PHONY: install-requirements
install-requirements: .venv
	.venv/bin/pip install -r requirements.txt &> /dev/null

# installs dev requirements for running installation
.PHONY: install-dev-requirements
install-dev-requirements: .venv
	.venv/bin/pip install -r requirements-dev.txt

# installs dependencies using pyinfra
.PHONY: install
install: install-requirements
	.venv/bin/pyinfra inventory.py set_up_mac.py -v
