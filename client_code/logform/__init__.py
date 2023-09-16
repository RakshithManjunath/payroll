from ._anvil_designer import logformTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class logform(logformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.newflag = False
    data = anvil.server.call('get_all_password')
    if len(list(data)) == 0:
      if(self.text_box_1.text== 'user1') and (self.text_box_2.text == '1'):
        self.newflag = True
       # open_form('comp_new')
      #print("no company")
    else:
         self.newflag = False
      #print("password exist")

    print(self.newflag)
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
  if (self.newflag == True):
    open_form('comp_new')
  else:
    value = anvil.server.call('check_username_and_password', self.text_box_1.text, self.text_box_2.text)
    if value == True:
      open_form('company_select')

