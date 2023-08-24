from ._anvil_designer import bank_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class bank_change(bank_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.drop_down_1.items = anvil.server.call('bank_change_name_and_code')

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def text_box_5_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.drop_down_1.visible=True
    self.text_box_5.visible=False


