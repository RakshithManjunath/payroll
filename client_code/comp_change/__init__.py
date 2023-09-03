from ._anvil_designer import comp_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class comp_change(comp_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.drop_down_1.items = anvil.server.call('comp_change_name_and_code')

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    self.text_box_7.visible = True
    if self.drop_down_1.selected_value is not None:
      split_list_comp = self.drop_down_1.selected_value.split("|")
      split_list_comp = [ele.strip() for ele in split_list_comp] 
      self.comp_code,self.comp_name = split_list_comp[0],split_list_comp[1]
  
      self.row = anvil.server.call('comp_get_details',self.comp_code)
  
      self.text_box_1.text = self.row['comp_addr1']
      self.text_box_2.text = self.row['comp_addr2']
      self.text_box_3.text = self.row['comp_addr3']
      self.text_box_4.text = self.row['comp_pf_number']
      self.text_box_5.text = self.row['comp_esi_number']
      self.text_box_6.text = self.row['comp_pto_circle']
      self.text_box_7.text = self.comp_name
      self.drop_down_1.visible = False
    else:
      self.button_1.enabled = False
   # self.text_box_5.text = self.bank_name

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_7.text == "":
      Notification("Company name cannot be blank").show()
    else:
      anvil.server.call('comp_update',self.comp_code,
      self.text_box_1.text, self.text_box_2.text,
      self.text_box_3.text,self.text_box_4.text,
      self.text_box_5.text,self.text_box_6.text,
      self.text_box_7.text)
    
    self.clear_inputs()
    self.drop_down_1.visible=True
    # refresh after button submit
    self.drop_down_1.items = anvil.server.call('comp_change_name_and_code')

  def clear_inputs(self):
    self.text_box_1.text = None
    self.text_box_2.text = None
    self.text_box_3.text = None
    self.text_box_4.text = None
    self.text_box_5.text = None
    self.text_box_6.text = None
    self.text_box_7.text = None
  

  def text_box_7_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.drop_down_1.visible = True
    self.text_box_7.visible = False

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('comp_add_change')





