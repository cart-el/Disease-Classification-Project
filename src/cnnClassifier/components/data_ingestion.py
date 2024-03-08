import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from pathlib import Path
from cnnClassifier.utils.reusables import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url, 
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with the following headers: \n{headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists with size: \
                        {get_size(Path(self.config.local_data_file))}")
            
    
    def unzip_file(self):
        """
        Unzips the downloaded file into the data directory

        zip_file_path: str
        Function returns None

        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)