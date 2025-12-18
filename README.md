[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sSkqmNLf)

# Final Project: Environmental Burden and Race

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group14/main)

## Repository Structure
- `data/`: Contains the raw CalEnviroScreen 4.0 shapefiles and `calenviroscreen40.csv`, a tabular version of the dataset with all non-geometric attributes
- `visualizations/`: Contains the generated figures and maps
- `analysis/`: Contains `chart_analysis.ipynb`, `map_analysis.ipynb`, and `kmeans_analysis.ipynb`
- `main.ipynb`: Overview notebook that combines results from the chart, map, and K-me[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sSkqmNLf)

# Final Project: Environmental Burden and Race

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group14/main)

This project uses the CalEnviroScreen 4.0 dataset to analyze the relationships between environmental pollution indicators, socioeconomic vulnerability measures, and racial composition. Geographic data are used to visualize these variables on maps, and K-means clustering is applied to group census tracts with similar environmental and socioeconomic profiles.

## Repository Structure
- `data/`: Contains the raw CalEnviroScreen 4.0 shapefiles and `calenviroscreen40.csv`, a tabular version of the dataset with all non-geometric attributes
- `visualizations/`: Contains the generated figures and maps
- `analysis/`: Contains `chart_analysis.ipynb`, `map_analysis.ipynb`, and `kmeans_analysis.ipynb`
- `main.ipynb`: Overview notebook that combines results from the chart, map, and K-means analysis
- `CEStools/`: Contains utility functions and `tests/`
- `main.ipynb`: Main project notebook, providing an overview of the analysis and results 
- `environment.yml`: Environment file specifying the required packages for the project  
- `Makefile`: Makefile to automate environment setup and execution of analysis notebooks
- `pdf_builds/`: Contains pdf versions of each notebook

## Usage

1. Clone this repository:
```bash
git clone https://github.com/UCB-stat-159-f25/final-group14.git
cd final-group14
```

2. Create and activate the environment:
```bash
make env
```

3. Execute all notebooks:
```bash
make all
```

4. Run tests:
```bash
make test
```

## License

This project is licensed under the BSD 3-Clause License.

## Bibliography 

Our analysis uses the CalEnviroScreen 4.0 census tract shapefiles [@calenviroscreen40shp]. We also used the CalEnviroScreen 4.0 data dictionary to help interpret score components and variable definitions [@calenviroscreen40].
ans analysis
- `CEStools/`: Contains utility functions and `tests/`
- `main.ipynb`: Main project notebook, providing an overview of the analysis and results 
- `environment.yml`: Environment file specifying the required packages for the project  
- `Makefile`: Makefile to automate environment setup and execution of analysis notebooks
