from ._anvil_designer import emp_more_earn1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class emp_more_earn1(emp_more_earn1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)

    ## HEAD1 ######    
    self.label_1.text = comp_details['comp_earn_head1']
    self.label_1.border="solid"
    self.check_box_1.checked = comp_details['comp_earnhead1_pf']
    self.check_box_11.checked = comp_details['comp_earnhead1_esi']
    self.check_box_21.checked = comp_details['comp_earnhead1_pt']
    self.check_box_31.checked = comp_details['comp_earnhead1_ot']
    self.check_box_41.checked = comp_details['comp_earnhead1_it'] 
    self.check_box_51.checked = comp_details['comp_earnhead1_bonus']

    ## HEAD2 ######    
    self.label_2.text = comp_details['comp_earn_head2']
    self.label_2.border="solid"
    self.check_box_2.checked = comp_details['comp_earnhead2_pf']
    self.check_box_12.checked = comp_details['comp_earnhead2_esi']
    self.check_box_22.checked = comp_details['comp_earnhead2_pt']
    self.check_box_32.checked = comp_details['comp_earnhead2_ot'] 
    self.check_box_42.checked = comp_details['comp_earnhead2_it'] 
    self.check_box_52.checked = comp_details['comp_earnhead2_bonus']    

    ## HEAD3 ######    
    self.label_3.text = comp_details['comp_earn_head3']
    self.label_3.border="solid"
    self.check_box_3.checked = comp_details['comp_earnhead3_pf']
    self.check_box_13.checked = comp_details['comp_earnhead3_esi']
    self.check_box_23.checked = comp_details['comp_earnhead3_pt']
    self.check_box_33.checked = comp_details['comp_earnhead3_ot']    
    self.check_box_43.checked = comp_details['comp_earnhead3_it']
    self.check_box_53.checked = comp_details['comp_earnhead3_bonus']    
    
    ## HEAD4 ######    
    self.label_4.text = comp_details['comp_earn_head4'] 
    self.label_4.border="solid"
    self.check_box_4.checked = comp_details['comp_earnhead4_pf']
    self.check_box_14.checked = comp_details['comp_earnhead4_esi']
    self.check_box_24.checked = comp_details['comp_earnhead4_pt']
    self.check_box_34.checked = comp_details['comp_earnhead4_ot']    
    self.check_box_44.checked = comp_details['comp_earnhead4_it']
    self.check_box_54.checked = comp_details['comp_earnhead4_bonus']
    
    ## HEAD5 ######    
    self.label_5.text = comp_details['comp_earn_head5']
    self.label_5.border="solid"
    self.check_box_5.checked = comp_details['comp_earnhead5_pf']
    self.check_box_15.checked = comp_details['comp_earnhead5_esi']
    self.check_box_25.checked = comp_details['comp_earnhead5_pt']
    self.check_box_35.checked = comp_details['comp_earnhead5_ot']
    self.check_box_45.checked = comp_details['comp_earnhead5_it']
    self.check_box_55.checked = comp_details['comp_earnhead5_bonus']
    
    ## HEAD6 ######
    self.label_6.text = comp_details['comp_earn_head6']
    self.label_6.border="solid"
    self.check_box_6.checked = comp_details['comp_earnhead6_pf']    
    self.check_box_16.checked = comp_details['comp_earnhead6_esi']
    self.check_box_26.checked = comp_details['comp_earnhead6_pt']
    self.check_box_36.checked = comp_details['comp_earnhead6_ot']
    self.check_box_46.checked = comp_details['comp_earnhead6_it']
    self.check_box_56.checked = comp_details['comp_earnhead6_bonus']
    
    ## HEAD7 ######    
    self.label_7.text = comp_details['comp_earn_head7']
    self.label_7.border="solid"
    self.check_box_7.checked = comp_details['comp_earnhead7_pf']
    self.check_box_17.checked = comp_details['comp_earnhead7_esi']    
    self.check_box_27.checked = comp_details['comp_earnhead7_pt']
    self.check_box_37.checked = comp_details['comp_earnhead7_ot']
    self.check_box_47.checked = comp_details['comp_earnhead7_it']
    self.check_box_57.checked = comp_details['comp_earnhead7_bonus'] 
    
    ## HEAD8 ######    
    self.label_8.text = comp_details['comp_earn_head8']
    self.label_8.border="solid"
    self.check_box_8.checked = comp_details['comp_earnhead8_pf']
    self.check_box_18.checked = comp_details['comp_earnhead8_esi']    
    self.check_box_28.checked = comp_details['comp_earnhead8_pt']
    self.check_box_38.checked = comp_details['comp_earnhead8_ot']
    self.check_box_48.checked = comp_details['comp_earnhead8_it']
    self.check_box_58.checked = comp_details['comp_earnhead8_bonus']    
    
    ## HEAD9 ######    
    self.label_9.text = comp_details['comp_earn_head9'] 
    self.label_9.border="solid"
    self.check_box_9.checked = comp_details['comp_earnhead9_pf']
    self.check_box_19.checked = comp_details['comp_earnhead9_esi']
    self.check_box_29.checked = comp_details['comp_earnhead9_pt']
    self.check_box_39.checked = comp_details['comp_earnhead9_ot']
    self.check_box_49.checked = comp_details['comp_earnhead9_it']    
    self.check_box_59.checked = comp_details['comp_earnhead9_bonus']    

    ## HEAD10 ######    
    self.label_10.text = comp_details['comp_earn_head10']
    self.label_10.border="solid"
    self.check_box_10.checked = comp_details['comp_earnhead10_pf']
    self.check_box_20.checked = comp_details['comp_earnhead10_esi']
    self.check_box_30.checked = comp_details['comp_earnhead10_pt']
    self.check_box_40.checked = comp_details['comp_earnhead10_ot'] 
    self.check_box_50.checked = comp_details['comp_earnhead10_it']
    self.check_box_60.checked = comp_details['comp_earnhead10_bonus']    

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


