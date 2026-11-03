import numpy as np

URL = "https://www.ncei.noaa.gov/pub/data/cdo/samples/GHCND_sample_csv.csv/"

np.set_printoptions(suppress=True)

raw = np.loadtxt(URL, delimiter=",", skiprows=1, usecols=[5, 6, 7, 8])

arr_1 = np.array([1, 3, 5])
arr_2 = np.array([2, 4, 6])

print(arr_1 + arr_2)


def normalize(np_arr) -> None:
    np_arr_range = np.max(np_arr) - np.min(np_arr)
    np_arr_min = np.min(np_arr)
    new_arr = (np_arr - np_arr_min) / (np_arr_range)
    print(new_arr)


def value_greater_than_mean(np_arr) -> None:
    print(np_arr > np.mean(np_arr))


normalize(arr_2)

value_greater_than_mean(arr_1)

raw_no_missing = raw[:, 3] < 999.9
print(np.mean(raw_no_missing))
