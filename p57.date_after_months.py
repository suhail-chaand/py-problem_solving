#Calculate the date 7 months from a date; take date input from console

from datetime import datetime
from dateutil.relativedelta import relativedelta

start_date = datetime.strptime(input('Enter start date dd-mm-yyyy: '),'%d-%m-%Y')

print('Date after 7 months:',(start_date+relativedelta(months=+7)).strftime('%d-%m-%Y'))