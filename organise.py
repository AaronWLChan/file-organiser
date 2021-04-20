from pathlib import Path
from sys import argv
import shutil
from categories import categories
import argparse

## Setup args parser
parser = argparse.ArgumentParser(description="Organize Files In Directory")
parser.add_argument('directory', metavar="'dir'", type=str, help="Directory Name" )
args = parser.parse_args()

path = Path(args.directory)

if path.is_dir():

    ## Retrieves category based on extension
    extensions = {extension: category
                    for category, extensions in categories.items()
                    for extension in extensions
                    }
    
    for file in path.iterdir():
        #File path
        filePath = file.absolute()

        if filePath.is_file():

            # Get Extension
            extension = file.suffix[1:]

            # Check if extension exists
            destination = None

            if extension in extensions:
                destination = path / extensions[extension]

            else:
                destination = path / "Other"

            if not destination.exists():
                destination.mkdir()

            shutil.move(str(filePath), str(destination))

    print(f"Directory '{args.directory}' organised.")

else:
    raise Exception("This is not a directory!")