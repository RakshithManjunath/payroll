from ._anvil_designer import stat_dedTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class stat_ded(stat_dedTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh()

    # Any code you write here will run before the form opens.
  def refresh(self):
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
    self.text_box_1.text = comp_details['comp_ded1']
    self.text_box_2.text = comp_details['comp_ded2']
    self.text_box_3.text = comp_details['comp_ded3']
    self.text_box_4.text = comp_details['comp_ded4']




