def create_chunks(parsed_file, file_path, file_content):
    """
    Convert parsed code into semantic chunks.
    """

    chunks = []

    # Split the original file into lines
    lines = file_content.splitlines()

    # -------------------------
    # Create chunks for classes
    # -------------------------
    for cls in parsed_file["classes"]:

        class_text = "\n".join(
            lines[
                cls["start_line"] - 1 : cls["end_line"]
            ]
        )

        chunk = {
            "type": "class",
            "language": parsed_file["language"],
            "file_path": file_path,
            "name": cls["name"],
            "start_line": cls["start_line"],
            "end_line": cls["end_line"],
            "methods": cls["methods"],
            "text": class_text,
        }

        chunks.append(chunk)

    # ----------------------------
    # Create chunks for functions
    # ----------------------------
    for func in parsed_file["functions"]:

        function_text = "\n".join(
            lines[
                func["start_line"] - 1 : func["end_line"]
            ]
        )

        chunk = {
            "type": "function",
            "language": parsed_file["language"],
            "file_path": file_path,
            "name": func["name"],
            "start_line": func["start_line"],
            "end_line": func["end_line"],
            "text": function_text,
        }

        chunks.append(chunk)

    return chunks