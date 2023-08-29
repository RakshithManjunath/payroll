from ._anvil_designer import comp_earnhead1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb


class comp_earnhead1(comp_earnhead1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
    self.label_1.text = comp_details['comp_earn_head1']
    self.label_2.text = comp_details['comp_earn_head2']    
    self.label_3.text = comp_details['comp_earn_head3']
    self.label_4.text = comp_details['comp_earn_head4']   
    self.label_5.text = comp_details['comp_earn_head5']
