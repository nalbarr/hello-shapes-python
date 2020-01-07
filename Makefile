all: test

test:
	python -m unittest -v tests.test_foo
	python -m unittest -v tests.test_hello_shapes
