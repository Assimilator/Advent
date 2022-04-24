import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""


def load_data(file):
    input_file = open(file, "r")
    lines = input_file.readlines()
    input_file.close()
    links = []
    for line in lines:
        links.append(line.strip().replace('\n', '').split('-'))
    return links


def process_nodes(node, used_nodes, links, extra_pass=0, used_node=''):
    children = get_children(node, links)
    ends = 0
    if len(children) == 0:
        return 0
    if 'end' in children:
        ends += 1
    if node.islower():
        used_nodes.append(node)
    for child in children:
        if child not in ['start', 'end']:
            if child not in used_nodes:
                ends += process_nodes(child, used_nodes.copy(), links, extra_pass, used_node)
            elif extra_pass > 0 and used_node == '':
                ends += process_nodes(child, used_nodes.copy(), links, extra_pass, child)
    return ends


def get_children(node, links):
    children = []
    for link in links:
        if node in link:
            children.extend(link)
    children = list(filter(node.__ne__, children))
    return children


def main():
    links = load_data(file_name)
    print(process_nodes('start', [], links))
    print(process_nodes('start', [], links, 1, ''))


if __name__ == '__main__':
    main()
