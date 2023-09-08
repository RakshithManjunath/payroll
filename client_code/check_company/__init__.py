from ._anvil_designer import check_companyTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class check_company(check_companyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    data = anvil.server.call('get_all_companies')
    if len(list(data)) == 0:
      print("no company")
      open_form('comp_add_change')
    else:
      print("companies exist")
      open_form('company_select')
