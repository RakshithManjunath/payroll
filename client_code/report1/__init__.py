from ._anvil_designer import report1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class report1(report1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    media_object = anvil.server.call('get_reportlab_pdf')
    download(media_object)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

