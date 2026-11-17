import csv
import io
import json

ROWS = [{"name": "a", "qty": 1}, {"name": "b", "qty": 2}]


def rows():
    return list(ROWS)


def export_csv():
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=["name", "qty"])
    w.writeheader()
    w.writerows(ROWS)
    return buf.getvalue()


def export_json():
    return json.dumps(ROWS)
