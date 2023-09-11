from ._anvil_designer import logformTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class logform(logformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    value = anvil.server.call('check_username_and_password', self.text_box_1.text, self.text_box_2.text)
    if value == True:
      open_form('company_select')

