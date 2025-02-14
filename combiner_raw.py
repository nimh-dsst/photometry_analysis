import os
import pandas as pd


###Example### change this to the path where you have the exported csv's from browser / synapse
base_path = r"U:\NIMH DIRP NSI\Projects\SST Subpopulations\Photometry Data\Circuits\BLA Proj GCaMP SST KD\FDD4\1"

# Read data from each file in the folder
control = pd.read_csv(os.path.join(base_path, "405.csv"))
signal = pd.read_csv(os.path.join(base_path, "470.csv"))
time = pd.read_csv(os.path.join(base_path, "470.csv"))
ttl = pd.read_csv(os.path.join(base_path, "ttl.csv"))

# Find beginning and end indices
row = ttl[ttl["D0"] == 1].index

# Check if any rows were found
if len(row) == 0:
    print("No rows where ttl['D0'] == 1 were found.")
else:
    begin = row[0] - 1
    end = row[-1]

    # Subset data
    control_subset = control["D0"].iloc[begin:end]
    signal_subset = signal["D0"].iloc[begin:end]
    timestamp = time["TIME"].iloc[: len(control_subset)]

    # Combine data
    tdtdata = pd.DataFrame(
        {
            "TimeStamp": timestamp.values,
            "Signal": signal_subset.values,
            "Control": control_subset.values,
        }
    )

    # Write data to file
    output_file = os.path.join(base_path, "new_TDT.csv")
    tdtdata.to_csv(output_file, index=False)
