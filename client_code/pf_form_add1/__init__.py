from ._anvil_designer import pf_form_add1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class pf_form_add1(pf_form_add1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  # def radio_button_1_clicked(self, **event_args):
  #   """This method is called when this radio button is selected"""
  #   self.text_box_1.enabled = True
  #   self.text_box_2.enabled = True

  # def radio_button_2_clicked(self, **event_args):
  #   """This method is called when this radio button is selected"""
  #   self.text_box_1.enabled = False
  #   self.text_box_2.enabled = False


