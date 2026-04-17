import pytest
from app import app

def test_header_present():
    assert "Pink Morsel Sales Dashboard" in str(app.layout)

def test_graph_present():
    assert "Graph" in str(app.layout)

def test_radio_present():
    assert "RadioItems" in str(app.layout)
