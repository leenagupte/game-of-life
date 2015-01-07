define green
	@tput setaf 2
	@tput bold
	@echo $1
	@tput sgr0
endef

.PHONY: default
default: unit_tests
	$(call green,"[Build successful]")


.PHONY: flake8
flake8:
	flake8 *.py unit_tests/*.py
	$(call green,"[Static analysis (flake8) successful]")

.PHONY: unit_tests
unit_tests:
	nosetests -q -v unit_tests/
	$(call green,"[Unit tests successful]")

