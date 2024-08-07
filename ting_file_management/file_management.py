import sys
import re


def txt_importer(path_file):
    if re.search(r"\.txt$", path_file) is None:
        print("Formato inválido", file=sys.stderr)
        return None
    try:
        with open(path_file) as file:
            return file.read().split("\n")
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None
