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

  earnhead1_pf = None
  earnhead1_esi = None
  earnhead1_pt = None
  earnhead1_it = None
  earnhead1_ot = None
  earnhead1_bonus = None

  earnhead2_pf = None
  earnhead2_esi = None
  earnhead2_pt = None
  earnhead2_it = None
  earnhead2_ot = None
  earnhead2_bonus = None

  earnhead3_pf = None
  earnhead3_esi = None
  earnhead3_pt = None
  earnhead3_it = None
  earnhead3_ot = None
  earnhead3_bonus = None

  earnhead4_pf = None
  earnhead4_esi = None
  earnhead4_pt = None
  earnhead4_it = None
  earnhead4_ot = None
  earnhead4_bonus = None

  earnhead5_pf = None
  earnhead5_esi = None
  earnhead5_pt = None
  earnhead5_it = None
  earnhead5_ot = None
  earnhead5_bonus = None

  earnhead6_pf = None
  earnhead6_esi = None
  earnhead6_pt = None
  earnhead6_it = None
  earnhead6_ot = None
  earnhead6_bonus = None

  earnhead7_pf = None
  earnhead7_esi = None
  earnhead7_pt = None
  earnhead7_it = None
  earnhead7_ot = None
  earnhead7_bonus = None

  earnhead8_pf = None
  earnhead8_esi = None
  earnhead8_pt = None
  earnhead8_it = None
  earnhead8_ot = None
  earnhead8_bonus = None

  earnhead9_pf = None
  earnhead9_esi = None
  earnhead9_pt = None
  earnhead9_it = None
  earnhead9_ot = None
  earnhead9_bonus = None

  earnhead10_pf = None
  earnhead10_esi = None
  earnhead10_pt = None
  earnhead10_it = None
  earnhead10_ot = None
  earnhead10_bonus = None
  
  bonus_pt_included = None
 
  for row in data_table:
    if row['comp_earnhead1_pf'] == False:
      ehead1_pf = 0
    elif row['comp_earnhead1_pf'] == True:
      ehead1_pf = 1
    elif row['comp_earnhead1_pf'] == None:
      ehead1_pf = 0
      
    if row['comp_earnhead1_esi'] == False:
      ehead1_esi = 0
    elif row['comp_earnhead1_esi'] == True:
      ehead1_esi = 1
    elif row['comp_earnhead1_esi'] == None:
      ehead1_esi = 0  

    if row['comp_earnhead1_pt'] == False:
      ehead1_pt = 0
    elif row['comp_earnhead1_pt'] == True:
      ehead1_pt = 1
    elif row['comp_earnhead1_pt'] == None:
      ehead1_pt = 0 
      
    if row['comp_earnhead1_it'] == False:
      ehead1_it = 0
    elif row['comp_earnhead1_it'] == True:
      ehead1_it = 1
    elif row['comp_earnhead1_it'] == None:
      ehead1_it = 0

    if row['comp_earnhead1_ot'] == False:
      ehead1_ot = 0
    elif row['comp_earnhead1_ot'] == True:
      ehead1_ot = 1
    elif row['comp_earnhead1_ot'] == None:
      ehead1_ot = 0   

    if row['comp_earnhead1_bonus'] == False:
      ehead1_bonus = 0
    elif row['comp_earnhead1_bonus'] == True:
      ehead1_bonus = 1
    elif row['comp_earnhead1_bonus'] == None:
      ehead1_bonus = 0    


    if row['comp_earnhead2_pf'] == False:
      ehead2_pf = 0
    elif row['comp_earnhead2_pf'] == True:
      ehead2_pf = 1
    elif row['comp_earnhead2_pf'] == None:
      ehead2_pf = 0
      
    if row['comp_earnhead2_esi'] == False:
      ehead2_esi = 0
    elif row['comp_earnhead2_esi'] == True:
      ehead2_esi = 1
    elif row['comp_earnhead2_esi'] == None:
      ehead2_esi = 0  

    if row['comp_earnhead2_pt'] == False:
      ehead2_pt = 0
    elif row['comp_earnhead2_pt'] == True:
      ehead2_pt = 1
    elif row['comp_earnhead2_pt'] == None:
      ehead2_pt = 0 
      
    if row['comp_earnhead2_it'] == False:
      ehead2_it = 0
    elif row['comp_earnhead2_it'] == True:
      ehead2_it = 1
    elif row['comp_earnhead2_it'] == None:
      ehead2_it = 0

    if row['comp_earnhead2_ot'] == False:
      ehead2_ot = 0
    elif row['comp_earnhead2_ot'] == True:
      ehead2_ot = 1
    elif row['comp_earnhead2_ot'] == None:
      ehead2_ot = 0   

    if row['comp_earnhead2_bonus'] == False:
      ehead2_bonus = 0
    elif row['comp_earnhead2_bonus'] == True:
      ehead2_bonus = 1
    elif row['comp_earnhead2_bonus'] == None:
      ehead2_bonus = 0    


    if row['comp_earnhead3_pf'] == False:
      ehead3_pf = 0
    elif row['comp_earnhead3_pf'] == True:
      ehead3_pf = 1
    elif row['comp_earnhead3_pf'] == None:
      ehead3_pf = 0
      
    if row['comp_earnhead3_esi'] == False:
      ehead3_esi = 0
    elif row['comp_earnhead3_esi'] == True:
      ehead3_esi = 1
    elif row['comp_earnhead3_esi'] == None:
      ehead3_esi = 0  

    if row['comp_earnhead3_pt'] == False:
      ehead3_pt = 0
    elif row['comp_earnhead3_pt'] == True:
      ehead3_pt = 1
    elif row['comp_earnhead3_pt'] == None:
      ehead3_pt = 0 
      
    if row['comp_earnhead3_it'] == False:
      ehead3_it = 0
    elif row['comp_earnhead3_it'] == True:
      ehead3_it = 1
    elif row['comp_earnhead3_it'] == None:
      ehead3_it = 0

    if row['comp_earnhead3_ot'] == False:
      ehead3_ot = 0
    elif row['comp_earnhead3_ot'] == True:
      ehead3_ot = 1
    elif row['comp_earnhead3_ot'] == None:
      ehead3_ot = 0   

    if row['comp_earnhead3_bonus'] == False:
      ehead3_bonus = 0
    elif row['comp_earnhead3_bonus'] == True:
      ehead3_bonus = 1
    elif row['comp_earnhead3_bonus'] == None:
      ehead3_bonus = 0    


    if row['comp_earnhead4_pf'] == False:
      ehead4_pf = 0
    elif row['comp_earnhead4_pf'] == True:
      ehead4_pf = 1
    elif row['comp_earnhead4_pf'] == None:
      ehead4_pf = 0
      
    if row['comp_earnhead4_esi'] == False:
      ehead4_esi = 0
    elif row['comp_earnhead4_esi'] == True:
      ehead4_esi = 1
    elif row['comp_earnhead4_esi'] == None:
      ehead4_esi = 0  

    if row['comp_earnhead4_pt'] == False:
      ehead4_pt = 0
    elif row['comp_earnhead4_pt'] == True:
      ehead4_pt = 1
    elif row['comp_earnhead4_pt'] == None:
      ehead4_pt = 0 
      
    if row['comp_earnhead4_it'] == False:
      ehead4_it = 0
    elif row['comp_earnhead4_it'] == True:
      ehead4_it = 1
    elif row['comp_earnhead4_it'] == None:
      ehead4_it = 0

    if row['comp_earnhead4_ot'] == False:
      ehead4_ot = 0
    elif row['comp_earnhead4_ot'] == True:
      ehead4_ot = 1
    elif row['comp_earnhead4_ot'] == None:
      ehead4_ot = 0   

    if row['comp_earnhead4_bonus'] == False:
      ehead4_bonus = 0
    elif row['comp_earnhead4_bonus'] == True:
      ehead4_bonus = 1
    elif row['comp_earnhead4_bonus'] == None:
      ehead4_bonus = 0    

    if row['comp_earnhead5_pf'] == False:
      ehead5_pf = 0
    elif row['comp_earnhead5_pf'] == True:
      ehead5_pf = 1
    elif row['comp_earnhead5_pf'] == None:
      ehead5_pf = 0
      
    if row['comp_earnhead5_esi'] == False:
      ehead5_esi = 0
    elif row['comp_earnhead5_esi'] == True:
      ehead5_esi = 1
    elif row['comp_earnhead5_esi'] == None:
      ehead5_esi = 0  

    if row['comp_earnhead5_pt'] == False:
      ehead5_pt = 0
    elif row['comp_earnhead5_pt'] == True:
      ehead5_pt = 1
    elif row['comp_earnhead5_pt'] == None:
      ehead5_pt = 0 
      
    if row['comp_earnhead5_it'] == False:
      ehead5_it = 0
    elif row['comp_earnhead5_it'] == True:
      ehead5_it = 1
    elif row['comp_earnhead5_it'] == None:
      ehead5_it = 0

    if row['comp_earnhead5_ot'] == False:
      ehead5_ot = 0
    elif row['comp_earnhead5_ot'] == True:
      ehead5_ot = 1
    elif row['comp_earnhead5_ot'] == None:
      ehead5_ot = 0   

    if row['comp_earnhead5_bonus'] == False:
      ehead5_bonus = 0
    elif row['comp_earnhead5_bonus'] == True:
      ehead5_bonus = 1
    elif row['comp_earnhead5_bonus'] == None:
      ehead5_bonus = 0    


    if row['comp_earnhead6_pf'] == False:
      ehead6_pf = 0
    elif row['comp_earnhead6_pf'] == True:
      ehead6_pf = 1
    elif row['comp_earnhead6_pf'] == None:
      ehead6_pf = 0
      
    if row['comp_earnhead6_esi'] == False:
      ehead6_esi = 0
    elif row['comp_earnhead6_esi'] == True:
      ehead6_esi = 1
    elif row['comp_earnhead6_esi'] == None:
      ehead6_esi = 0  

    if row['comp_earnhead6_pt'] == False:
      ehead6_pt = 0
    elif row['comp_earnhead6_pt'] == True:
      ehead6_pt = 1
    elif row['comp_earnhead6_pt'] == None:
      ehead6_pt = 0 
      
    if row['comp_earnhead6_it'] == False:
      ehead6_it = 0
    elif row['comp_earnhead6_it'] == True:
      ehead6_it = 1
    elif row['comp_earnhead6_it'] == None:
      ehead6_it = 0

    if row['comp_earnhead6_ot'] == False:
      ehead6_ot = 0
    elif row['comp_earnhead6_ot'] == True:
      ehead6_ot = 1
    elif row['comp_earnhead6_ot'] == None:
      ehead6_ot = 0   

    if row['comp_earnhead6_bonus'] == False:
      ehead6_bonus = 0
    elif row['comp_earnhead6_bonus'] == True:
      ehead6_bonus = 1
    elif row['comp_earnhead6_bonus'] == None:
      ehead6_bonus = 0    

    if row['comp_earnhead7_pf'] == False:
      ehead7_pf = 0
    elif row['comp_earnhead7_pf'] == True:
      ehead7_pf = 1
    elif row['comp_earnhead7_pf'] == None:
      ehead7_pf = 0
      
    if row['comp_earnhead7_esi'] == False:
      ehead7_esi = 0
    elif row['comp_earnhead7_esi'] == True:
      ehead7_esi = 1
    elif row['comp_earnhead7_esi'] == None:
      ehead7_esi = 0  

    if row['comp_earnhead7_pt'] == False:
      ehead7_pt = 0
    elif row['comp_earnhead7_pt'] == True:
      ehead7_pt = 1
    elif row['comp_earnhead7_pt'] == None:
      ehead7_pt = 0 
      
    if row['comp_earnhead7_it'] == False:
      ehead7_it = 0
    elif row['comp_earnhead7_it'] == True:
      ehead7_it = 1
    elif row['comp_earnhead7_it'] == None:
      ehead7_it = 0

    if row['comp_earnhead7_ot'] == False:
      ehead7_ot = 0
    elif row['comp_earnhead7_ot'] == True:
      ehead7_ot = 1
    elif row['comp_earnhead7_ot'] == None:
      ehead7_ot = 0   

    if row['comp_earnhead7_bonus'] == False:
      ehead7_bonus = 0
    elif row['comp_earnhead7_bonus'] == True:
      ehead7_bonus = 1
    elif row['comp_earnhead7_bonus'] == None:
      ehead7_bonus = 0 

    if row['comp_earnhead8_pf'] == False:
      ehead8_pf = 0
    elif row['comp_earnhead8_pf'] == True:
      ehead8_pf = 1
    elif row['comp_earnhead8_pf'] == None:
      ehead8_pf = 0
      
    if row['comp_earnhead8_esi'] == False:
      ehead8_esi = 0
    elif row['comp_earnhead8_esi'] == True:
      ehead8_esi = 1
    elif row['comp_earnhead8_esi'] == None:
      ehead8_esi = 0  

    if row['comp_earnhead8_pt'] == False:
      ehead8_pt = 0
    elif row['comp_earnhead8_pt'] == True:
      ehead8_pt = 1
    elif row['comp_earnhead8_pt'] == None:
      ehead8_pt = 0 
      
    if row['comp_earnhead8_it'] == False:
      ehead8_it = 0
    elif row['comp_earnhead8_it'] == True:
      ehead8_it = 1
    elif row['comp_earnhead8_it'] == None:
      ehead8_it = 0

    if row['comp_earnhead8_ot'] == False:
      ehead8_ot = 0
    elif row['comp_earnhead8_ot'] == True:
      ehead8_ot = 1
    elif row['comp_earnhead8_ot'] == None:
      ehead8_ot = 0   

    if row['comp_earnhead8_bonus'] == False:
      ehead8_bonus = 0
    elif row['comp_earnhead8_bonus'] == True:
      ehead8_bonus = 1
    elif row['comp_earnhead8_bonus'] == None:
      ehead8_bonus = 0 

    if row['comp_earnhead9_pf'] == False:
      ehead9_pf = 0
    elif row['comp_earnhead9_pf'] == True:
      ehead9_pf = 1
    elif row['comp_earnhead9_pf'] == None:
      ehead9_pf = 0
      
    if row['comp_earnhead9_esi'] == False:
      ehead9_esi = 0
    elif row['comp_earnhead9_esi'] == True:
      ehead9_esi = 1
    elif row['comp_earnhead9_esi'] == None:
      ehead9_esi = 0  

    if row['comp_earnhead9_pt'] == False:
      ehead9_pt = 0
    elif row['comp_earnhead9_pt'] == True:
      ehead9_pt = 1
    elif row['comp_earnhead9_pt'] == None:
      ehead9_pt = 0 
      
    if row['comp_earnhead9_it'] == False:
      ehead9_it = 0
    elif row['comp_earnhead9_it'] == True:
      ehead9_it = 1
    elif row['comp_earnhead9_it'] == None:
      ehead9_it = 0

    if row['comp_earnhead9_ot'] == False:
      ehead9_ot = 0
    elif row['comp_earnhead9_ot'] == True:
      ehead9_ot = 1
    elif row['comp_earnhead9_ot'] == None:
      ehead9_ot = 0   

    if row['comp_earnhead9_bonus'] == False:
      ehead9_bonus = 0
    elif row['comp_earnhead9_bonus'] == True:
      ehead9_bonus = 1
    elif row['comp_earnhead9_bonus'] == None:
      ehead9_bonus = 0 

    if row['comp_earnhead10_pf'] == False:
      ehead10_pf = 0
    elif row['comp_earnhead10_pf'] == True:
      ehead10_pf = 1
    elif row['comp_earnhead10_pf'] == None:
      ehead10_pf = 0
      
    if row['comp_earnhead10_esi'] == False:
      ehead10_esi = 0
    elif row['comp_earnhead10_esi'] == True:
      ehead10_esi = 1
    elif row['comp_earnhead10_esi'] == None:
      ehead10_esi = 0  

    if row['comp_earnhead10_pt'] == False:
      ehead10_pt = 0
    elif row['comp_earnhead10_pt'] == True:
      ehead10_pt = 1
    elif row['comp_earnhead10_pt'] == None:
      ehead10_pt = 0 
      
    if row['comp_earnhead10_it'] == False:
      ehead10_it = 0
    elif row['comp_earnhead10_it'] == True:
      ehead10_it = 1
    elif row['comp_earnhead10_it'] == None:
      ehead10_it = 0

    if row['comp_earnhead10_ot'] == False:
      ehead10_ot = 0
    elif row['comp_earnhead10_ot'] == True:
      ehead10_ot = 1
    elif row['comp_earnhead10_ot'] == None:
      ehead10_ot = 0   

    if row['comp_earnhead10_bonus'] == False:
      ehead10_bonus = 0
    elif row['comp_earnhead10_bonus'] == True:
      ehead10_bonus = 1
    elif row['comp_earnhead10_bonus'] == None:
      ehead10_bonus = 0    
    
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