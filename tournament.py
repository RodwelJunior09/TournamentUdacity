#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("DELETE FROM Matches")
    cursor.execute("DELETE FROM Winners")
    cursor.execute("DELETE FROM Losers")
    cursor.execute("UPDATE players set wins = 0, matches = 0")
    cursor.execute("ALTER SEQUENCE matches_id_match_seq RESTART with 1")
    DB.commit()
    DB.close()

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("DELETE FROM players")
    cursor.execute("ALTER SEQUENCE players_id_seq RESTART with 1")
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT COUNT(*) FROM players")
    count = cursor.fetchall()
    DB.close()
    return count[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("INSERT INTO players VALUES(%s)", (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    Lists = []
    DB = connect()
    cursor = DB.cursor()
    # cursor.execute("SELECT * FROM players_count_wins")
    # cursor.execute("SELECT * FROM Matchescount")
    # cursor.execute("SELECT id, name, count(winner_id), count(*) From players, Winners GROUP BY id, name")
    cursor.execute("SELECT players.id, players.name, players.wins , players.matches FROM players ORDER BY players.wins DESC")
    for player in cursor.fetchall():
        Lists.append(player)
    # cursor.execute("SELECT COUNT(*) FROM Winners, players where Winners.winner_id = players.id")
    cursor.execute("SELECT * FROM players")
    # print cursor.fetchall()
    # print Lists
    DB.close()
    return Lists


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("INSERT INTO Matches VALUES(%s, %s)", (winner, loser))
    cursor.execute("UPDATE players set wins = wins + (%s), matches = matches + (%s) where id=(%s)", (1, 1, winner))
    cursor.execute("UPDATE players set matches = matches + (%s) where id=(%s)", (1, loser))
    DB.commit()
    cursor.execute("INSERT INTO Winners VALUES(%s)", (winner,))
    cursor.execute("INSERT INTO Losers VALUES(%s)",(loser,))
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # Pair1, Pair2, Pair3, Pair4  = [], [], [], []
    Rounds = []
    pairs = ()
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM players_pair")
    for element in cursor.fetchall():
        pairs += element[0], element[1]
        # if len(List_of_pairs1) != 1:
        if len(pairs) == 4:
            Rounds.append(pairs)
            pairs = ()
        # else:
        #     if len(pairs) == 4:
        #         List_of_pairs2.append(pairs)
        #         pairs = ()

    print Rounds
    return Rounds


    # for element in List_of_pairs:


    # for p in player:
    #     List_of_pairs.append(p)
    #
    # print List_of_pairs

    # print pairs
