# -*- coding: utf-8 -*-
"""Generic interface for recommendations.

This module contains interface fucntions that cna be driven by external API interfaces such as
Flask, Django, Tornado, etc.

Todo:
    * Given a skillset/technologies return most relevant skills/technologies
    * Given two skillsets/technologies return complementarity score
    * Given a skillset/technologies return most relevant profile in terms of skills/technologies
    * Given a member-id return most relevant profile in terms of skills/technologies
    * Given a member-id return compatible/similar/different/partner profile in terms of skills
    * Given a member-id return compatible/similar/different profile in terms of social connections
    * Given a member-id return lits of possible partner profiles in terms of skills and social connections
    * Given a member-id return lits of possible partner profiles in terms of skills and social connections
        along with a recommended collaboration topic.
"""

import sys, os
sys.path.insert(0, os.path.abspath('../'))


if __name__ == '__main__': pass
