from ._anvil_designer import emp_trans_viewTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class emp_trans_view(emp_trans_viewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.populate_custom_data_grid()
    self.repeating_panel_1.items = anvil.server.call('trans_get_all_details')

  def populate_custom_data_grid(self):
    # col = self.data_grid_1.columns
    columns = self.data_grid_1.columns
    # print(columns, len(columns))
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
    columns[21]["title"] = comp_details['comp_leave_head1']
    columns[22]["title"] = comp_details['comp_leave_head2']
    columns[23]["title"] = comp_details['comp_leave_head3']  

    columns[26]["title"] = comp_details['comp_ded1'] 
    columns[27]["title"] =comp_details['comp_ded2']      
    columns[28]["title"] = comp_details['comp_ded3']     
    columns[29]["title"] = comp_details['comp_ded4']   

    columns[30]["title"] = comp_details['comp_loan_head1']  
    columns[31]["title"] = comp_details['comp_loan_head2']       
    
    # Update the Data Grid with the modified column
    self.data_grid_1.columns = columns


    
    
    ######## Find the index value of acolumn in the DataGrid##############
    # # Specify the field name you want to check for
    #field_name = 'Trans Leave1'
    
  # for col in col:
  #   if (col["name"] == field_name):
  #     print(col["name"])
  #   else:
  #     pass

    # Specify the index of the column you want to change (e.g., column at index 2)
    #column_index_to_change = 2
    
    # Set the new header text for the specified column
    # new_header_text = gvarb.g_leave2
    # columns[3]["title"] = new_header_text
  
    # Update the Data Grid with the modified column
    #self.data_grid_1.columns = columns
    
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

