import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter your project name: ")
    if project_name.strip() != '':
        break

logging.info(f"Creating project by name: {project_name}")

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/model_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/utils.py",
    f"config/config.yaml",
    f"config/schema.yaml",
    f"config/model.yaml",
    f"templates/index.html",
    f"notebook/__init__.py",
    f"data",
    "main.py",
    "setup.py",
    "demo.py",
    "app.py",
    "requirements.txt",
    "user.txt"
    "README.md",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a new directory at: {filedir} for file: {filename}")

    full_filepath = os.path.join(filedir, filename)
    if (not os.path.exists(full_filepath)) or (os.path.getsize(full_filepath) == 0):
        with open(full_filepath, "w"):
            pass
        logging.info(f"Creating a new file: {filename} for path: {full_filepath}")
    else:
        logging.info(f"File is already present at: {full_filepath}")
