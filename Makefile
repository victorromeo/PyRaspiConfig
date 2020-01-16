init:
	pip install -r requirements.txt

test:
	nose2 -v

doc:
	-rm -rf build/sphinx
	python3 setup.py build_sphinx
