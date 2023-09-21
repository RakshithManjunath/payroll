import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import file_path

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
#
@anvil.server.callable
def just_test():
  # Access the data table
  cols = app_tables.transaction.list_columns()

  #print(cols)
  
  # # Specify the field name you want to check for
  field_name = 'xxxx'
  field_type = 'bool'

  for col in cols:
    if ((col["name"] == field_name) and (col["type"] == field_type)):
      print(col["name"])
      print(col["type"])
    else:
      pass
    #      print("fail")
    
    # 'type': 'number' for numeric
    # 'type': 'string' for text
    # 'type': 'bool' for logical
    # 'type': 'date' for date

    #  # field_type = anvil.server.app_tables.transaction.TextColumnType()  # You can choose the appropriate column type (e.g., Text, Date, Number)
  #    app_tables.transaction.add_column(field_name, field_type)
  
    # # Get a list of all column names in the data table
    #   # all_column_names = data_table.get_columns()
    #   all_column_names = cols(0)
  
  
@anvil.server.callable
def test_add_column():
  app_tables.transaction.update(columns={"age": int},all=True)

@anvil.server.callable
def get_all_test_columns():
  data_table = app_tables.test_table.search()
  csv_rows = []

  gender_val = None
  for row in data_table:
    if row['gender'] == False:
      gender_val = 0
    elif row['gender'] == True:
      gender_val = 1
    elif row['gender'] == None:
      gender_val = 0
    csv_row = ["[496577,781197072]",row['name'],row['age'],row['salary'],gender_val,row['dob']]  
    csv_rows.append(csv_row)

  df = pd.DataFrame(csv_rows, columns=["ID","name","age","salary","gender","dob"])
  df.to_csv('/tmp/test_table.csv',index=False)
  df_media = anvil.media.from_file('/tmp/test_table.csv', 'csv', 'test_table.csv')
  return df_media

@anvil.server.callable
def import_test_csv():
  with open(file_path.test_path, "r") as f:
    dtype_mapping = {
      'name':str,
      'age':int,
      'salary':float,
      'gender':bool
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    df['dob'] = pd.to_datetime(df['dob']).dt.date
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.test_table.add_row(**d)