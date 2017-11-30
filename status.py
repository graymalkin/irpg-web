#!/usr/bin/env python3

import sys
import json

"""Status script for IdleRPG. Emits a json blob of useful information
to be displayed on a webpage.

"""

COLUMNS = {
    'username': 0,
    'level': 3,
    'class': 4,
    'next_ttl': 5,
    'nick': 6,
    'online': 8,
    'idled': 9,
    'x_pos': 10,
    'y_pos': 11,
    'on_quest':17,
    'amulet': 21,
    'charm': 22,
    'helm': 23,
    'boots': 24,
    'gloves': 25,
    'ring': 26,
    'leggings': 27,
    'shield': 28,
    'tunic': 29,
    'weapon': 30,

    'alignment': 31
}

def usage():
    print("IdleRPG Status Usage:")
    print("  ./{} <idlerpg.db>".format(sys.argv[0]))

def main():
    if len(sys.argv) < 2 :
        usage()
        return -1
    f = open(sys.argv[1], 'r')
    data = f.read()

    lines = data.splitlines()
    lines = lines[1:] # drop the first line with the column header
    players = []
    
    for line in lines:
        l = line.split("\t")
        p = {
            'username': l[COLUMNS['username']],
            'level': l[COLUMNS['level']],
            'class': l[COLUMNS['class']],
            'next_ttl': l[COLUMNS['next_ttl']],
            'nick': l[COLUMNS['nick']],
            'online': l[COLUMNS['online']],
            'idled': l[COLUMNS['idled']],
            'x_pos': l[COLUMNS['x_pos']],
            'y_pos': l[COLUMNS['y_pos']],
            'on_quest': (l[COLUMNS['on_quest']] == "1"),
            'amulet': l[COLUMNS['amulet']],
            'charm': l[COLUMNS['charm']],
            'helm': l[COLUMNS['helm']],
            'boots': l[COLUMNS['boots']],
            'gloves': l[COLUMNS['gloves']],
            'ring': l[COLUMNS['ring']],
            'leggings': l[COLUMNS['leggings']],
            'shield': l[COLUMNS['shield']],
            'tunic': l[COLUMNS['tunic']],
            'weapon': l[COLUMNS['weapon']],

            'alignment': l[COLUMNS['alignment']]
        }
        players.append(p)

    print(json.dumps(players, indent=4, separators=(',', ': ')))

if __name__ == "__main__":
    main()

