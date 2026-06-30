import re


def split_repository_content(content: str):
    """
    Split the raw gitingest content into individual files.
    """

    pattern = r"=+\nFILE:\s*(.*?)\n=+\n"

    matches = list(re.finditer(pattern, content))

    files = []

    for i, match in enumerate(matches):
        file_path = match.group(1).strip()

        start = match.end()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(content)

        file_content = content[start:end].strip()

        files.append({
            "path": file_path,
            "content": file_content
        })

    return files