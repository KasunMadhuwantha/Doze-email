from datetime import datetime

def convert_invoice_period_format(invoice_period_input_str:str):
    input_date = datetime.strptime(invoice_period_input_str, '%Y-%m') # Convert string to datetime object
    return input_date.strftime('%B, %Y') # Format the datetime object

def generate_invoice_id():
    return 'DZN-10120'