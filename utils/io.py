import os
import pandas as pd
from urllib.request import urlretrieve

def get_anac_data(path_to_file, url, force_download=False):
    """
    Carica i dati json dal sito dell'anac, solo se non esistono in locale
    
    Parameters
    ---------
    path_to_file: string
        Path dove trovare il file json o dove memorizzarlo
    url: string
        Url del sito dell'anac
    force_download: boolean
        Se settato a true forza il download
    
    """
    if force_download or not os.path.exists(path_to_file):
        urlretrieve(url, path_to_file)
    df = pd.read_json(path_to_file)
    return df