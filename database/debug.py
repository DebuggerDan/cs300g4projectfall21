# CS 300 - Group (#4) Project: ChocAn [Section: Database, subsection: Debug] - Fall 2021
# Christopher Juncker, Justin Greever, Samantha Zeigler, Tori Anderson, Naya Mairena, Ian Guy, Dan Jang

# This file contains the debugging functions for the database.
import numpy as np
import os
import sys
import json
import logging
import functools
import inspect
import traceback
import pprint
import pdb
import time
import datetime
import re
import random
import string
import csv
import sqlite3
import pandas as pd
from datetime import date time, timedelta
from collections import namedtuple
from typing import List, Dict, Tuple, Optional, Union


class Debug:
    def __init__(self):
        pass

    def print_provider_list(self, provider_list):
        for provider in provider_list:
            print(provider)

    def print_member_list(self, member_list):
        for member in member_list:
            print(member)

    def print_service_list(self, service_list):
        for service in service_list:
            print(service)

    def print_service_code_list(self, service_code_list):
        for service_code in service_code_list:
            print(service_code)

    def print_service_code_dict(self, service_code_dict):
        for service_code in service_code_dict:
            print(service_code)
    
    def print_member_dict(self, member_dict):
        for member in member_dict:
            print(member)

    def print_provider_dict(self, provider_dict):
        for provider in provider_dict:
            print(provider)

    def print_member_service_dict(self, member_service_dict):
        for member in member_service_dict:
            print(member)

    def print_provider_service_dict(self, provider_service_dict):
        for provider in provider_service_dict:
            print(provider)

    def print_member_service_code_dict(self, member_service_code_dict):
        for member in member_service_code_dict:
            print(member)

    def print_provider_service_code_dict(self, provider_service_code_dict):
        for provider in provider_service_code_dict:
            print(provider)

    