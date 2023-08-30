from ._anvil_designer import month_and_year_selectTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class month_and_year_select(month_and_year_selectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    cur_trans_date = anvil.server.call('cur_trans_date')

    month_names_alphabets = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_names_numeric = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    year_names = ["2023", "2024", "2025", "2026"]

    if cur_trans_date[0].month <=9:
      month = str(cur_trans_date[0].month).zfill(2)
    else:
      month = str(cur_trans_date[0].month)
      
    self.month_db_lbl.text = month_names_alphabets[month_names_numeric.index(month)]
    self.year_db_lbl.text = cur_trans_date[0].year

    self.month_select_dp.items = month_names_alphabets
    self.year_select_dp.items = year_names

  def submit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

    
