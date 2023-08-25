from ._anvil_designer import bank_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class bank_add(bank_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.value= anvil.server.call('bank_get_next_string_value')
    bank_id= anvil.server.call('next_bank_id_value')
    anvil.server.call('bank_add',self.value,bank_id, self.text_box_1.text,
                    self.text_box_2.text,self.text_box_3.text,self.text_box_4.text,
                    self.text_box_5.text)
    Notification(self.text_box_1.text + " data added successfully").show()
    self.clear_inputs()
    
  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = ""
    self.text_box_2.text = ""
    self.text_box_3.text = ""
    self.text_box_4.text = ""
    self.text_box_5.text = ""

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_add_change')
