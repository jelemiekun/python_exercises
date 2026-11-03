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


def question_2_2_1() -> None:
    tmax_mon = np.max(raw[3::7, 1])
    print(tmax_mon)


def question_2_2_2() -> None:
    mondays = raw[3::7, 1]
    sd = np.sqrt((np.sum(np.square(mondays - np.mean(mondays)))) / len(mondays))
    print(sd)


def question_2_3_1() -> None:
    axis_0_mean = np.mean(raw, axis=0)
    print(axis_0_mean[1:])


def prac_2_5_1() -> None:
    print(raw[0][0])
    print(raw[[0, 2]])


def prac_2_5_3() -> None:
    whole = raw[:, 1:] > 0
    raw_1 = raw[:, 1:]
    print(raw_1[whole])


normalize(arr_2)

value_greater_than_mean(arr_1)

raw_no_missing = raw[:, 3] < 999.9
print(np.mean(raw_no_missing))

question_2_2_1()
question_2_2_2()
question_2_3_1()
prac_2_5_1()
prac_2_5_3()
