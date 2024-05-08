import os


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
