import numpy as np
import astropy
from astropy.table import Table
from astropy.io import ascii
from astropy.io import fits


def main():
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)
    data = Table([x, y], names=["x", "sin(x)"])
    print(data)


if __name__ == "__main__":
    main()
