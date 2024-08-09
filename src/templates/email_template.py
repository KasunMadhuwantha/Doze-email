def get_email_body(name:str, invoice_period:str, invoice_no:str, business_name:str, due_date:str, amount:str):
    return f"""\
        <html>
            <body>
                <p>Hi {name},</p>
                <p>Friendly reminder of the payment of <strong>{invoice_period}</strong> (Invoice No. {invoice_no}) for {business_name} is due on <strong>{due_date}</strong>.</p>
                <p>Please confirm your payment of <strong>LKR {amount}</strong>.</p>
                <p>Best regards,<br>Dozen Solutions Pvt Ltd</p>
            </body>
        </html>
        """