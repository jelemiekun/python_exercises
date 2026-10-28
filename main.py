import numpy as np

list_a: list[str] = [
    "a",
    "b",
    "r",
    "d",
]

np_list_a = np.array(list_a)

print(np_list_a)

fr_np_to_ls = np_list_a.tolist()

print(type(fr_np_to_ls))

np.set_printoptions(3)

URL = "https://www.ncei.noaa.gov/pub/data/cdo/samples/GHCND_sample_csv.csv"

raw = np.loadtxt(URL, skiprows=1, usecols=[6, 7, 8], delimiter=",")

week_one = raw[0:7, 5:]

print(raw)
