from tournament import simulate_tournament
from unittest.mock import patch


def test_simulate_tournament():
    teams = [
        {"team": "Team A", "rating": 100},
        {"team": "Team B", "rating": 50},
        {"team": "Team C", "rating": 200},
        {"team": "Team D", "rating": 150},
    ]

    # Patching random.random to always return 0.5
    with patch("random.random", return_value=0.5):
        winner = simulate_tournament(teams)
        assert winner == "Team C"  # Highest rating
