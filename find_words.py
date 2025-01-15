from collections import defaultdict
from functools import partial
from argparse import ArgumentParser


def filter_not_contain(word, contain_displace_dict):
    for i, char in enumerate(word):
        if i in contain_displace_dict[char]:
            return False
    return True


def filter_contain(word, contain):
    for i, char in contain.items():
        if word[i] != char:
            return False
    return True


#
def find_word(file_name, length, not_contain='', contain_displace='', contain=''):
    with open(file_name, 'r', encoding='utf-8') as file:
        dropout = (word.lower() for word in file.read().split('\n') if len(word) == length)

    contain_displace_dict = defaultdict(list)

    for char, *i in contain_displace.split():
        contain_displace_dict[char].append(int(''.join(i)))

    contain_dict = {int(''.join(i)): char for char, *i in contain.split()}

    dropout = [*filter(lambda word: set(word).issuperset(set(contain_displace_dict)), dropout)]
    dropout = [*filter(lambda word: set(word).isdisjoint(set(not_contain)), dropout)]
    dropout = [*filter(partial(filter_contain, contain=contain_dict), dropout)]
    dropout = [*filter(partial(filter_not_contain, contain_displace_dict=contain_displace_dict), dropout)]

    print([*dropout])


def main():
    parser = ArgumentParser(description='Find the world')
    parser.add_argument('file', help='Words base')
    parser.add_argument('length', type=int, help='Length of word')
    parser.add_argument('--not_contain', '-nc', default='', help='Letters that are not contained')
    parser.add_argument('--contain_displace', '-cd', default='',
                        help='Letters that are contained and their indices where they cannot be (<char><i>)')
    parser.add_argument('--contain', '-c', default='', help='Letters contained in a word and their indices (<char><i>)')
    args = parser.parse_args()
    find_word(args.file, args.length, args.not_contain, args.contain_displace, args.contain)


if __name__ == '__main__':
    main()
