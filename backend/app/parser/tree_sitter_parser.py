from tree_sitter import Language, Parser
import tree_sitter_python

PYTHON_LANGUAGE = Language(tree_sitter_python.language())
parser = Parser(PYTHON_LANGUAGE)

def parse_python_file(file_content: str):
    """
    Parse a Python file and extract classes and functions.
    """

    code = file_content.encode("utf-8")
    tree = parser.parse(code)

    result = {
        "language": "python",
        "classes": [],
        "functions": [],
        "imports": []
    }

    def traverse(node):

        if node.type == "class_definition":

            name_node = node.child_by_field_name("name")

            class_info = {
                "name": code[name_node.start_byte:name_node.end_byte].decode("utf-8"),
                "start_line": node.start_point[0] + 1,
                "end_line": node.end_point[0] + 1,
                "methods": []
            }

            result["classes"].append(class_info)

        elif node.type == "function_definition":

            name_node = node.child_by_field_name("name")

            function_info = {
                "name": code[name_node.start_byte:name_node.end_byte].decode("utf-8"),
                "start_line": node.start_point[0] + 1,
                "end_line": node.end_point[0] + 1
            }

            parent = node.parent

            while parent is not None:

                if parent.type == "class_definition":

                    class_name_node = parent.child_by_field_name("name")

                    class_name = code[
                        class_name_node.start_byte:class_name_node.end_byte
                    ].decode("utf-8")

                    for cls in result["classes"]:
                        if cls["name"] == class_name:
                            cls["methods"].append(function_info)
                            break

                    return

                parent = parent.parent

            result["functions"].append(function_info)

        for child in node.children:
            traverse(child)

    traverse(tree.root_node)

    return result