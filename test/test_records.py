import src.records as records


def test_records_storage():
    assert type(records.records_hash) is dict
    assert type(records.records_date) is dict


def test_records_creation():
    assert hasattr(records.create_record, '__call__')

    record = records.create_record('test', 1)

    assert type(record) is dict
    assert len(record.keys()) == 3
    assert type(record['id']) is int
    assert type(record['date']) is str
    assert type(record['hash']) is str

    assert record['id'] == 1
    assert record['date'] == 'test'
    assert record['hash'] != 'test'


def test_records_loading():
    assert hasattr(records.load_records, '__call__')

    try:
        ret = records.load_records()
        assert ret is None
    except OSError:
        assert False

    assert len(records.records_hash) > 0
    assert len(records.records_date) > 0
