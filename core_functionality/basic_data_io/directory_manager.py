import os
import shutil
import random
import glob
import shutil
import json
from pathlib import Path
from pprint import PrettyPrinter
from typing import List, Dict


class DirectoryManager:
    """
    Stores system directories
    """

    def __init__(self, path: Path, extensions: List) -> None:
        self._path = path
        self._extensions = extensions
        self._files_to_sort = []
        self._file_map = {}
        self._pp = PrettyPrinter(indent=4)

    def make_example_files(self) -> None:
        """
        Create a random number (between 1 and 100) of empty files
        for each file extension in _extensions
        """
        for ext in self._extensions:
            self._file_map[ext] = []
            ext_qty = random.randint(0, 100)
            (Path(os.getcwd()) / f"example{ext_qty}{ext}").touch()

    def get_extensions(self) -> None:
        for file in self._files_to_sort:
            if Path(file).suffix not in self._extensions:
                self._extensions.append(Path(file).suffix)

    def map_files(self) -> None:
        for ext in self._extensions:
            files = glob.glob(self._path, f"**/*{ext}")
            if ext in self._file_map:
                self._file_map[ext] + files

    def move_files(self) -> None:
        for file in self._files_to_sort:
            dirname = Path(file).suffix[1:]
            if dirname in os.listdir(self._path):
                shutil.move(file, f"{self._path}/{dirname}")
            else:
                os.mkdir(dirname)
                shutil.move(file, f"{self._path}/{dirname}")

    def get_files(self) -> None:
        self._files_to_sort = glob.glob(f"{self._path}/example*")

    def clean_up(self) -> None:
        curr, subdirs, files = []
        for filepath in os.walk(self._path):
            curr, subdirs, files = filepath
        for subdir in subdirs:
            shutil.rmtree(subdir)

    def report(self) -> None:
        with open('file_map.json', 'w') as map_in:
            json.dump(self._file_map, map_in)
            

    def organize_files_in_new_dir(self, dir_name, ext: str) -> None:
        os.mkdir(self._path / f"{dir_name}")

    @property
    def extensions(self) -> list:
        return self._extensions

    @property
    def files_to_sort(self) -> list:
        return self._files_to_sort

    @property
    def file_map(self) -> Dict[str, List[str]]:
        return self._file_map


if __name__ == "__main__":
    dirmgr = DirectoryManager(
        os.getcwd(),
        [
            ".txt",
            ".csv",
            ".yaml",
            ".xml",
            ".xlsx",
        ],
    )
    dirmgr.make_example_files()
    dirmgr.get_files()
    dirmgr.get_extensions()
    dirmgr.move_files()
    dirmgr.map_files()
