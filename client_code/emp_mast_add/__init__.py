from ._anvil_designer import emp_mast_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class emp_mast_add(emp_mast_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_4.text = gvarb.g_comname
    self.drop_down_1.items = anvil.server.call('dept_change_name_and_code')
    self.drop_down_2.items = anvil.server.call('desi_change_name_and_code')

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

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('emp_mast_add')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1.text == "" and self.text_box_2.text == "":
      Notification("Employee code & name cannot be blank").show()
    else:
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

      dept_code,dept_name,desi_code,desi_name = None,None,None,None

      # to check if any option in the dropdown is chosen, if not by default it is none
      if self.drop_down_1.selected_value!=None:
        split_list_dept = self.drop_down_1.selected_value.split("|")
        split_list_dept = [ele.strip() for ele in split_list_dept] 
        dept_code,dept_name = split_list_dept[0],split_list_dept[1]

      # to check if any option in the dropdown is chosen, if not by default it is none
      if self.drop_down_2.selected_value!=None:
        split_list_desi = self.drop_down_2.selected_value.split("|")
        split_list_desi = [ele.strip() for ele in split_list_desi] 
        desi_code,desi_name = split_list_desi[0],split_list_desi[1]
    
      emp_id= anvil.server.call('emp_get_next_id_value')
      row = anvil.server.call('emp_add',emp_id,self.text_box_1.text,self.text_box_2.text,self.text_box_3.text,
                    self.date_picker_1.date,self.date_picker_2.date,emp_sex, emp_type,
                    pf_contribution,self.custom_1.text_box_1.text,self.custom_1.text_box_2.text,
                    esi_contribution,self.custom_2.text_box_1.text,self.custom_2.text_box_2.text,
                    pt_contribution,it_contribution, self.custom_3.text_box_1.text,dept_code,dept_name,
                    desi_code,desi_name)
      anvil.server.call('emp_default_values',row)
      Notification(self.text_box_1.text + " data added successfully").show()










