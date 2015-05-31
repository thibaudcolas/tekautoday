import scripts.fetch as fetch


def test_fetch_formats_timespans_properly():
    year1 = 2001
    year2 = 2002
    result = fetch.format_timespan(year1, year2)

    assert type(result) is str
    assert result == '2001+TO+2002'
