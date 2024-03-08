import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns
    
    Args:
        path_to_yaml (str): Path to the yaml file
        
    Raises:
        ValueError: If the yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: A ConfigBox object
        
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories in a list
    
    Args:
        path_to_directories (list): List of path of directories
        ignore_log(bool, optional): Ignore if multiple directories are to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path_to_json: Path, data: dict):
    """Saves a json file
    
    Args:
        path_to_json (str): Path to the json file
        data (dict): Data to be saved
    """
    with open(path_to_json, "w") as outfile:
        json.dump(data, outfile, indent=4)

    logger.info(f"json file: {path_to_json} saved successfully")


@ensure_annotations
def load_json(path_to_json: Path) -> ConfigBox:
    """
    Loads a json file and returns it
    
    Args:
        path_to_json (str): Path to the json file
        
    Returns:
        ConfigBox: Data as class attributes instead of a dictionary
    """
    with open(path_to_json, "r") as json_file:
        data = json.load(json_file)
    
    logger.info(f"json file: {path_to_json} loaded successfully")
    return ConfigBox(data)

@ensure_annotations
def save_binary(data: Any, path_to_binary: Path):
    """
    Saves a binary file
    
    Args:
        data (Any): Data to be saved as a binary file
        path_to_binary (str): Path to the binary file
    """
    joblib.dump(value=data, filename=path_to_binary)
    logger.info(f"binary file: {path_to_binary} saved successfully")


@ensure_annotations
def load_binary(path_to_binary: Path) -> Any:
    """
    Loads a binary file and returns it
    
    Args:
        path_to_binary (str): Path to the binary file
        
    Returns:
        Any: Data loaded from the binary file
    """
    data = joblib.load(path_to_binary)
    logger.info(f"binary file loaded from {path_to_binary} successfully")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size of a file in kb

    Args:
        path: Path to the file
        
    Returns:
        str: Size in kb
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"


def decode_image(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encode_image_toBase64(cropped_image_path):
    with open(cropped_image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read())
    