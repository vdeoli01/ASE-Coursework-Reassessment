from tournament import simulate_tournament, main
from unittest.mock import patch
import sys
from contextlib import redirect_stdout
import io


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


def test_main():
    filename = "test-teams.csv"
    # Simulate command-line argument
    sys.argv = ["tournament.py", filename]

    # Capture output
    io_stream = io.StringIO()
    with redirect_stdout(io_stream):
        # Patching random.random to always return 0.5
        with patch("random.random", return_value=0.5):
            main()
    main_output = io_stream.getvalue()
    print(main_output)

    assert "Prob of T1 beating T2 is 0.54782" in main_output
    assert "T1: 100.0% chance of winning" in main_output
