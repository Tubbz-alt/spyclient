# Build package
all:
	python setup.py sdist bdist_wheel


# Install package locally
install:
	python setup.py install


# Uninstall package
uninstall:
	pip uninstall -y spyclient


# Develop package locally
develop:
	python setup.py develop


# Remove build files
clean:
	rmdir /S /Q spyclient.egg-info
	rmdir /S /Q build
	rmdir /S /Q dist
