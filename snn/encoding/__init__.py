import numpy as np


def kulkarni_rajendran(spikes: np.array) -> np.array:
    """
        Based on Kulkarnia and Rajendran encoding from:
        ElsevierNN_published_paper.pdf
    """
    return np.array(list(map(lambda x: 2700 + (x * 101.2), spikes)))
