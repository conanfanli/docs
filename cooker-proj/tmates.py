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


class Tmate:

    def __init__(self):
        self.client = GClient()

    def kill(self):
        return subprocess.run(['pkill', 'tmate'])

    def new_session(self):
        return subprocess.check_output(
            shlex.split(CMD_CREATE_SESSION),
            stderr=subprocess.STDOUT
        )

    def get_session_url(self):
        try:
            return subprocess.check_output(
                shlex.split(CMD_PRINT_WEB),
                stderr=subprocess.STDOUT
            ).decode('utf-8').strip()
        except subprocess.CalledProcessError:
            return None

    def _get_row(self, rows):
        return [row for row in rows if row['name'] == 'ricebox'][0]

    def update_session(self):
        rows = self.client.get_csv_rows(fileId=TMATE_DB)
        row = self._get_row(rows)

        session_url = self.get_session_url()
        if row['url'] == session_url:
            print(f'URL in sync: {session_url}')
            return None

        print('{}!={}. Restarting ...'.format(row['url'], session_url))
        self.kill()
        time.sleep(2)
        self.new_session()

        row['updated_ts'] = int(time.time())
        row['url'] = session_url
        row['comment'] = 'sup'
        print(row)

        self.update_csv(rows)

    def update_csv(self, rows) -> dict:

        fieldnames = list(rows[0].keys())
        new_file = io.StringIO()

        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

        results = self.client.update_file(
            fileId=TMATE_DB,
            new_file=new_file,
        )
        return results
