# Functions file

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def qmap(shape, col, title=None, cmap="viridis", k=6, figsize=(10,10), save=None, bins=None):
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

def clean_data(raw_data):
    raw_data = raw_data.replace([-999, -1998], np.nan)

    pctl_cols = ['CIscoreP', 'OzoneP',  'PM2_5_P', 'DieselPM_P', 'PesticideP',
                 'Tox_Rel_P', 'TrafficP', 'DrinkWatP', 'Lead_P', 'CleanupP',
                 'GWThreatP', 'HazWasteP', 'ImpWatBodP', 'SolWasteP', 'PolBurdP',
                 'AsthmaP', 'LowBirWP', 'CardiovasP', 'EducatP', 'Ling_IsolP',
                 'PovertyP', 'UnemplP', 'HousBurdP', 'PopCharP']

    race_cols = ['Hispanic', 'White', 'AfricanAm', 'NativeAm', 'OtherMult', 'AAPI']

    for c in (pctl_cols + race_cols):
        if c in raw_data.columns:
            raw_data[c] = pd.to_numeric(raw_data[c], errors="coerce")

    clean = raw_data[pctl_cols + race_cols]

    return clean