#!/usr/bin/python3
"""A module containing the State model"""
from models.base_model import BaseModel


class State(BaseModel):
    """Implements the State model for any state object"""
    name = ""
			   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
