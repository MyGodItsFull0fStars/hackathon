import os
import torch
import torchaudio
import torchaudio.functional as F
import torchaudio.transforms as T

import matplotlib.pyplot as plt

from IPython.display import Audio, display


def plot_waveform(waveform, sample_rate, title="Waveform", xlim=None, ylim=None) -> None:
    waveform = waveform.numpy()

    num_channels, num_frames = waveform.shape
    time_axis = torch.arange(0, num_frames) / sample_rate

    figure, axes = plt.subplots(num_channels, 1)
    if num_channels == 1:
        axes = [axes]
    for c in range(num_channels):
        axes[c].plot(time_axis, waveform[c], linewidth=1)
        axes[c].grid(True)
        if num_channels > 1:
            axes[c].set_ylabel(f'Channel {c+1}')
        if xlim:
            axes[c].set_xlim(xlim)
        if ylim:
            axes[c].set_ylim(ylim)
    figure.suptitle(title)
    plt.show(block=False)


def play_audio(waveform, sample_rate) -> None:
    waveform = waveform.numpy()

    num_channels, num_frames = waveform.shape
    if num_channels == 1:
        display(Audio(waveform[0], rate=sample_rate))
    elif num_channels == 2:
        display(Audio((waveform[0], waveform[1]), rate=sample_rate))
    else:
        raise ValueError(
            "Waveform with more than 2 channels are not supported.")


def inspect_file(path) -> None:
    print("-" * 10)
    print("Source:", path)
    print("-" * 10)
    print(f" - File size: {os.path.getsize(path)} bytes")
    print(f" - {torchaudio.info(path)}")


def is_sound_file(file_path: str) -> bool:
    """Returns True if the file is a sound file

    Parameters
    ----------
    file_path : str


    Returns
    -------
    bool
        True if it is a sound file, False if not
    """
    return file_path.endswith('wav')


def get_sound_effects(dir_path: str) -> list[str]:
    """Returns list of sound files

    Parameters
    ----------
    dir_path : str
        directory path

    Returns
    -------
    list[str]
        list of all sound files
    """
    sound_list: list[str] = [
        s for s in os.listdir(dir_path) if is_sound_file(s)]
    return sound_list
