#!/usr/bin/env python3
import yaml
import os
import sys
import pprint

pp = pprint.PrettyPrinter()
dirs = {
        "characters": os.path.abspath("files/characters"),
        "zones": os.path.abspath("files/zones"),
        "items": os.path.abspath("files/items"),
        }


game_config = {
        "characters": {},
        "zones": {},
        "items": {},
        }

class Game():
    def __init__(self, data):
        for zone in data["zones"]:
            self.zones = [[ Zone(data["zones"][zone]) for zone in data["zones"] ]]
        for character in data["characters"]:
            self.characters = [[ Character(data["characters"][character]) for character in data["characters"] ]]
        for item in data["items"]:
            self.items = [[ Item(data["items"][item]) for item in data["items"] ]]
        
    def show(self):
        for zone in self.zones:
            print(zone[0].show_data())

class Zone():
    def __init__(self, data):
        self.data = data

    def show_data(self):
        print(self.data)

class Character():
    def __init__(self, data):
        self.data = data

    def show(self):
        print(self.data)

class Item():
    def __init__(self, data):
        self.data = data

    def show(self):
        print(self.data)

# Import Asset Files
for asset_type in game_config.keys():
    for root, subdir, assets in os.walk(dirs[asset_type]):
        for asset_file in assets:
            asset = yaml.safe_load(open(os.path.join(root, asset_file), "r").read())
            game_config[asset_type][asset["id"]] = asset

game = Game(game_config)
game.show()
