#!/bin/sh

echo "Running build_files.sh..."

# Print the current directory
echo "Current directory:"
pwd

# List files in the current directory
echo "Files in current directory:"
ls -la

# Check for Python version
echo "Checking Python and pip versions:"
python3 --version || { echo "Python3 not found"; exit 1; }
pip3 --version || { echo "pip3 not found"; exit 1; }

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt || { echo "Failed to install dependencies"; exit 1; }

# Collect static files
echo "Running collectstatic..."
python3 manage.py collectstatic --noinput || { echo "collectstatic failed"; exit 1; }

# Run migrations
echo "Running migrations..."
python3 manage.py migrate || { echo "migrations failed"; exit 1; }

echo "build_files.sh completed successfully."
