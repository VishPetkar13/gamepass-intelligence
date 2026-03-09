import os
from dotenv import load_dotenv
import kaggle


load_dotenv()
kaggle.api.authenticate()

kaggle.api.dataset_download_files(dataset="fronkongames/steam-games-dataset", 
        path="data/raw/", unzip=True)