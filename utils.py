# Functions file

import matplotlib.pyplot as plt

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
    plt.show()