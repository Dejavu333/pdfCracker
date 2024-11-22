import PyPDF2
from datetime import datetime, timedelta

def generate_date_passwords(start_date, end_date):
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y%m%d'))
        current_date += timedelta(days=1)
    return date_list

def unlock_pdf(pdf_path, passwords):
    for password in passwords:
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                if reader.decrypt(password):
                    print(f'Success! The password is: {password}')
                    return True
        except Exception as e:
            print(f'Error: {e}')
    print('Failed to unlock the PDF.')
    return False

# Define the range of dates to try
start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 11, 22)

# Generate the list of passwords
passwords = generate_date_passwords(start_date, end_date)

# Path to the PDF file
pdf_path = 'Vasvári Botond.pdf'

# Attempt to unlock the PDF
unlock_pdf(pdf_path, passwords)