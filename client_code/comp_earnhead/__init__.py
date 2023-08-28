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
    self.text_box_1.text = comp_details['comp_earn_head1']
    self.text_box_3.text = comp_details['comp_earn_head2']
    self.text_box_5.text = comp_details['comp_earn_head3']
    self.text_box_7.text = comp_details['comp_earn_head4']
    self.text_box_9.text = comp_details['comp_earn_head5']
    self.text_box_11.text = comp_details['comp_earn_head6']

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('comp_more')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('comp_more_update_earnhead', gvarb.g_comcode, self.text_box_1.text,
                     self.text_box_3.text,self.text_box_5.text,
                     self.text_box_7.text,self.text_box_9.text,
                     self.text_box_11.text)


