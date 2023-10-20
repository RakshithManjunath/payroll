from ._anvil_designer import pass_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class pass_add(pass_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_5.text = gvarb.g_comname+' '+gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('pass_add')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1.text == "":
      Notification("User name cannot be blank").show()
    else:
      id= anvil.server.call('pass_get_next_string_value')
      passcode= anvil.server.call('next_pass_code_value')
      row = anvil.server.call('pass_add',id,passcode, self.text_box_1.text,
                        self.text_box_2.text,gvarb.g_comcode)
      #anvil.server.call('comp_default_values',row)
      result = confirm(self.text_box_1.text+" user successfully added ! continue to login  ?", buttons=["Yes"])
      if result == "Yes":
        self.clear_inputs()
        open_form('logform')
    
  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = ""
    self.text_box_2.text = ""
    self.text_box_3.text = ""
