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
    #self.label_2.text = gvarb.g_comname+' '+gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")

    comp_details = anvil.server.call('comp_get_details', '002')
    self.columns,self.unmodified_cols = anvil.server.call('get_transaction_columns', comp_details)
    print("Original cols: ", self.unmodified_cols)
    print("Modified cols: ", self.columns)

    flow_panel = anvil.FlowPanel()
    for i in range(len(self.columns)):
      if self.columns[i] == 'trans_empid' or self.columns[i] == 'trans_empname':
        checkbox = CheckBox(text=self.columns[i], checked=True)  
        flow_panel.add_component(checkbox)
      else:
        checkbox = CheckBox(text=self.columns[i], checked=False)  
        flow_panel.add_component(checkbox)
    self.add_component(flow_panel)

    # Dynamically create sellect button
    button = anvil.Button(text="Preview")
    button.role = 'filled-button'
    self.add_component(button)
    button.set_event_handler('click', self.dynamic_button_click)

    # Dynamically create set all button
    button_set = anvil.Button(text="set all sellection")
    button_set.role = 'filled-button'
    self.add_component(button_set)
    button_set.set_event_handler('click', self.dynamic_button_set_click)
    
    # Dynamically create clear all button
    button_clear = anvil.Button(text="Clear all sellection")
    button_clear.role = 'filled-button'
    self.add_component(button_clear)
    button_clear.set_event_handler('click', self.dynamic_button_clear_click)

  # Attach a click listener
  def dynamic_button_set_click(self, **event_args):
    all_components = self.get_components()
    print(all_components)
    all_flow_components = [component for component in all_components if isinstance(component, anvil.FlowPanel)]
    flow_component_with_checkboxes = all_flow_components[-1].get_components()
    only_checkboxes = [component for component in flow_component_with_checkboxes if isinstance(component, anvil.CheckBox)]
    print(only_checkboxes)
    for checkbox in only_checkboxes:
      print(checkbox)
      checkbox.checked = True

  # Attach a click listener
  def dynamic_button_clear_click(self, **event_args):
    open_form('report_new')


  # Attach a click listener
  def dynamic_button_click(self, **event_args):
    # Your code to be executed when the button is clicked
    all_components = self.get_components()
    if isinstance(all_components[-1], anvil.DataGrid):
      all_components[-1].remove_from_parent()
    print(all_components)
    all_flow_components = [component for component in all_components if isinstance(component, anvil.FlowPanel)]
    flow_component_with_checkboxes = all_flow_components[-1].get_components()
    only_checkboxes = [component for component in flow_component_with_checkboxes if isinstance(component, anvil.CheckBox)]
    selected_boxes = []
    modified_col_names = []
    for checkbox in only_checkboxes:
      if checkbox.checked and checkbox.text not in self.unmodified_cols:
        print("Selected and not in og list: ",checkbox.text)
        pos = self.columns.index(checkbox.text)
        print("corresponding unmodified value ",self.unmodified_cols[pos])
        selected_boxes.append(self.unmodified_cols[pos])
        modified_col_names.append(checkbox.text)
      elif checkbox.checked and checkbox.text in self.unmodified_cols:
        selected_boxes.append(checkbox.text)
        modified_col_names.append(checkbox.text)
    grid_rows, grid_cols = anvil.server.call('get_only_selected_trans_values', '002',selected_boxes,modified_col_names)
    print(type(grid_cols), grid_cols)
    print(type(selected_boxes), selected_boxes)
    grid = anvil.DataGrid()
    grid.role = 'wide'
    self.add_component(grid)
    grid.columns = grid_cols
    # grid.columns = selected_boxes

    rp = anvil.RepeatingPanel(item_template=anvil.DataRowPanel)
    rp.items = grid_rows
    # Add the repeating panel to your data grid
    grid.add_component(rp)
    all_components = self.get_components()
    print(all_components)    

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  # def button_1_click(self, **event_args):
  #   """This method is called when the button is clicked"""
  #   all_components = self.get_components()
  #   if isinstance(all_components[-1], anvil.DataGrid):
  #     all_components[-1].remove_from_parent()
  #   print(all_components)
  #   all_flow_components = [component for component in all_components if isinstance(component, anvil.FlowPanel)]
  #   flow_component_with_checkboxes = all_flow_components[-1].get_components()
  #   only_checkboxes = [component for component in flow_component_with_checkboxes if isinstance(component, anvil.CheckBox)]
  #   selected_boxes = []
  #   for checkbox in only_checkboxes:
  #     if checkbox.checked:
  #       selected_boxes.append(checkbox.text)
  #   grid_rows, grid_cols = anvil.server.call('get_only_selected_trans_values', '002',selected_boxes)

  #   grid = anvil.DataGrid()
  #   grid.role = 'wide'
  #   self.add_component(grid)
  #   grid.columns = grid_cols

  #   rp = anvil.RepeatingPanel(item_template=anvil.DataRowPanel)
  #   rp.items = grid_rows
  #   # Add the repeating panel to your data grid
  #   grid.add_component(rp)
  #   all_components = self.get_components()
  #   print(all_components)

 

