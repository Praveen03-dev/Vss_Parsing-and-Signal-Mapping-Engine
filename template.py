import os
from pathlib import Path
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "vss_to_vhal_mapper"

# Define the folder and file structure
list_of_files = [
    f"{project_name}/main.py",

    # Signal parser
    f"{project_name}/signal_parser/__init__.py",
    f"{project_name}/signal_parser/vss_parser.py",

    # Mapping loader
    f"{project_name}/mapping_loader/__init__.py",
    f"{project_name}/mapping_loader/mapping_loader.py",

    # HAL parser
    f"{project_name}/hal_parser/__init__.py",
    f"{project_name}/hal_parser/hal_parser.py",

    # Merger
    f"{project_name}/merger/__init__.py",
    f"{project_name}/merger/signal_merger.py",

    # Data models
    f"{project_name}/model/__init__.py",
    f"{project_name}/model/signal.py",
    f"{project_name}/model/constants.py",

    # Sample test data
    f"{project_name}/sample_data/VehicleSignalSpecification.vspec",
    f"{project_name}/sample_data/overlays/production.vspec",
    f"{project_name}/sample_data/mapping.yml",
    f"{project_name}/sample_data/types.hal",

    # Tests
    f"{project_name}/tests/__init__.py",
    f"{project_name}/tests/test_vss_parser.py",

    # Metadata and config
    f"{project_name}/requirements.txt",
    f"{project_name}/README.md",
    f"{project_name}/.gitignore",
    f"{project_name}/.vscode/settings.json",
]

# Create files and folders
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent

    # Create directory
    if filedir != Path("."):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    # Create empty file if not present or empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")