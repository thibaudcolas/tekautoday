import src.records as records


def test_records_are_stored_by_hash():
    assert type(records.records_hash) is dict
