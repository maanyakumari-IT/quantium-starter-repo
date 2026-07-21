#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run test suite
pytest

# Return appropriate exit code
if [ $? -eq 0 ]; then
    exit 0
else
    exit 1
fi