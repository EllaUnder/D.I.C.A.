from discord.ext import commands
import discord
import random
import json
import re

with open("files/report.json",'r') as r:
    r_json = json.load(r)
