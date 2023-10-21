from ._anvil_designer import report_newTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class report_new(report_newTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    comp_details = anvil.server.call('comp_get_details', '002')
    columns = anvil.server.call('get_transaction_columns', comp_details)

    flow_panel = anvil.FlowPanel()
    for i in range(len(columns)):
      if columns[i] == 'trans_empid' or columns[i] == 'trans_empname':
        checkbox = CheckBox(text=columns[i], checked=True)  
        flow_panel.add_component(checkbox)
      else:
        checkbox = CheckBox(text=columns[i], checked=False)  
        flow_panel.add_component(checkbox)
    self.add_component(flow_panel)  

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    all_components = self.get_components()
    if isinstance(all_components[-1], anvil.DataGrid):
      all_components[-1].remove_from_parent()
    print(all_components)
    all_flow_components = [component for component in all_components if isinstance(component, anvil.FlowPanel)]
    flow_component_with_checkboxes = all_flow_components[-1].get_components()
    only_checkboxes = [component for component in flow_component_with_checkboxes if isinstance(component, anvil.CheckBox)]
    selected_boxes = []
    for checkbox in only_checkboxes:
      if checkbox.checked:
        selected_boxes.append(checkbox.text)
    grid_rows, grid_cols = anvil.server.call('get_only_selected_trans_values', '002',selected_boxes)

    grid = anvil.DataGrid()
    grid.role = 'wide'
    self.add_component(grid)
    grid.columns = grid_cols

    rp = anvil.RepeatingPanel(item_template=anvil.DataRowPanel)
    rp.items = grid_rows
    # Add the repeating panel to your data grid
    grid.add_component(rp)
    all_components = self.get_components()
    print(all_components)


