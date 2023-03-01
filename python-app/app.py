import sys

import numpy as np
import pandas as pd


def main():
    print("Hello world")
    print(f"Python version: {sys.version}")
    print(f"Numpy version: {np.__version__}")
    print(f"Pandas version: {pd.__version__}")
    print(f"Numpy array: {np.array([1, 2, 3])}")
    print("Pandas dataframe: {}".format(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})))


if __name__ == "__main__":
    main()
