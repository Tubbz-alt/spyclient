# Build package
all:
	python setup.py sdist bdist_wheel


# Install package locally
install:
	python setup.py install


# Uninstall package
uninstall:
	pip3 uninstall -y spyclient


# Develop package locally
develop:
	python setup.py develop


# Run tests
test:
	python test\test.py


# Remove build files
clean:
	rmdir /S /Q spyclient.egg-info
	rmdir /S /Q build
	rmdir /S /Q dist


.PHONY: all test clean
