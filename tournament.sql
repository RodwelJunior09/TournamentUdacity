-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here

-- CREATE DATABASE tournament;



CREATE TABLE players(name TEXT, wins INT DEFAULT 0, matches INT DEFAULT 0, id serial PRIMARY KEY);

CREATE TABLE Matches(player1_id INT, player2_id INT, id_match SERIAL PRIMARY KEY);

CREATE TABLE Winners(winner_id INT);
--
CREATE TABLE Losers(loser_id INT);

CREATE VIEW players_pair AS
  SELECT id, name FROM players ORDER BY wins; 
  -- SELECT count(players.wins) as PlayersWins FROM players, Winners where players.id = Winners.winner_id
  -- SELECT COUNT(winner_id) as PlayersWins FROM players, Matches GROUP BY Matches.winner_id;
  -- SELECT COUNT(winner_id) as PlayersWins FROM players LEFT JOIN Matches ON players.id = Matches.winner_id;
  -- SELECT COUNT(winner_id) as PlayersWins FROM Matches, players WHERE Matches.winner_id = players.id;
  -- SELECT count(matches.winner_id) AS won FROM players LEFT JOIN matches ON players.id = matches.winner_id GROUP BY players.name ORDER BY won DESC;

-- CREATE VIEW Matchescount AS
  -- SELECT COUNT(*) as MatchesPlayers FROM Matches, players where Matches.player1_id = players.id or Matches.player2_id = players.id;
  -- SELECT COUNT(winner_id) as MatchesPlayers FROM Matches, players where Matches.winner_id = players.id OR Matches.loser_id = players.id;
  -- SELECT id_match as MatchesPlayers FROM Matches, players where Matches.winner_id = players.id OR Matches.loser_id = players.id;
-- CREATE VIEW playersjoin AS
--   SELECT id, name FROM sub;
