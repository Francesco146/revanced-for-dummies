import itertools
import os
from argparse import ArgumentParser
from pathlib import Path
from typing import Iterator, Tuple


def is_iterator_empty(it: Iterator) -> Tuple[bool, Iterator]:
    """
    Check if an iterator is empty and return a tuple with a boolean indicating if it is empty and the iterator itself.

    :param it: The iterator to check.
    :return: A tuple containing a boolean indicating if the iterator is empty and the iterator itself.
    """
    try:
        peek = next(it)
        return False, itertools.chain([peek], it)
    except StopIteration:
        return True, it


def get_latest_file(path: str, included_suffix: str) -> Path:
    """
    Get the latest file from a directory, including only files with a certain suffix.

    :param path: The directory to search.
    :param included_suffix: The file suffix to include.
    :return: The latest file.
    :raises FileNotFoundError: If no files with the specified suffix are found in the directory.
    """
    files = (release for release in Path(path).iterdir() if release.suffix == included_suffix)

    is_empty, files = is_iterator_empty(files)

    if is_empty:
        raise FileNotFoundError(f"No files with suffix {
                                included_suffix} found in {path}")

    return max(files, key=os.path.getctime)


def main() -> None:
    """
    Parse command-line arguments and save the latest patches and integrations file paths to an .env file.

    :raises FileNotFoundError: If no files with the specified suffix are found in the provided directories.
    """
    parser = ArgumentParser(
        description='Save the latest patches and integrations file paths to an .env file.')
    parser.add_argument('patches_path', metavar='PATCHES_PATH', type=str,
                        help='the directory where the patches are stored')
    parser.add_argument('integrations_path', metavar='INTEGRATIONS_PATH', type=str,
                        help='the directory where the integrations are stored')
    parser.add_argument('-o', metavar='ENV_PATH', type=str,
                        help='the path of the output environment file', required=True)

    args = parser.parse_args()

    latest_patch = get_latest_file(args.patches_path, '.jar')
    latest_integration = get_latest_file(args.integrations_path, '.apk')

    with open(args.o, 'w') as f:
        f.write(f'PATCHES_PATH={latest_patch}\n')
        f.write(f'INTEGRATIONS_PATH={latest_integration}\n')


if __name__ == "__main__":
    main()
