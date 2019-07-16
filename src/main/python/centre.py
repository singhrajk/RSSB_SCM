from selenium.webdriver.common.keys import Keys
from tab import Tab
import constants
class Centre(Tab):

    def __init__(self):
        super(Centre, self).__init__()

    def search_schedule(self, input):
        self.search(constants.TAB_CENTRE, constants.GROUP_NO_CENTRE, constants.LIST_NO_CENTRE, constants.CHOICE_2, input)

    def search_details(self, input):
        self.search_query(constants.TAB_CENTRE, constants.GROUP_NO_CENTRE, constants.LIST_NO_CENTRE, constants.CHOICE_1, input)

    def delete_details(self, input):
        self.delete(constants.TAB_CENTRE, constants.GROUP_NO_CENTRE, constants.LIST_NO_CENTRE, constants.CHOICE_1, input)

    def insert_details(self, input):
        self.select_group_and_group_choice(TAB_CENTRE, GROUP_NO_CENTRE, LIST_NO_CENTRE, constants.CHOICE_1)
        self.log("\tPerforming the insert with input: " + input + " on the tab: " + TAB_CENTRE)
        self.send_keys_lookup(TAB_CENTRE, input)
        self.click_select_button(TAB_CENTRE)
        self.send_keys_lookup(constants.LAND_TYPE, Keys.DOWN)
        self.send_keys_lookup(constants.OWNERSHIP_TYPE, Keys.DOWN)
        self.send_keys_lookup(constants.LAND_NATURE, Keys.DOWN)
        self.send_keys_id(constants.LAND_EXTENT, constants.TEST)
        self.press_button(constants.BUTTON_SAVE, TAB_CENTRE)

    def export_details(self):
        self.export(constants.TAB_CENTRE, constants.GROUP_NO_CENTRE, constants.LIST_NO_CENTRE, constants.CHOICE_1)
