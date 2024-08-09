import pandas as pd
import gspread
from configuration import config

def open_gsheet() -> pd.DataFrame:
    g_client = gspread.service_account(filename=config.GSHEET_CREDS_PATH)

    spreadsheet = g_client.open_by_url(config.SPREADSHEET_URL)
    # spreadsheet = gc.open(config.SPREADSHEET_NAME)

    # available worksheets
    # worksheets = spreadsheet.worksheets()

    # select worksheet
    worksheet = spreadsheet.worksheet(config.WORKSHEET_NAME)

    data = worksheet.get_all_values() # get_all_values() method reads the sheet as a list of lists
    headers = data.pop(0) # column names

    df = pd.DataFrame(data, columns=headers)

    return df

if __name__ == "__main__":
    df = open_gsheet()
    print(df.head())