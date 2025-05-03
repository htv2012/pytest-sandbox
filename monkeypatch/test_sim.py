from types import SimpleNamespace
from unittest import mock

import pytest


class VenueController:
    def __init__(self):
        self.venue_config = SimpleNamespace(sim={})


class SIM:
    def __init__(self, venue_controller: VenueController):
        if venue_controller.venue_config.sim is None:
            raise ValueError("No SIM venue_configuration found")
        self.venue_controller = venue_controller


def test_sim(monkeypatch):
    vc = VenueController()
    monkeypatch.setattr(vc.venue_config, "sim", None)
    with pytest.raises(ValueError, match="No SIM venue_configuration"):
        SIM(vc)


def test_sim_using_patch():
    vc = VenueController()
    with mock.patch.object(vc.venue_config, "sim", None):
        with pytest.raises(ValueError, match="No SIM venue_configuration"):
            SIM(vc)


def test_sim_using_mock():
    vc = mock.Mock()
    vc.venue_config.sim = None
    with pytest.raises(ValueError, match="No SIM venue_configuration"):
        SIM(vc)
