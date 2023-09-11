from ._anvil_designer import comp_newTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class comp_new(comp_newTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    month_names_alphabets = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_names_numeric = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    year_names = ["2023", "2024", "2025", "2026"]

    self.drop_down_1.items = month_names_alphabets
    self.drop_down_2.items = year_names
  
  
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()

  def update(self, initial_date):
    # Get the current month and year
    current_month = initial_date.month
    current_year = initial_date.year

    # Move to the next month
    next_month = current_month + 1 if current_month < 12 else 1
    next_year = current_year if current_month < 12 else current_year + 1

    # Calculate the initial date of the next month
    next_initial_date = datetime(next_year, next_month, 1).date()

    # Calculate the number of days in the next month
    if next_month == 2 and calendar.isleap(next_year):
        next_days = 29
    else:
        next_days = calendar.monthrange(next_year, next_month)[1]

    # Calculate the number of Sundays in the next month
    next_num_of_sundays = sum(
        1 for day in range(1, next_days + 1) if datetime(next_year, next_month, day).weekday() == 6
    )

    # Calculate the end date of the next month
    next_end_date = datetime(next_year, next_month, next_days).date()

    return next_initial_date, next_days, next_num_of_sundays, next_end_date

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1.text == "":
      Notification("Company name cannot be blank").show()
    else:
      id= anvil.server.call('comp_get_next_string_value')
      compcode= anvil.server.call('next_comp_id_value')
      row = anvil.server.call('new_comp_add',id,compcode, self.text_box_1.text)
      tr_id = 1

      next_initial_date, next_days, next_num_of_sundays, next_end_date = self.update(self.date_picker_1.date)
      print("", next_initial_date)
      

      # anvil.server.call('new_comp_trans_date_add',tr_id,self.date_picker_1.date)
      # anvil.server.call('comp_default_values',row)
      # Notification(self.text_box_1.text + " data added successfully").show()
      # self.clear_inputs()
      # anvil.users.logout()
      # open_form('company_select')
      # anvil.users.login_with_form()
    
  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = ""



