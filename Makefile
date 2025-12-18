ENV_NAME = ligo

NOTEBOOKS = \
	map_descriptive_analysis.ipynb \
	chart_descriptive_analysis.ipynb \
	kmeans_analysis.ipynb 

.PHONY: env all

env:
	@echo ">>> Creating conda environment: $(ENV_NAME)"
	conda env create -f environment.yml --name $(ENV_NAME) || \
	conda env update -f environment.yml --name $(ENV_NAME)
	@echo ">>> Done. Activate conda $(ENV_NAME)"

all:
	@echo ">>> Executing all notebooks..."
	jupyter nbconvert --to notebook --execute $(NOTEBOOKS) --inplace
	@echo ">>> All notebooks executed successfully."

