import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
from datetime import datetime,date
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
from temp_invoice import my_temp # import the template
from invoice_data import *  # get all data required for invoice

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42

############ trans change #############
@anvil.server.callable
def trans_change_update(trans_empid,trans_mandays,trans_wo,trans_ph,trans_layoff,trans_absent,
                        trans_leave1,trans_leave2,trans_leave3,trans_othrs,trans_inchrs,
                        trans_ded1,trans_ded2,trans_ded3,trans_ded4,
                        trans_loan1,trans_loan2,
                        trans_adv,trans_tds,trans_pfvol,trans_lic,
                        trans_arr_esipt,trans_arr_pf,trans_paid_days):
  row = app_tables.transaction.get(trans_empid=trans_empid)
  row.update(trans_mandays=trans_mandays,
            trans_wo=trans_wo,
            trans_ph=trans_ph,
            trans_layoff=trans_layoff,
            trans_absent=trans_absent,
            trans_leave1=trans_leave1,
            trans_leave2=trans_leave2,
            trans_leave3=trans_leave3,
            trans_othrs=trans_othrs,
            trans_inchrs=trans_inchrs,
            trans_ded1=trans_ded1,
            trans_ded2=trans_ded2,
            trans_ded3=trans_ded3,
            trans_ded4=trans_ded4,
            trans_loan1=trans_loan1,
            trans_loan2=trans_loan2,
            trans_adv=trans_adv,
            trans_tds=trans_tds,
            trans_pfvol=trans_pfvol,
            trans_lic=trans_lic,
            trans_arr_esipt=trans_arr_esipt,
            trans_arr_pf=trans_arr_pf,
            trans_paid_days=trans_paid_days
            )

@anvil.server.callable
def trans_emp_name_and_code(trans_comp_code):
  emp_details = []
  for r in app_tables.transaction.search(trans_comp_code=trans_comp_code):
    emp_details.append(r['trans_empid'] + " | "  +r['trans_empname'])
  return emp_details

@anvil.server.callable
def trans_emp_get_details(trans_empid):
  row = app_tables.transaction.get(trans_empid=trans_empid)
  return row

@anvil.server.callable
def trans_emp_delete_row(trans_empid,trans_comp_code):
  row = app_tables.transaction.search(trans_empid=trans_empid,trans_comp_code=trans_comp_code)
  row[0].delete()

@anvil.server.callable
def trans_get_all_details(trans_comp_code):
  trans_all_data = app_tables.transaction.search(trans_comp_code=trans_comp_code)
  # df = pd.DataFrame(trans_all_data)
  # columns_and_type = app_tables.transaction.list_columns()
  # column_names = []
  # for column in columns_and_type:
  #   column_names.append(column['name'])
  # df.columns = column_names
  # formatted_date_column = []
  # for record in trans_all_data:
  #   formatted_date = record['trans_empdob'].strftime('%d/%m/%Y')
  #   formatted_date_column.append(formatted_date)
  # df['trans_empdob'] = formatted_date_column
  # print(df, type(trans_all_data))
  # data = df.to_dict(orient='records')
  # return data
  return app_tables.transaction.search(trans_comp_code=trans_comp_code)

@anvil.server.callable
def get_all_companies():
  return app_tables.company.search()

@anvil.server.callable
def get_all_password():
  return app_tables.password.search()

@anvil.server.callable
def get_reportlab_pdf():
  my_path='my_pdf.pdf' 
  c = canvas.Canvas(my_path,pagesize=letter)
  c=my_temp(c) # run the template
  
  c.setFillColorRGB(0,0,1) # font colour
  c.setFont("Helvetica", 20)
  row_gap=0.6 # gap between each row
  line_y=7.9 # location of fist Y position 
  total=0
  employee_data = app_tables.employee.search()
  for row in employee_data:
    c.drawString(0.1*inch,line_y*inch,row['emp_code']) # p Name
    c.drawRightString(3*inch,line_y*inch,row['emp_name']) # p Price
    # c.drawRightString(6.7*inch,line_y*inch,str(my_sale[items])) # p Qunt 
    line_y=line_y-row_gap
  
  c.showPage()
  c.save()
  pdf_media = anvil.media.from_file(my_path, 'application/pdf', 'my_pdf.pdf')
  return pdf_media

