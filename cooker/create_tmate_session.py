#!/usr/bin/env python3
import shlex
import io
import subprocess
import csv
import time
from pprint import pprint

from gdrive.clients import GClient

TMATE_DB = '1Jbsm4qCqk2-HRwA3cnT4wBRV3dnvvAQrXdqV6fBvuoA'

CMD_CREATE_SESSION = 'tmate -S /tmp/tmate.sock new-session -d'
CMD_PRINT_WEB = "tmate -S /tmp/tmate.sock display -p '#{tmate_web}'"


def update_session(gclient: GClient, url: str) -> dict:
    current_rows = gclient.get_csv_rows(fileId=TMATE_DB)
    for row in current_rows:
        if row['name'] == 'ricebox':
            row['updated_ts'] = int(time.time())
            row['url'] = url
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
    print(subprocess.run(['pkill', 'tmate']))

    print(subprocess.check_output(
        shlex.split(CMD_CREATE_SESSION),
        stderr=subprocess.STDOUT
    ))

    time.sleep(2)
    web_url = subprocess.check_output(
        shlex.split(CMD_PRINT_WEB),
        stderr=subprocess.STDOUT
    ).decode('utf-8')

    # Update
    gclient = GClient()
    pprint(update_session(gclient, url=web_url))


if __name__ == '__main__':
    main()
