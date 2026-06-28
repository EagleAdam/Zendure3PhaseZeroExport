from scripts.export_limit import compute_export_limit


def test_no_export_needed_when_importing():
    assert compute_export_limit(100, 0) == 0


def test_excess_export_is_offset():
    # Exporting 500 W, max allowed 100 W → offset 400 W
    assert compute_export_limit(-500, 100) == 400
