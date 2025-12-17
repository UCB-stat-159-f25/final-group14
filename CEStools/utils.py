# Functions file

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def qmap(shape, col, title=None, cmap="viridis", k=6, figsize=(10,10), save=None, bins=None):
    """
    Create a choropleth map from a GeoDataFrame using either quantile-based
    classification or user-defined bins.

    This function plots a geographic variable from a GeoDataFrame and optionally
    saves the resulting figure to disk. If `bins` is not provided, the data are
    classified into quantiles. If `bins` is provided, a fixed bin classification
    is used, allowing for consistent legends across multiple maps.

    Parameters
    ----------
    shape : geopandas.GeoDataFrame
        GeoDataFrame containing geometry and the variable to be mapped.
    col : str
        Name of the column in `shape` to visualize.
    title : str, optional
        Title of the map. If None, the column name is used.
    cmap : str, default "viridis"
        Matplotlib colormap used for the choropleth.
    k : int, default 6
        Number of quantiles to use when `bins` is None.
    figsize : tuple of int, default (10, 10)
        Size of the figure in inches (width, height).
    save : str or None, default None
        File path to save the figure. If None, the figure is not saved.
    bins : list or array-like, optional
        User-defined bin edges for classification. If provided, overrides
        quantile-based classification.

    Returns
    -------
    None
        The function displays the map and optionally saves it to disk, but does
        not return any objects.
    """

    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.set_axis_off()

    if bins is None:
        # quantiles (different per race variable)
        shape.plot(
            column=col, scheme="quantiles", k=k, cmap=cmap, legend=True, ax=ax,
            edgecolor="white", linewidth=0.08,
            missing_kwds={"color": "lightgrey", "label": "Missing"},
            legend_kwds={"loc": "lower left"}
        )
    else:
        # fixed bins (same legend across variables)
        shape.plot(
            column=col, scheme="user_defined", classification_kwds={"bins": bins},
            cmap=cmap, legend=True, ax=ax,
            edgecolor="white", linewidth=0.08,
            missing_kwds={"color": "lightgrey", "label": "Missing"},
            legend_kwds={"loc": "lower left"}
        )

    ax.set_title(title if title else col, fontsize=14)

    if save:
        plt.savefig(save, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)

    plt.show()

def clean_data(raw_data, keep_geom = False):
    """
    Clean and prepare CalEnviroScreen data for analysis.
    Replace values with NaN, select only percentile columns, race columns,
    and geometry (if keep_geom=True).
    Make sure all values in the dataset are numeric.
    Parameters
    ----------
    raw_data : pandas.DataFrame OR geopandas.GeoDataframe
        Raw CalEnviroScreen data containing percentile and race columns.
    keep_geom : boolean
        Indicates whether the geometry column in a GeoDataframe should be kept
    Returns
    -------
    pandas.DataFrame OR geopandas.GeoDataframe (if keep_geom=True)
        Cleaned data with only necessary columns, invalid values replaced by NaN and
        selected columns coerced to numeric.
    """
    raw_data = raw_data.replace([-999, -1998], np.nan)

    pctl_cols = ['CIscoreP', 'OzoneP',  'PM2_5_P', 'DieselPM_P', 'PesticideP',
                 'Tox_Rel_P', 'TrafficP', 'DrinkWatP', 'Lead_P', 'CleanupP',
                 'GWThreatP', 'HazWasteP', 'ImpWatBodP', 'SolWasteP', 'PolBurdP',
                 'AsthmaP', 'LowBirWP', 'CardiovasP', 'EducatP', 'Ling_IsolP',
                 'PovertyP', 'UnemplP', 'HousBurdP', 'PopCharP']

    race_cols = ['Hispanic', 'White', 'AfricanAm', 'NativeAm', 'OtherMult', 'AAPI']

    required = set(pctl_cols + race_cols)
    missing = required - set(raw_data.columns)
    if missing:
        raise KeyError(f"Missing required columns: {sorted(missing)}")

    for c in (pctl_cols + race_cols):
        if c in raw_data.columns:
            raw_data[c] = pd.to_numeric(raw_data[c], errors="coerce")

    if keep_geom:
        clean = raw_data[pctl_cols + race_cols + ["geometry"]]
    else:
        clean = raw_data[pctl_cols + race_cols]

    return clean