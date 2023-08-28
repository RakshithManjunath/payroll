from ._anvil_designer import comp_earnheadTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class comp_earnhead(comp_earnheadTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
    self.text_box_2.text = comp_details['comp_emp_pfrate']

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('comp_more')

