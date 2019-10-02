SHELL = /bin/sh
clean:
	@echo "clean all pyc extension"
	rm -rf mykonos/core/*.pyc
	rm -rf mykonos/core/__pycache__
	rm -rf mykonos/*.pyc
	rm -rf mykonos/__pycache__
	rm -rf mykonos/keywords/*.pyc
	rm -rf *.pyc
	rm -rf __pycache__
	rm -rf test/__pycache__
