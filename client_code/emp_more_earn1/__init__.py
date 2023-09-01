from ._anvil_designer import emp_more_earn1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class emp_more_earn1(emp_more_earn1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)

    ## HEAD1 ######    
    self.label_1.text = comp_details['comp_earn_head1']

    ## HEAD2 ######    
    self.label_2.text = comp_details['comp_earn_head2']

    ## HEAD3 ######    
    self.label_3.text = comp_details['comp_earn_head3']
    
    ## HEAD4 ######    
    self.label_4.text = comp_details['comp_earn_head4'] 
    
    ## HEAD5 ######    
    self.label_5.text = comp_details['comp_earn_head5']
    
    ## HEAD6 ######
    self.label_6.text = comp_details['comp_earn_head6']
    
    ## HEAD7 ######    
    self.label_7.text = comp_details['comp_earn_head7']
    
    ## HEAD8 ######    
    self.label_8.text = comp_details['comp_earn_head8']
    
    ## HEAD9 ######    
    self.label_9.text = comp_details['comp_earn_head9'] 

    ## HEAD10 ###### 
    #if comp_details['comp_earn_head10'].text!=None:
    self.label_10.text = comp_details['comp_earn_head10']
    #else:
      #self.label_10.disable = True
      
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    # split_list_emp = parent_form.drop_down_1.selected_value.split("|")
    #print(self.parent, self.parent.parent, self.parent.parent.parent)
    parent = self.parent.parent.get_components()
    dropdowns = [component for component in parent if isinstance(component, anvil.DropDown)]

    split_list_emp = dropdowns[0].selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    emp_code,emp_name = split_list_emp[0],split_list_emp[1]
    anvil.server.call('emp_update_earn',emp_code,self.text_box_1.text,
                     self.text_box_2.text,self.text_box_3.text,
                     self.text_box_4.text)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('emp_more_earn1')


