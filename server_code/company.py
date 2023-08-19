import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

####### company select ########
@anvil.server.callable
def company_select_code_and_name():
  company_details = [row['company_code'] + " | "  +row['company_name'] for row in app_tables.company.search(tables.order_by("company_code"))]
  return company_details
