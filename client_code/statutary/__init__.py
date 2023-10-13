from ._anvil_designer import statutaryTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class statutary(statutaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_1.text = gvarb.g_comname+' '+gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = not self.custom_1.visible
    self.custom_2.visible = False
    self.custom_3.visible = False
    self.custom_4.visible = False

    self.custom_1.refresh()

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = not self.custom_2.visible
    self.custom_3.visible = False
    self.custom_4.visible = False

    self.custom_2.refresh()

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = False
    self.custom_3.visible = not self.custom_3.visible
    self.custom_4.visible = False

    self.custom_3.refresh()
    
  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = False
    self.custom_3.visible = False
    self.custom_4.visible = not self.custom_4.visible

    self.custom_4.refresh()

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('statutary_update_pf', gvarb.g_comcode, 
                      self.text_box_2.text,
                      self.text_box_3.text, 
                      self.text_box_4.text,
                      self.text_box_5.text, 
                      self.text_box_7.text,
                      self.text_box_8.text)



   




