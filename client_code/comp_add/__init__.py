from ._anvil_designer import comp_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class comp_add(comp_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.value= anvil.server.call('comp_get_next_string_value')
    comp_id= anvil.server.call('next_comp_id_value')
    anvil.server.call('comp_add',self.value,comp_id, self.text_box_1.text,
                      self.text_box_2.text,self.text_box_3.text,self.text_box_4.text,
                      self.text_box_5.text,self.text_box_6.text,self.text_box_7.text
                      )
    self.clear_inputs()
    
  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = None
    self.text_box_2.text = None
    self.text_box_3.text = None
    self.text_box_4.text = None
    self.text_box_5.text = None
    self.text_box_6.text = None
    self.text_box_7.text = None


