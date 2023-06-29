import matplotlib.pyplot as plt

from utils.Series import Series


series = Series({
    'A0': 1,
    'K0': 1,
    'L0': 1,
    'Y0': 1,
    'n': 100,
    'alpha': 0.5,
    'depreciation': 0.5,
    'pop_growth': 0.5,
    'savings': 0.5,
    'innovation': 0.05,
})

series.createDataset()
# series.print()
series.plot()




