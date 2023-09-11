from ._anvil_designer import company_selectTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from .. import gvarb

class company_select(company_selectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # first open the login/signup form
    # anvil.users.login_with_form()

    form['']
    data = anvil.server.call('get_all_companies')
    if len(list(data)) == 0:
      self.button_2.visible = "True"
      self.button_3.visible = "True" 
      self.button_4.visible = "True" 
      print("no company")
    else:
      self.company_select_dp.visible = "True"
      self.submit_btn.visible = "True"
      self.button_1.visible = "True"
      print("companies exist")
    

    # after login, populate dropdown 
    self.company_select_dp.items = anvil.server.call('company_select_code_and_name')

  def submit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.company_select_dp.selected_value!=None:
      split_list_comp = self.company_select_dp.selected_value.split("|")
      split_list_comp = [ele.strip() for ele in split_list_comp] 
      gvarb.g_comcode,gvarb.g_comname = split_list_comp[0],split_list_comp[1]
     
      open_form('mode_select')
    else:
      Notification("Pls select company").show()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
   # open_form('company_select')
    anvil.users.login_with_form()

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('comp_new')







    
