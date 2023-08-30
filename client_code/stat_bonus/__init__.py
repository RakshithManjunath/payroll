from ._anvil_designer import stat_bonusTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class stat_bonus(stat_bonusTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.drop_down_1.items = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    self.drop_down_2.items = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('statutary')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.radio_button_1.selected == True:
      pt_bonus_amount_included = True
    else:
      pt_bonus_amount_included = False
      
    anvil.server.call('stat_bonus_update', gvarb.g_comcode, self.drop_down_1.selected_value,
                      self.drop_down_2.selected_value, self.text_box_1.text, self.text_box_2.text,
                      pt_bonus_amount_included)

    


