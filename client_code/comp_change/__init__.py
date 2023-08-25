from ._anvil_designer import comp_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class comp_change(comp_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.drop_down_1.items = anvil.server.call('comp_change_name_and_code')

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    split_list_comp = self.drop_down_1.selected_value.split("|")
    split_list_comp = [ele.strip() for ele in split_list_comp] 
    self.comp_code,self.comp_name = split_list_comp[0],split_list_comp[1]

    self.row = anvil.server.call('comp_get_details',self.comp_code)

    self.text_box_1.text = self.row['comp_addr1']
    self.text_box_2.text = self.row['comp_addr2']
    self.text_box_3.text = self.row['comp_addr3']
    #self.text_box_4.text = self.row['bank_ifsc']
   # self.text_box_5.text = self.bank_name


