"""
Spectrum of Extracted DIA Data TEMPLATE
=======================================

This example shows a spectrum from extracted data. No binning is applied.
"""
import pandas as pd
import requests

pd.options.plotting.backend = 'TEMPLATE'

# # Download test file

url = 'https://raw.githubusercontent.com/Roestlab/massdash/dev/test/test_data/featureMap/ionMobilityTestFeatureDf.tsv'
file_name = 'ionMobilityTestFeatureDf.tsv'

# # Send a GET request to the URL
# # Send a GET request to the URL and handle potential errors
try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    
    # # Save the content of the response to a file
    with open(file_name, 'wb') as file:
        file.write(response.content)
except requests.RequestException as e:
    print(f"Error downloading file: {e}")
except IOError as e:
    print(f"Error writing file: {e}")



# # Code to add annotation to ionMobilityTestFeatureDf data
df = pd.read_csv("./ionMobilityTestFeatureDf.tsv", sep="\t")

df.plot(kind="spectrum", x="mz", y="int", custom_annotation='Annotation', annotate_mz=True, bin_method='none', annotate_top_n_peaks=5, aggregate_duplicates=True)


