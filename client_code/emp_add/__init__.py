from ._anvil_designer import emp_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class emp_add(emp_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = not self.custom_1.visible

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_2.visible = not self.custom_2.visible

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_3.visible = not self.custom_3.visible



