from ._anvil_designer import comp_earnhead1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb


class comp_earnhead1(comp_earnhead1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
    self.label_1.text = comp_details['comp_earn_head1']
    self.label_1.border="solid"
    self.label_2.text = comp_details['comp_earn_head2']
    self.label_2.border="solid"
    self.label_3.text = comp_details['comp_earn_head3']
    self.label_3.border="solid"
    self.label_4.text = comp_details['comp_earn_head4'] 
    self.label_4.border="solid"
    self.label_5.text = comp_details['comp_earn_head5']
    self.label_5.border="solid"

    self.label_6.text = comp_details['comp_earn_head6']
    self.label_6.border="solid"
    self.label_7.text = comp_details['comp_earn_head7']
    self.label_7.border="solid"
    self.label_8.text = comp_details['comp_earn_head8']
    self.label_8.border="solid"
    self.label_9.text = comp_details['comp_earn_head9'] 
    self.label_9.border="solid"
    self.label_10.text = comp_details['comp_earn_head10']
    self.label_10.border="solid"

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call(gvarb.g_comcode,self.check_box_1.text,self.check_box_2.text,self.check_box_3.text,
                      self.check_box_4.text,self.check_box_5.text,self.check_box_6.text,self.check_box_7.text,
                      self.check_box_8.text,self.check_box_9.text,self.check_box_10.text,self.check_box_11.text,
                      self.check_box_12.text,self.check_box_13.text,self.check_box_14.text,self.check_box_15.text,
                      self.check_box_16.text,self.check_box_17.text,self.check_box_18.text,self.check_box_19.text,
                      self.check_box_20.text,self.check_box_21.text,self.check_box_22.text,self.check_box_23.text,
                      self.check_box_24.text,self.check_box_25.text,self.check_box_26.text,self.check_box_27.text,
                      self.check_box_28.text,self.check_box_29.text,self.check_box_30.text,self.check_box_31.text,
                      self.check_box_32.text,self.check_box_33.text,self.check_box_34.text,self.check_box_35.text,
                      self.check_box_36.text,self.check_box_37.text,self.check_box_38.text,self.check_box_39.text,
                      self.check_box_40.text,self.check_box_41.text,self.check_box_42.text,self.check_box_43.text,
                      self.check_box_44.text,self.check_box_45.text,self.check_box_46.text,self.check_box_47.text,
                      self.check_box_48.text,self.check_box_49.text,self.check_box_50.text)
    
