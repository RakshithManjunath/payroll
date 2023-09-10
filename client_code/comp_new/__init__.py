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

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1.text == "":
      Notification("Company name cannot be blank").show()
    else:
      id= anvil.server.call('comp_get_next_string_value')
      compcode= anvil.server.call('next_comp_id_value')
      row = anvil.server.call('new_comp_add',id,compcode, self.text_box_1.text)
      anvil.server.call('comp_default_values',row)
      Notification(self.text_box_1.text + " data added successfully").show()
      self.clear_inputs()
    
  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = ""



