from app.parser.tree_sitter_parser import parse_python_file


def parse_file(file_path: str, file_content: str):
    """
    Dispatch the file to the correct language parser.
    """

    file_path = file_path.lower()

    if file_path.endswith(".py"):
        return parse_python_file(file_content)

    # Future languages
    elif file_path.endswith(".js"):
        return None

    elif file_path.endswith(".ts"):
        return None

    elif file_path.endswith(".java"):
        return None

    elif file_path.endswith(".cpp"):
        return None

    return None