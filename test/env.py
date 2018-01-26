#!/usr/bin/env python
# encoding: utf-8
import os
import pathlib
import dotenv

from collections import namedtuple


ROOT_DIR_PATH = pathlib.Path(__file__).resolve().parent.parent

dotenv_path = ROOT_DIR_PATH.joinpath('.env')
if dotenv_path.exists():
    dotenv.load_dotenv(str(dotenv_path))


clientinfo = namedtuple(
    'clientinfo',
    ['client_id', 'client_secret']
)

CLIENT_ID = os.environ['client_id']
CLIENT_SECRET = os.environ['client_secret']

ClientInfo = clientinfo(CLIENT_ID, CLIENT_SECRET)
