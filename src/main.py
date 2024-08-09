from fastapi import FastAPI
from fastapi.params import Body
from mangum import Mangum
from connector.data_connector import open_gsheet
from send_email import send_email
from helper import generate_invoice_id, convert_invoice_period_format

app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def health_check():
    return {
        "status" : 200,
        "message" : "Welcome to Dozen Invoice Reminder bot!"
    }

@app.post("/emails/manual")
async def send_remind_mail(request_body:dict=Body(...)):
    invoice_id = generate_invoice_id()
    send_email(
        subject = f'Dozen Pvt Ltd: Invoice-[{invoice_id}]',
        receiver_email = request_body['email'],
        name = request_body['personToAddress'],
        business_name = request_body['businessName'],
        invoice_no = invoice_id,
        invoice_period = convert_invoice_period_format(str(request_body['invoicePeriod'])),
        due_date = request_body['dueDate'], 
        amount = request_body['dueAmount']
    )

    return {
        "status" : 200,
        "message" : f"successfully sent invoice ({invoice_id}) mail to client: {request_body['businessName']}"
    }

@app.get("/emails/google_sheets")
async def send_remind_mails_from_gheets():
    mail_sent_clients = []
    gheet_df = open_gsheet()
    if gheet_df.empty:
        return {
            "status" : 200,
            "message" :"No mails sent. Empty Google sheet found."
        }

    for _, row in gheet_df.iterrows():
        # if payment not paid
        if str(row['paid']).lower() == 'no':
            invoice_id = generate_invoice_id()
            send_email(
                subject = f'Dozen Pvt Ltd: Invoice-[{invoice_id}]',
                receiver_email = row['email'],
                name = row['person to address'],
                business_name = row['business name'],
                invoice_no = invoice_id,
                invoice_period = convert_invoice_period_format(str(row['invoice period'])),
                due_date = row['due date'], 
                amount = row['due amount']
            )
            mail_sent_clients.append(str(row['business name']))

    return {
        "status" : 200,
        "message" : f"Successfully sent a total of {str(len(mail_sent_clients))} mails to clients [{', '.join(mail_sent_clients)}]"
    }