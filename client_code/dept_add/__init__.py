from ._anvil_designer import dept_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class dept_add(dept_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.value= anvil.server.call('dept_get_next_string_value')


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1.text == "":
      Notification("Department name cannot be blank").show()
    else:
      dept_id= anvil.server.call('next_dept_id_value')
      anvil.server.call('dept_add',dept_id,self.value, self.text_box_1.text)
      Notification(self.text_box_1.text + " data added successfully").show()
      self.clear_inputs()

  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = None

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dept')


  