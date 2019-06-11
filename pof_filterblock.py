import pof_actions
import pof_conditions

conditions = pof_conditions
actions = pof_actions


# =================================================================================================
# FilterBlock
# =================================================================================================
class FilterBlock():

    lstcond = []
    lstact = []

    def __init__(self, conditions, actions):
        lstcond = conditions
        lstact = actions

    def Show(self, show=true):
        """ Begining of the filter block
        :param show: Shows or Hides items based on rest of the block
        :input show: bool true to show false to hide
        """
