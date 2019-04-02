import numpy as np


def kulkarni_rajendran(inpts: np.array) -> np.array:
    """
        Based on Kulkarnia and Rajendran encoding from:
        ElsevierNN_published_paper.pdf
    """

    def _encode(x):
        return 2700 + (x * 101.2)

    return np.vectorize(_encode)(inpts)
