from ._anvil_designer import desi_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class desi_change(desi_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.drop_down_1.items = anvil.server.call('desi_change_name_and_code')

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.drop_down_1.visible=True
    self.text_box_1.visible=False

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    #self.button_1.enabled=True
    self.text_box_1.visible = True
    if self.drop_down_1.selected_value is not None:
      self.cur_desiname_and_code = self.drop_down_1.selected_value
      desiname_and_code = self.cur_desiname_and_code.split("|")
      self.text_box_1.text = desiname_and_code[1].strip()
      self.cur_desicode = desiname_and_code[0].strip()
      self.drop_down_1.visible = False
    else:
      self.button_1.enabled = False

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('desi_update_row', self.cur_desicode, 
                                       self.text_box_1.text)
    
    Notification(self.text_box_1.text + " data modified successfully").show()
    self.clear_inputs()

  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = None

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('desi')



