#!/usr/bin/env python3
import io
import csv
import time
from pprint import pprint

from gdrive.clients import GClient

TMATE_DB = '1Jbsm4qCqk2-HRwA3cnT4wBRV3dnvvAQrXdqV6fBvuoA'


def update_session(gclient: GClient) -> dict:
    current_rows = gclient.get_csv_rows(fileId=TMATE_DB)
    for row in current_rows:
        if row['name'] == 'ricebox':
            row['updated_ts'] = int(time.time())
            row['url'] = 'hi'
            row['comment'] = 'sup'

    fieldnames = list(current_rows[0].keys())
    new_file = io.StringIO()

    writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(current_rows)

    results = gclient.update_file(
        fileId=TMATE_DB,
        new_file=new_file,
    )
    return results


def main() -> None:
    gclient = GClient()
    pprint(update_session(gclient))


if __name__ == '__main__':
    main()
