from ._anvil_designer import emp_trans_attnTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class emp_trans_attn(emp_trans_attnTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)

    self.label_6.text = comp_details['comp_leave_head1']
    self.label_7.text = comp_details['comp_leave_head2']
    self.label_8.text = comp_details['comp_leave_head3']


