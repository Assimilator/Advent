import sys


def loadData():
    inputFile = open(sys.argv[1], "r")
    lines=inputFile.readlines()
    links = []
    for line in lines:
        links.append(line.strip().replace('\n','').split('-'))
    return links

def processNodes(node, usedNodes, links, extraPass = 0, usedNode = ''):
    children = getChildren(node, links)
    ends = 0
    if len(children) == 0:
        return 0
    if 'end' in children:
        ends += 1
    if node.islower():
        usedNodes.append(node)
    for child in children:
        if child not in ['start', 'end']:
            if child not in usedNodes:
                ends += processNodes(child, usedNodes.copy(), links, extraPass, usedNode)
            elif extraPass > 0 and usedNode == '':
                ends += processNodes(child, usedNodes.copy(), links, extraPass, child)
    return ends

def getChildren(node, links):
    children = []
    for link in links:
        if node in link:
            children.extend(link)
    children = list(filter((node).__ne__, children))
    return children

def main():
    links = loadData()
    count = processNodes('start', [], links)
    print(count)
    count = processNodes('start', [], links, 1, '')
    print(count)

if __name__ == '__main__':
    main()