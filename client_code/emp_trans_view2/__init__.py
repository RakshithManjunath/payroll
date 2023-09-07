from ._anvil_designer import emp_trans_view2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class emp_trans_view2(emp_trans_view2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.populate_custom_data_grid()
    self.repeating_panel_1.items = anvil.server.call('trans_get_all_details')

    # self.repeating_panel_1.items = anvil.server.call('trans_get_all_details')
    # Any code you write here will run before the form opens.
    # data = self.populate_custom_data_grid()
    # rp_items = []
    # for row in data:
    #   print(row)
    #   print(row["Custom_Column1"])
    #   rp_items.append(row[0]['CustomColumn2'])
    # self.repeating_panel_1.items = rp_items
    # self.repeating_panel_1.items = self.populate_custom_data_grid()
    # self.data_grid_1.add_component(self.repeating_panel_1)

  def populate_custom_data_grid(self):
    # Fetch data from an existing data source (e.g., 'existing_data_table')
    # get_trans_details = anvil.server.call('trans_get_all_details')
    # self.data_grid_1.clear()
    # custom_data = []
    # # Iterate through the rows of the existing data table
    # for row in get_trans_details:
    #     # Create a dictionary to represent the row data with custom column names
    #     custom_row_data = {
    #         'empid': row['trans_empid'],
    #         'empname': row['trans_empname'],
    #         # Add more columns as needed
    #     }
    #     # Add the custom row data to the custom Data Grid
    #     custom_data.append(custom_row_data)
    # return custom_data
    columns = self.data_grid_1.columns
    print(columns, len(columns))

    # Specify the index of the column you want to change (e.g., column at index 2)
    column_index_to_change = 2

    # Set the new header text for the specified column
    # new_header_text = "ABCD"
    # columns[column_index_to_change]["title"] = new_header_text

    new_header_text = gvarb.g_leave2
    columns[3]["title"] = new_header_text

    # Update the Data Grid with the modified column
    self.data_grid_1.columns = columns

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')
