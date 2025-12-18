ENV_NAME = CES

NOTEBOOKS = \
	analysis/map_analysis.ipynb \
	analysis/chart_analysis.ipynb \
	analysis/kmeans_analysis.ipynb 

.PHONY: env all test

env:
	@echo ">>> Creating conda environment: $(ENV_NAME)"
	conda env create -f environment.yml --name $(ENV_NAME) || \
	conda env update -f environment.yml --name $(ENV_NAME)
	@echo ">>> Done. Activate conda $(ENV_NAME)"

all:
	@echo ">>> Executing all notebooks..."
	jupyter nbconvert --to notebook --execute $(NOTEBOOKS) --inplace
	@echo ">>> All notebooks executed successfully."

test:
	@echo ">>> Running all tests..."
	PYTHONPATH=. pytest
	@echo ">>> All tests passed successfully."
