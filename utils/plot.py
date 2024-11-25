import matplotlib.pyplot as plt
import numpy as np

from .weather import WeatherData


def plot_to_a_file(data: list[WeatherData], filename: str):
    """
    Plot Data and save it to file
    """
    precipation_proba = []
    precipation = []
    t = np.arange(24)

    for d in data:
        precipation_proba.append(d.precipitation_probability)
        precipation.append(d.precipitation)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time (H)')
    ax1.set_ylabel('precipation', color=color)
    ax1.bar(t, precipation, color=color)
    ax1.tick_params(axis='y', color=color)

    ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis

    color = 'tab:blue'
    # we already handled the x-label with ax1
    ax2.set_ylabel('precipitaion probability', color=color)
    ax2.plot(t, precipation_proba, 'o-', color=color)
    ax2.tick_params(axis='y', color=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.grid()
    plt.savefig(filename)
