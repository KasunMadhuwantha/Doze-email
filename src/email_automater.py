#!/usr/bin/python3
import parameters as pr
import helper as hh
from connector.data_connector import open_gsheet
from send_email import send_email

if __name__ == "__main__":
    try:
        email_counter = 0
        gheet_df = open_gsheet()
        
        mail_sent_clients = []

        for _, row in gheet_df.iterrows():
            # if payment not paid
            if str(row['paid']).lower() == 'no':
                invoice_id = hh.generate_invoice_id()
                send_email(
                    subject = f'Dozen Pvt Ltd: Invoice-[{invoice_id}]',
                    receiver_email = row['email'],
                    name = row['person to address'],
                    business_name = row['business name'],
                    invoice_no = invoice_id,
                    invoice_period = hh.convert_invoice_period_format(str(row['invoice period'])),
                    due_date = row['due date'], 
                    amount = row['due amount']
                )
                mail_sent_clients.append(str(row['business name']))
                email_counter += 1
                
        print(f"Total Emails Sent: {email_counter}")

    except Exception as e:
        raise Exception(f"Exception Raised: {e}")