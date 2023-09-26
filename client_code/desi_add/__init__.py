from ._anvil_designer import desi_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class desi_add(desi_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1.text == "":
      Notification("Designation name cannot be blank").show()
    else:
      self.value= anvil.server.call('desi_get_next_string_value')
      desi_id= anvil.server.call('next_desi_id_value')
      anvil.server.call('desi_add',desi_id,self.value, self.text_box_1.text,gvarb.g_comcode)
      Notification(self.text_box_1.text + " data added successfully").show()
      self.clear_inputs()

  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = None

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('desi')
