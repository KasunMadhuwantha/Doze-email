from datetime import date 
import pandas as pd 
from send_email import send_email #local python module

#public googlesheet url - not secure
SHEET_ID = "1OmQPYrEuLT38EtxNHHor7fjnTDo1cWz5lgyyPcIlho4"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}" #sametime this converts google data sheet pandas data frame

def load_df(url):
    parse_dates = ["due_date","reminder_date"]

    df = pd.read_csv(url, parse_dates=parse_dates)
    return df

def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present >= row["reminder_date"].date()) and (row["has_paid"] == "no"):
            send_email(
                subject=f'[Dozen Pvt Ltd] Invoice: {row["invoice_no"]}',
                receiver_email=row["email"],
                name=row["name"],
                due_date=row["due_date"].strftime("%d, %b %Y"), 
                invoice_no=row["invoice_no"],
                amount=row["amount"],
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"

df = load_df(URL) #loading dataframe
result = query_data_and_send_emails(df) #seeing the results as counts
print(result)

