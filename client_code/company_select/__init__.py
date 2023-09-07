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
    anvil.users.login_with_form()

    # after login, populate dropdown 
    self.company_select_dp.items = anvil.server.call('company_select_code_and_name')

  def submit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.company_select_dp.selected_value!=None:
      split_list_comp = self.company_select_dp.selected_value.split("|")
      split_list_comp = [ele.strip() for ele in split_list_comp] 
      gvarb.g_comcode,gvarb.g_comname = split_list_comp[0],split_list_comp[1]
     
      comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
      gvarb.g_leave1 = comp_details['comp_leave_head1']
      gvarb.g_leave2 = comp_details['comp_leave_head2']  
      gvarb.g_leave3 = comp_details['comp_leave_head3']      

      gvarb.g_ded1 = comp_details['comp_ded1'] 
      gvarb.g_ded2 = comp_details['comp_ded2']
      gvarb.g_ded3 = comp_details['comp_ded3'] 
      gvarb.g_ded4 = comp_details['comp_ded4'] 

      gvarb.g_loan1 = comp_details['comp_loan_head1'] 
      gvarb.g_loan2 = comp_details['comp_loan_head2'] 

      open_form('mode_select')
    else:
      Notification("Pls select company").show()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
   # open_form('company_select')
    anvil.users.login_with_form()




    
