from ._anvil_designer import dept_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class dept_change(dept_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.drop_down_1.items = anvil.server.call('dept_change_name_and_code')
    dept_comp_code = anvil.server.call('company_dept_code',gvarb.g_comcode)
    for row in dept_comp_code:
      print(row['dept_name'])

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.drop_down_1.visible=True
    self.text_box_1.visible=False

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    #self.button_1.enabled=True
    self.text_box_1.visible = True
    if self.drop_down_1.selected_value is not None:
      self.cur_deptname_and_code = self.drop_down_1.selected_value
      deptname_and_code = self.cur_deptname_and_code.split("|")
      self.text_box_1.text = deptname_and_code[1].strip()
      self.cur_deptcode = deptname_and_code[0].strip()
      self.drop_down_1.visible = False
    else:
      self.button_1.enabled = False

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1.text == "":
      Notification("Department name cannot be blank").show()
    else:
      anvil.server.call('dept_update_row', self.cur_deptcode, 
                                       self.text_box_1.text)
    
      Notification(self.text_box_1.text + " data modified successfully").show()
      self.clear_inputs()
      self.drop_down_1.visible=True

      # refresh after button submit
      self.drop_down_1.items = anvil.server.call('dept_change_name_and_code')

  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = None
  
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dept')





