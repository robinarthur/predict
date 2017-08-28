"""0_scraping.py
https://github.com/llSourcell/Predicting_Winning_Teams


Database if fully cached at first invocation so there won't by any additional requests:

.. code-block:: python

    >>> fut.nations
    >>> fut.leagues
    >>> fut.teams
    >>> fut.stadiums
    >>> fut.players
    >>> fut.playstyles

You can access database even without login:

.. code-block:: python

    >>> import fut
    >>> nations = fut.core.nations()
    >>> leagues = fut.core.leagues()
    >>> teams = fut.core.teams()
    >>> stadiums = fut.core.stadiums()
    >>> players = fut.core.players()
    >>> playestyles = fut.core.playstyles()

"""

import sys
sys.path.append("fut")
import fut

nations = fut.core.nations()
leagues = fut.core.leagues()
teams = fut.core.teams()
stadiums = fut.core.stadiums()
players = fut.core.players()
playstyles = fut.core.playstyles()


#print("nations", nations)
#print("leagues", leagues)
print("teams", teams)
