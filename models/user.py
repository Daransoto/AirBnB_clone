#!/usr/bin/python3
"""Users"""

import models
from models.base_model import BaseModel


class User(BaseModel):
    """A class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
