from ._anvil_designer import emp_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class emp_change(emp_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    self.drop_down_1.items = anvil.server.call('emp_name_and_code')

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    split_list_emp = self.drop_down_1.selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    self.emp_code,self.emp_name = split_list_emp[0],split_list_emp[1]

    self.text_box_1.text = self.emp_name

    anvil.server.call('emp_get_details')
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('emp_update_row', self.emp_code, 
                                       self.text_box_1.text)
    
    Notification(self.text_box_1.text + " data modified successfully").show()



