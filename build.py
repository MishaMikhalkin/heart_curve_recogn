import sys
from pynt import task


@task()
def clean():
    print("Cleaning build directory...")