import re
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion

kernel = sk.Kernel()
# Configure AI service used by the kernel
api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))
search_term = "search_content"

def extract_dependencies_from_file(dot_content, target_file):
    """
    Recursively extract all dependencies for a given file from the DOT file content.
    
    :param dot_content: A string containing the contents of the DOT file.
    :param target_file: The file name of which to find the dependencies.
    :return: A set of all dependencies for the target file, including indirect dependencies.
    """
    pattern = re.compile(r'"([^"]+)" -> "([^"]+)"')
    # Find all matches of the pattern in the DOT content
    edges = pattern.findall(dot_content)

    # Build a dependency graph
    dependency_graph = {}
    for source, target in edges:
        if source in dependency_graph:
            dependency_graph[source].add(target)
        else:
            dependency_graph[source] = {target}

    # Recursive function to find dependencies
    def find_dependencies(file, graph, seen):
        if file in seen:
            return
        seen.add(file)
        for dependency in graph.get(file, []):
            find_dependencies(dependency, graph, seen)

    # Initialize the set to store all dependencies
    seen_dependencies = set()
    # Start the recursive search for dependencies
    find_dependencies(target_file, dependency_graph, seen_dependencies)
    # Remove the target file from the set of dependencies
    seen_dependencies.discard(target_file)

    # Return the sorted list of dependencies
    return sorted(seen_dependencies)

def get_dependencies():
    with open('output.dot', 'r') as file:
        dot_file_content = file.read()
    # Specify the file you want to extract dependencies for
    target_file = 'bthread.cpp'
    #Extract the dependencies
    dependency_info = extract_dependencies_from_file(dot_file_content, target_file)

    # print(f"Dependencies for {target_file}:")
    # for dep in dependency_info:
    #     print(dep)

    testsuite_dependencies = extract_dependencies_from_file(dot_file_content, 'testsuite.c')
    # Print the dependencies
    print("All dependencies of 'testsuite.c':")
    for dep in testsuite_dependencies:
        print(dep)



