#!/bin/bash
echo "Creating Conda environment from environment.yml..."
conda env create -f environment.yml || conda env update -f environment.yml --prune
echo "Done. Run 'conda activate <environment-name>' to activate the environment."
