[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sSkqmNLf)

# Final Project: Environmental Burden and Race

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group14/main)

## Repository Structure
- `data/`: Contains the raw CalEnviroScreen 4.0 shapefiles and `calenviroscreen40.csv`, a tabular version of the dataset with all non-geometric attributes
- `visualizations/`: Contains the generated figures and maps
- `analysis/`: Contains `chart_analysis.ipynb`, `map_analysis.ipynb`, and `kmeans_analysis.ipynb`
- `main.ipynb`: Overview notebook that combines results from the chart, map, and K-means analysis
- `CEStools/`: Contains utility functions and `tests/`
- `main.ipynb`: Main project notebook, providing an overview of the analysis and results 
- `environment.yml`: Environment file specifying the required packages for the project  
- `Makefile`: Makefile to automate environment setup and execution of analysis notebooks

## License

This project is licensed under the BSD 3-Clause License.

## Bibliography 

Our analysis uses the CalEnviroScreen 4.0 census tract shapefiles [@calenviroscreen40shp]. We also used the CalEnviroScreen 4.0 data dictionary to help interpret score components and variable definitions [@calenviroscreen40].