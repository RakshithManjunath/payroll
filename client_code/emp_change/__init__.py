from ._anvil_designer import emp_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class emp_change(emp_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_10.text = gvarb.g_comname

    # self.drop_down_1.items = anvil.server.call('emp_name_and_code',gvarb.g_comcode)
    print(type(anvil.server.call('comp_wise_emp_code_and_name', gvarb.g_comcode)))
    print(anvil.server.call('comp_wise_emp_code_and_name', gvarb.g_comcode))
    self.drop_down_1.items = anvil.server.call('comp_wise_emp_code_and_name', gvarb.g_comcode)

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    split_list_emp = self.drop_down_1.selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    self.emp_code,self.emp_name = split_list_emp[0],split_list_emp[1]

    self.row = anvil.server.call('emp_get_details',self.emp_code,gvarb.g_comcode)
    
    self.text_box_1.text = self.emp_name
    self.text_box_2.text = self.row['emp_hus_name']
    self.emp_sex = self.row['emp_sex']
    if self.emp_sex == "Male":
      self.radio_button_1.selected = True
      self.radio_button_2.selected = False
    else:
      self.radio_button_2.selected = True
      self.radio_button_1.selected = False

    self.date_picker_1.date = self.row['emp_dob']
    self.date_picker_2.date = self.row['emp_doj']

    self.emp_type = self.row['emp_type']
    if self.emp_type == "Staff":
      self.radio_button_3.selected = True
      self.radio_button_4.selected = False
    else:
      self.radio_button_4.selected = True
      self.radio_button_3.selected = False

    self.text_box_3.text = self.row['emp_dept_name']
    self.drop_down_2.items = anvil.server.call('dept_change_name_and_code',gvarb.g_comcode)
    self.text_box_4.text = self.row['emp_desi_name']
    self.drop_down_3.items = anvil.server.call('desi_change_name_and_code',gvarb.g_comcode)

    self.emp_pfc = self.row['emp_pf_contribution']
    if self.emp_pfc == True:
      self.custom_1.radio_button_1.selected = True
      self.custom_1.radio_button_2.selected = False
    else:
      self.custom_1.radio_button_2.selected = True
      self.custom_1.radio_button_1.selected = False

    self.custom_1.text_box_1.text = self.row['emp_pf_number']
    self.custom_1.text_box_2.text = self.row['emp_pf_uan']

    self.emp_esic = self.row['emp_esi_contribution']
    if self.emp_esic == True:
      self.custom_2.radio_button_1.selected = True
      self.custom_2.radio_button_2.selected = False
    else:
      self.custom_2.radio_button_2.selected = True
      self.custom_2.radio_button_1.selected = False

    self.custom_2.text_box_1.text = self.row['emp_esi_number']
    self.custom_2.text_box_2.text = self.row['emp_esi_dispensary']

    self.emp_ptc = self.row['emp_pt_contribution']
    if self.emp_ptc == True:
      self.custom_3.radio_button_1.selected = True
      self.custom_3.radio_button_2.selected = False
    else:
      self.custom_3.radio_button_2.selected = True
      self.custom_3.radio_button_1.selected = False

    self.emp_itc = self.row['emp_it_contribution']
    if self.emp_itc == True:
      self.custom_3.radio_button_3.selected = True
      self.custom_3.radio_button_4.selected = False
    else:
      self.custom_3.radio_button_4.selected = True
      self.custom_3.radio_button_3.selected = False
      
    self.custom_3.text_box_1.text = self.row['emp_pan_number']
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1.text == "":
      Notification("Employee name cannot be blank").show()
    else:
      if self.radio_button_1.selected == True:
        self.emp_sex = "Male"
      else:
        self.emp_sex = "Female"

      if self.radio_button_3.selected == True:
        self.emp_type = "Staff"
      else:
        self.emp_type = "Worker"

      if self.custom_1.radio_button_1.selected == True:
        self.emp_pfc = True
      else:
        self.emp_pfc = False

      if self.custom_2.radio_button_1.selected == True:
        self.emp_esic = True
      else:
        self.emp_esic = False

      if self.custom_3.radio_button_1.selected == True:
        self.emp_ptc = True
      else:
        self.emp_ptc = False

      if self.custom_3.radio_button_3.selected == True:
        self.emp_itc = True
      else:
        self.emp_itc = False

      dept_code,dept_name,desi_code,desi_name = None,None,None,None
      self.dept_code,self.desi_code = None,None
      if self.drop_down_2.selected_value != None:
        split_list_dept = self.drop_down_2.selected_value.split("|")
        split_list_dept = [ele.strip() for ele in split_list_dept] 
        dept_code,dept_name = split_list_dept[0],split_list_dept[1]

      if self.drop_down_3.selected_value != None:
        split_list_desi = self.drop_down_3.selected_value.split("|")
        split_list_desi = [ele.strip() for ele in split_list_desi] 
        desi_code,desi_name = split_list_desi[0],split_list_desi[1]

      if self.row['emp_dept_code'] != dept_code:
        self.dept_code = dept_code
        self.text_box_3.text = dept_name

      if self.row['emp_desi_code'] != desi_code:
        self.desi_code = desi_code
        self.text_box_4.text = desi_name

      anvil.server.call('emp_update_row', self.emp_code, 
                                      self.text_box_1.text,
                                      self.text_box_2.text,
                    self.date_picker_1.date,
                    self.date_picker_2.date,
                    self.emp_sex,
                    self.emp_type,
                    self.emp_pfc,
                    self.custom_1.text_box_1.text,
                    self.custom_1.text_box_2.text,
                    self.emp_esic,
                    self.custom_2.text_box_1.text,
                    self.custom_2.text_box_2.text,
                    self.emp_ptc,
                    self.emp_itc,
                    self.custom_3.text_box_1.text,
                    self.dept_code,
                    self.text_box_3.text,
                    self.desi_code,
                    self.text_box_4.text,
                    )
      Notification(self.text_box_1.text + " data modified successfully").show()
      self.drop_down_1.visible=True

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
    open_form('emp_change')

