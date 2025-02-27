from naas_drivers.driver import InDriver, OutDriver
from urllib.parse import urljoin
import pandas as pd
import requests
import os


BIG_NUM_TO_GETALL = 1000000


class Gsheet(InDriver, OutDriver):
    sheets_api = None
    spreadsheet_id = None
    sheet_name = None

    def __init__(self):
        self.sheets_api = os.getenv("GSHEETS_API")

    def connect(
        self,
        spreadsheet_id: str,
        api_url: str = None,
    ):
        self.spreadsheet_id = spreadsheet_id
        self.sheets_api = api_url if api_url else os.getenv("GSHEETS_API")
        self.connected = True
        return self

    def get(
        self,
        sheet_name: str,
        items_per_page: int = BIG_NUM_TO_GETALL,
    ) -> pd.DataFrame:
        self.check_connect()
        resp = requests.get(
            urljoin(self.sheets_api, f"{self.spreadsheet_id}/{sheet_name}"),
            params={"perPage": items_per_page},
        )
        resp.raise_for_status()
        data = resp.json()
        df = pd.DataFrame(data=data["data"], columns=data["columns"])
        return df

    def send(
        self, 
        data, 
        sheet_name: str, 
        append: bool = True
    ) -> str:
        self.check_connect()
        data_formated = data
        if isinstance(data, pd.DataFrame):
            data_formated = data.to_dict("records")
        
        if not append:
            cur_data = requests.get(urljoin(self.sheets_api, f"{self.spreadsheet_id}/{sheet_name}"))
            row_count = cur_data.json().get('data')[0].get('rowNumber')
            requests.delete(urljoin(self.sheets_api, f"{self.spreadsheet_id}/{sheet_name}"), json=list(range(1,row_count+1)))
            
        resp = requests.post(
            urljoin(self.sheets_api, f"{self.spreadsheet_id}/{sheet_name}"),
            json=data_formated,
        )
        resp.raise_for_status()
        return resp.json()
