#!/usr/bin/env python3

"""
Voter Participation in Kiel, Germany
EU Elections 1979-2014
Version: 1.0
Python 3.10+
Date created: August 21st, 2022
Date modified: -
"""

import plotly.express as px

year = [1979, 1984, 1989, 1994, 1999, 2004, 2009, 2014]
voter_participation = [115684, 96752, 104815, 93879, 63185, 62414, 61611, 75741]

fig = px.line(
    x=year,
    y=voter_participation,
    title="Voter Participation in Kiel (EU Elections)",
    labels={"x": "Year", "y": "Voter Participation"},
)

fig.write_html("eu-elections.html", auto_open=True)
