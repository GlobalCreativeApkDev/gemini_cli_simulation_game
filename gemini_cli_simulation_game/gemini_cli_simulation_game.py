"""
This file contains code for the game "Gemini CLI Simulation Game".

Authors:
1. GlobalCreativeApkDev
2. Renatha Salfa
"""


# Game version: 1


# Importing necessary libraries


import sys
import time
import uuid
import pickle
import copy
import google.generativeai as gemini
import random
from datetime import datetime
import os
from dotenv import load_dotenv
from functools import reduce

from mpmath import mp, mpf
from tabulate import tabulate

mp.pretty = True


# Creating main functions to be used in this game.


def is_number(string: str) -> bool:
    try:
        mpf(string)
        return True
    except ValueError:
        return False


def list_to_string(a_list: list) -> str:
    res: str = "["  # initial value
    for i in range(len(a_list)):
        if i == len(a_list) - 1:
            res += str(a_list[i])
        else:
            res += str(a_list[i]) + ", "

    return res + "]"


def load_game_data(file_name):
    # type: (str) -> SavedGameData
    return pickle.load(open(file_name, "rb"))


def save_game_data(game_data, file_name):
    # type: (SavedGameData, str) -> None
    pickle.dump(game_data, open(file_name, "wb"))


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# TODO: create more necessary static functions.


###########################################
# GENERAL
###########################################


# TODO: create more necessary classes.


class Player:
    """
    This class contains attributes of the player in this game.
    """

    def __init__(self, name):
        # type: (str) -> None
        self.player_id: str = str(uuid.uuid1())
        self.name: str = name
        self.level: int = 1

        # TODO: add more attributes to the player, depending on the type of simulation game.

    def clone(self):
        # type: () -> Player
        return copy.deepcopy(self)


class SavedGameData:
    """
    This class contains attributes of the saved game data in this game.
    """

    def __init__(self, player_name, temperature, top_p, top_k, max_output_tokens, player_data):
        # type: (str, float, float, float, int, Player) -> None
        self.player_name: str = player_name
        self.temperature: float = temperature
        self.top_p: float = top_p
        self.top_k: float = top_k
        self.max_output_tokens: int = max_output_tokens
        self.player_data: Player = player_data

    def __str__(self):
        # type: () -> str
        res: str = ""  # initial value
        res += str(self.trainer_name).upper() + "\n"
        res += "Temperature: " + str(self.temperature) + "\n"
        res += "Top P: " + str(self.top_p) + "\n"
        res += "Top K: " + str(self.top_k) + "\n"
        res += "Max output tokens: " + str(self.max_output_tokens) + "\n"
        return res

    def clone(self):
        # type: () -> SavedGameData
        return copy.deepcopy(self)


###########################################
# GENERAL
###########################################


# Creating main function used to run the game.


def main() -> int:
    """
    This main function is used to run the game.
    :return: an integer
    """

    load_dotenv()
    gemini.configure(api_key=os.environ['GEMINI_API_KEY'])

    # Gemini safety settings
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    # Saved game data
    saved_game_data: SavedGameData

    # The player's name
    player_name: str = ""  # initial value

    # Gemini Generative Model
    model = gemini.GenerativeModel(model_name="gemini-1.5-pro",
                                       generation_config={
                                           "temperature": 1,
                                           "top_p": 0.95,
                                           "top_k": 64,
                                           "max_output_tokens": 8192,
                                           "response_mime_type": "text/plain",
                                       },
                                       safety_settings=safety_settings)  # initial value

    print("Enter \"NEW GAME\" to create new saved game data.")
    print("Enter \"LOAD GAME\" to load existing saved game data.")
    action: str = input("What do you want to do? ")

    # TODO: implement in-game functionality

    # Start playing the game.
    while True:
        clear()


if __name__ == "__main__":
    main()
