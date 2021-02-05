TESTS := $(wildcard test/test_*.py)

PYFILES := $(wildcard nfor/*.py)
doc: doc/source/conf.py doc/Makefile doc/source/*.rst $(PYFILES)
	cd doc
	make markdown

test: FORCE
	pytest --ignore=sandbox/ --cov=./ --cov-report=html --cov-config=.coveragerc | tee doc/source/_static/doc_test.txt

FORCE:

