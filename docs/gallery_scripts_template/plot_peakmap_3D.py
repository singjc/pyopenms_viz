"""
Extracted PeakMap 3D TEMPLATE
==================================

This shows a peakmap across m/z and retention time, plotted in 3D.
"""

import pandas as pd
from io import StringIO
import requests

pd.options.plotting.backend = "TEMPLATE"

# download the file for example plotting
url = "https://github.com/OpenMS/pyopenms_viz/releases/download/v0.1.5/ionMobilityTestFeatureDf.tsv"
response = requests.get(url)
response.raise_for_status()  # Check for any HTTP errors
df = pd.read_csv(StringIO(response.text), sep="\t")

# Code to plot a peakmap
df.plot(kind="peakmap", x="rt", y="mz", z="int", aggregate_duplicates=True, plot_3d=True)