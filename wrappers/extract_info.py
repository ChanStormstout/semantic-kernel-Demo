import re

def extract_dependencies_from_file(dot_content, target_file):
    """
    Extract all dependency lines for a given file from the DOT file content.
    
    :param dot_content: A string containing the contents of the DOT file.
    :param target_file: The file name of which to find the dependencies.
    :return: A list of all dependency lines for the target file.
    """
    pattern = re.compile(r'("([^"]+)" -> "([^"]+)")')
    # Find all matches of the pattern in the DOT content
    all_edges = pattern.findall(dot_content)

    # Filter edges that involve the target file
    relevant_edges = [match[0] for match in all_edges if target_file in match[1:]]

    # Return the list of relevant dependency lines
    return relevant_edges

def get_dependencies(target_file):
    with open('output.dot', 'r') as file:
        dot_file_content = file.read()
        return extract_dependencies_from_file(dot_file_content, target_file)

def read_file(file_path):
    """
    Reads the content of a C file and stores it in a string variable.

    :param file_path: Path to the C file.
    :return: A string containing the content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

# Example usage
# dependencies = get_dependencies("ares_create_query.c")
# print(dependencies)
