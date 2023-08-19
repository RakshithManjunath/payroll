import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

####### trans date #######
@anvil.server.callable
def cur_trans_date():
    return [(r["tr_date"]) for r in app_tables.trans_date.search()]
