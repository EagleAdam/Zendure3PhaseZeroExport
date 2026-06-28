from scripts.phase_matching import distribute_power_across_phases


def test_distribute_power_basic():
    l1, l2, l3 = distribute_power_across_phases(500, 500, 500, 900)
    assert (l1, l2, l3) == (300, 300, 300)
