from CEStools.utils import qmap
from CEStools.utils import clean_data
import pytest
import pandas as pd
import os
import geopandas as gpd
from shapely import Point

def test_clean_data_cols_exist():
	df = pd.DataFrame({
		"CIscoreP": [10, 20],
		"White": [50, 60],
	})
	
	with pytest.raises(KeyError, match="Missing required columns"):
		clean_data(df)


def test_clean_data_no_geom():
	pctl_cols = ['CIscoreP', 'OzoneP', 'PM2_5_P', 'DieselPM_P', 'PesticideP',
				 'Tox_Rel_P', 'TrafficP', 'DrinkWatP', 'Lead_P', 'CleanupP',
				 'GWThreatP', 'HazWasteP', 'ImpWatBodP', 'SolWasteP', 'PolBurdP',
				 'AsthmaP', 'LowBirWP', 'CardiovasP', 'EducatP', 'Ling_IsolP',
				 'PovertyP', 'UnemplP', 'HousBurdP', 'PopCharP']

	race_cols = ['Hispanic', 'White', 'AfricanAm', 'NativeAm', 'OtherMult', 'AAPI']

	data = {c: [1, 2] for c in pctl_cols + race_cols}
	data["geometry"] = [Point(0, 0), Point(1, 1)]

	gdf = gpd.GeoDataFrame(data, geometry="geometry")

	out = clean_data(gdf, keep_geom=True)

	assert "geometry" in out.columns


def test_qmap_runs():
    gdf = gpd.GeoDataFrame(
        {"value": [1, 2, 3]},
        geometry=[Point(0, 0), Point(1, 1), Point(2, 2)]
    )
    
    qmap(gdf, col="value")

def test_qmap_saves_file(tmp_path):
    gdf = gpd.GeoDataFrame(
        {"value": [1, 2, 3]},
        geometry=[Point(0, 0), Point(1, 1), Point(2, 2)]
    )

    output_path = tmp_path / "test_map.png"

    qmap(
        gdf,
        col="value",
        bins=[1, 2, 3],
        save=str(output_path)
    )

    assert output_path.exists()
