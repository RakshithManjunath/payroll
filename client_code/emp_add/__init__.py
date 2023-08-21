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
    self.custom_2.visible = False
    self.custom_3.visible = False

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = not self.custom_2.visible
    self.custom_3.visible = False

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = False
    self.custom_3.visible = not self.custom_3.visible

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.radio_button_1.selected == True:
      emp_sex = "Male"
    else:
      emp_sex = "Female"

    if self.radio_button_3.selected == True:
      emp_type = "Staff"
    else:
      emp_type = "Worker"

    if self.custom_1.radio_button_1.selected == True:
      pf_contribution = True
    else:
      pf_contribution = False

    if self.custom_2.radio_button_1.selected == True:
      esi_contribution = True
    else:
      esi_contribution = False

    if self.custom_3.radio_button_1.selected == True:
      pt_contribution = True
    else:
      pt_contribution = False

    if self.custom_3.radio_button_3.selected == True:
      it_contribution = True
    else:
      it_contribution = False
    
    emp_id= anvil.server.call('emp_get_next_id_value')
    anvil.server.call('emp_add',emp_id,self.text_box_1.text,self.text_box_2.text,self.text_box_3.text,
                      self.date_picker_1.date,self.date_picker_2.date,emp_sex, emp_type,
                     pf_contribution,self.custom_1.text_box_1.text,self.custom_1.text_box_2.text,
                     esi_contribution,self.custom_2.text_box_1.text,self.custom_2.text_box_2.text,
                     pt_contribution,it_contribution, self.custom_3.text_box_1.text)