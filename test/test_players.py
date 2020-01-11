import unittest
from basketball_reference_scraper.players import get_stats

class TestPlayers(unittest.TestCase):
    def test_get_stats(self):
        expected_columns = ['SEASON', 'AGE', 'TEAM', 'LEAGUE', 'POS', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
        df = get_stats('LaMarcus Aldridge') 
        self.assertCountEqual(list(df.columns), expected_columns)

        df = get_stats('LaMarcus Aldridge', career=True)
        expected_columns = ['SEASON', 'TEAM', 'LEAGUE', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
        self.assertCountEqual(list(df.columns), expected_columns)

        df = get_stats('LaMarcus Aldridge', playoffs=True, career=True)
        self.assertCountEqual(list(df.columns), expected_columns)


if __name__ == '__main__':
    unittest.main()
