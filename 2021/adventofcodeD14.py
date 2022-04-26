import sys

from collections import defaultdict

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = ""


def load_data(file):
    input_file = open(file, "r")
    polymer = input_file.readline().strip().replace('\n', '')
    input_file.readline()
    rules_dict = create_rules_dict(input_file.readlines())
    input_file.close()
    return polymer, rules_dict


def create_rules_dict(rules):
    rules = [[pair[0], pair[1]] for pair in
             [(item.strip().replace('\n', '').split(' -> ')) for item in rules]]
    rules_dict = defaultdict(lambda: "No Rule")
    for rule in rules:
        rules_dict[rule[0]] = rule[1]
    return rules_dict


def start_pairs_tally(polymer):
    starting_pairs = defaultdict(lambda: 0)
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        starting_pairs[pair] += 1
    tally = defaultdict(lambda: 0)
    for i in range(len(polymer)):
        tally[polymer[i]] += 1
    return starting_pairs, tally


def pairing(rules, pairs, tally):
    new_pairs = defaultdict(lambda: 0)
    for pair in pairs.items():
        children, tally = get_children(rules, pair, tally)
        for child in children:
            new_pairs[child] += pair[1]
    return new_pairs, tally


def get_children(rules, pair, tally):
    children = []
    if rules[pair[0]] != "No Rule":
        child_part = rules[pair[0]]
        tally[child_part] += pair[1]
        children.append(pair[0][:1] + child_part)
        children.append(child_part + pair[0][1:])
    return children, tally


def stepper(rules, pairs, tally, steps):
    for _ in range(steps):
        pairs, tally = pairing(rules, pairs, tally)
    counted = tally.values()
    return max(counted) - min(counted)


def main():
    polymer, rules = load_data(file_name)
    pairs, tally = start_pairs_tally(polymer)
    print(stepper(rules, pairs.copy(), tally.copy(), 10))
    print(stepper(rules, pairs.copy(), tally.copy(), 40))


if __name__ == '__main__':
    main()
