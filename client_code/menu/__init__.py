from ._anvil_designer import menuTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class menu(menuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def open_login_page(self, **kwargs):
    anvil.users.logout()
    alert(f"You have logged out successfully...!")
    open_form('company_select')

  def open_update_page(self, **kwargs):
    open_form('update_trans_date')

  def open_emp_add(self, **kwargs):
    open_form('emp_add')

  def open_dept(self, **kwargs):
    open_form('dept')

  def open_desi(self, **kwargs):
    open_form('desi')
