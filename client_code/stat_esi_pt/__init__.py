from ._anvil_designer import stat_esi_ptTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class stat_esi_pt(stat_esi_ptTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    comp_details = anvil.server.call('comp_get_details', '001')
    self.text_box_1.text = comp_details['comp_esi_sal_lt']

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('statutary_update_esi', "001", self.text_box_1.text)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('statutary')



