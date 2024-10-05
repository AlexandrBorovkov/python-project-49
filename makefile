install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3.12 -m pip install dist/*.whl

package-reinstall:
	python3.12 -m pip install --force-reinstall dist/*.whl



