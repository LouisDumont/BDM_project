"""
Parses txt files contained in the node_files folder.
Creates the associated instances of Node and Choice
by: Louis Dumont
last modified: 13/04/2019
"""

from choice import Choice
from node import Node
import os
import glob

## Script variables

content_folder = os.getcwd() + "/content" #antislach is for windows

def create_moments(folder):
    """
    Parses the txt files and creates a node from each file
    """
    print(folder)
    files_list = glob.glob(folder + '/*.txt') # antislash for windows
    nodes_list = []
    print(files_list)
    for file in files_list:
        print('Reading new file: ' + str(file))
        with open(file, 'r', encoding='utf-8') as lines:
            name = ''
            description = ''
            for line in lines:
                #print(line)
                if line.startswith("NAME = "):
                    name = line[7:].strip('\n')
                if line.startswith("PAR = "):
                    description += line[6:].strip('\n') + '\n'
                #print("Red new line")
            #print("Creating new node")
            #description = description.encode('utf-8')
            nodes_list.append(Node(name=name, description=description))
    #print(len(nodes_list))
    for node in nodes_list:
        print("New node")
        print(node.name_)
        node.print_description()
    
    return nodes_list
 
def find_node(nodes_list, name):
    """
    Given a name and a node list, returns the index of the node named by "name"
    Arguments:
    ----------
    nodes_list: list of Node
    name: string
    Returns:
    --------
    int
    """
    for i, node in enumerate(nodes_list):
        if node.name_ == name:
            return i
    return None
    
def create_choices(folder, nodes_list):
    """
    Parses the txt files and creates the links (choices) between the nodes
    """
    files_list = glob.glob(folder + '/*.txt')
    for file in files_list:
        print("Reading new file... " + file.split("\\")[-1])
        with open(file, 'r', encoding='utf-8') as lines:
            for line in lines:
                if line.startswith("NAME = "):
                    idx_origin = find_node(nodes_list, line[7:].strip('\n'))
                    print(idx_origin)
                if line.startswith("LINK = "):
                    description = line.split(" ---")[0][7:]
                    idx_destination = find_node(nodes_list, line.split(" ---")[1].strip('\n'))
                    nodes_list[idx_origin].add_choice(description, nodes_list[idx_destination])
                    print("Adding link from node %d to node %f!"%(idx_origin, idx_destination))
                    print("Description: " + description)
    return(nodes_list)
    
def graph_from_text(folder):
    """
    Calls create_moments and create_choices to create the graph from the txt files
    """
    nodes_list = create_moments(folder)
    nodes_list = create_choices(folder, nodes_list)
    return(nodes_list)


if __name__ == "__main__":
    print("Testing the files parsing script...")
    graph_from_text(content_folder)    