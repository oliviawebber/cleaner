import click
import os
from functools import partial

def get_size(name: str) -> int:
    return os.path.getsize(name)

@click.command()
@click.option("--root", default=os.getcwd(), help="The root folder to start listing from.")
def main(root: str):
    """Main interface for listing large files."""
    files = []
    for (dirpath, _, filenames) in os.walk(root):
       if filenames == []:
           continue
       path = partial(os.path.join, dirpath)
       sizes = list(map(lambda x: (path(x), get_size(path(x))), filenames))
       files.extend(sizes)

    files.sort(key=lambda x: x[1], reverse=True)

    for (name, size) in files:
        print("File: {} Size: {}".format(name, size))
