from ._anvil_designer import company_selectTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

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
    open_form('mode_select')


    
