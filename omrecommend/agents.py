# -*- coding: utf-8 -*-
"""OpenMaker module for agent design.

This module contains Pyhton class objects for agent based modellings.

Todo:
    * Design abstract agent object
    * Design Maker agent object
"""
import sys, os
sys.path.insert(0, os.path.abspath('../'))

from .utilities import get_attributes

class Agent(object):
    """A generic agent class.

    Args:
        id (:obj:`int`)): A unique identifier for the agent.
        state (:obj:`str`, optional): Current state of the agent.

    Attributes:
        id (:obj:`int`)): A unique identifier for the agent.
        state (:obj:`str`, optional): Current state of the agent.

    """

    def __init__(self, id, state = 'idle', type = 'generic'):
        self.id = id
        self.state = state
        self.type = type

    def current_state(self):
        """It reports the current state of the agent.

        Returns:
            (:obj:`dict`): A `dict` summarizing the state of the agent.

        """

        state = {'id': self.id, 'state': self.state, 'type': self.type}
        return state




class Maker(Agent):
    """A maker (:obj:`Agent`) class.

        Notes:


        Attributes:
            name (:obj:`str`, optional): Name of the maker.
            surname (:obj:`str`, optional): Surname of the maker.
            twitter (:obj:`str`, optional): Twitter name of the maker.
            omid (:obj:`int`, optional): OpenMaker platform id of the maker.
            tags (:obj:`list` of :obj:`str`, optional): Self assigned tags of the maker.
            skills (:obj:`list` of :obj:`str`, optional): Skills of the agent.
            technologies(:obj:`list` of :obj:`str`, optional): Technologies used by the agent.
            areas (:obj:`list` of :obj:`str`, optional): Interest areas in terms technologies.
            domains (:obj:`list` of :obj:`str`, optional): Activity domains of the agent.

    """
    name = ''
    surname = ''
    twitter = ''
    omid = 0
    tags = []
    skills = []
    technologies = []
    areas = []
    domains = []

    def __init__(self, id, state='idle'):
        super().__init__(id, state, type = 'Maker')

    def load_profile(self, profile):
        """Updates or loads the profile od the agent.

            Args:
                profile (:obj:`dict`): A python dictionary where keys are attributes of
                this class data attributes and values are the values to be loaded.

            Returns:
                (obj:`bool`): when successful.

        """
        attrs = get_attributes(self)
        attrs.extend(get_attributes(Maker))
        for k,v in profile.items():
            if k not in attrs: continue
            assignment = "self.{} = {}".format(k,v)
            exec(assignment)

        return True

if __name__ == '__main__': pass
