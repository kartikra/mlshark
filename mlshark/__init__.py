import pathlib
import mlshark

PACKAGE_ROOT = pathlib.Path(mlshark.__file__).resolve().parent
VERSION_PATH = PACKAGE_ROOT / 'VERSION'

name = "mlshark"

with open(VERSION_PATH, 'r') as version_file:
    __version__ = version_file.read().strip()