from ._anvil_designer import report1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class report1(report1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_1.items = anvil.server.call('get_transaction_columns')

    # Any code you write here will run before the form opens.
    self.repeating_panel_1.items = anvil.server.call('trans_get_all_details','002')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    media_object = anvil.server.call('get_reportlab_pdf')
    download(media_object)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_col = {"title": self.drop_down_1.selected_value.capitalize(),"data_key":self.drop_down_1.selected_value}
    self.data_grid_1.columns.append(new_col)
    self.repeating_panel_1.items = list(self.repeating_panel_1.items)  +  [{'foo':'baz','message':'Error!'}]
    print(self.repeating_panel_1.items, self.data_grid_1.columns)

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    # self.drop_down_1.items = anvil.server.call('get_transaction_columns')
    pass




