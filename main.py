import numpy as np

# np.set_printoptions(1)

URL = "https://www.ncei.noaa.gov/pub/data/cdo/samples/GHCND_sample_csv.csv"

raw = np.loadtxt(URL, skiprows=1, usecols=[5, 6, 7, 8], delimiter=",")

week_one = raw[0:7, 5:]
dates = raw[:, 0]

print(dates)
