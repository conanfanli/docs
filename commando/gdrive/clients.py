#!/usr/bin/env python3
import httplib2
import os
import argparse
from pprint import pprint

from googleapiclient.discovery import Resource
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'


class GClient:

    def __init__(self) -> None:
        self.credentials = GClient.get_credentials()
        self.service = GClient.get_service(self.credentials)

    @staticmethod
    def get_service(credentials=None) -> Resource:
        if not credentials:
            credentials = GClient.get_credentials()

        http = credentials.authorize(httplib2.Http())
        service = discovery.build('drive', 'v3', http=http)
        return service

    @staticmethod
    def get_credentials() -> client.OAuth2Credentials:
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'drive-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)

            print('Storing credentials to ' + credential_path)
        return credentials

    def list_files(self,
                   *,
                   pageSize: int=20,
                   fields: str='nextPageToken, files(id, name)'
                   ):
        return self.service.files().list(
            pageSize=pageSize
        ).execute()


def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    gclient = GClient()
    results = gclient.list_files()
    pprint(results)


if __name__ == '__main__':
    main()
