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

  def call_dept_names(self, **kwargs):
    data = anvil.server.call('get_dept_names')
    self.dept_dp.items = data

  def save_to_database(self, db_val, **kwargs):
    anvil.server.call('save_data', db_val)
