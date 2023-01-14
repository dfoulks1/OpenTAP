#!/usr/bin/env python3
import yaml
import os
import sys

dirs = {
        "characters": os.path.abspath("files/characters"),
        "zones": os.path.abspath("files/zones"),
        "items": os.path.abspath("files/items"),
        }


game = {
        "characters": {},
        "zones": {},
        "items": {},
        }

# Import Asset Files
for asset_type in game.keys():
    for root, subdir, assets in os.walk(dirs[asset_type]):
        for asset_file in assets:
            asset = yaml.safe_load(open(os.path.join(root, asset_file), "r").read())
            game[asset_type][asset["id"]] = asset

print(game)
