from ._anvil_designer import pdf_viewerTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class pdf_viewer(pdf_viewerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.url = properties['url']

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    self.call_js('display_pdf', self.url)
