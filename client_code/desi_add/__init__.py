from ._anvil_designer import desi_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class desi_add(desi_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.value= anvil.server.call('desi_get_next_string_value')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    desi_id= anvil.server.call('next_desi_id_value')
    anvil.server.call('desi_add',desi_id,self.value, self.text_box_1.text)

