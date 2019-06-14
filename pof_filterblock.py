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

    def __init__(self):
        """init"""

    def Create(self, show=True):
        """ Begining of the filter block
        :param show: Shows or Hides items based on rest of the block
        :input show: bool true to show false to hide
        """

    def AddCondition(self, *args):
        """Add Conditions to FilterBlock
        :param args: condition arguments
        :input args: condition name, condition inputs...
        """
        if args[0] == "ItemLevel":
            return self.lstcond.append(conditions.ItemLevel(args[1], args[2]))
        elif args[0] == "DropLevel":
            return self.lstcond.append(conditions.DropLevel(args[1], args[2]))
        elif args[0] == "Quality":
            return self.lstcond.append(conditions.Quality(args[1], args[2]))
        elif args[0] == "Rarity":
            return self.lstcond.append(conditions.Rarity(args[1], args[2]))
        elif args[0] == "ItemClass":
            return self.lstcond.append(conditions.ItemClass(args[1]))
        elif args[0] == "BaseType":
            return self.lstcond.append(conditions.BaseType(args[1]))
        elif args[0] == "SocketAmount":
            return self.lstcond.append(conditions.SocketAmount(args[1], args[2]))
        elif args[0] == "LinkedSocket":
            return self.lstcond.append(conditions.LinkedSocket(args[1], args[2]))
        elif args[0] == "SocketGroup":
            return self.lstcond.append(conditions.SocketGroup(args[1]))
        elif args[0] == "MapTier":
            return self.lstcond.append(conditions.MapTier(args[1]))

    def AddAction(self, *args):
        """Add Actions to FilterBlock
        :param args: action arguments
        :input args: action name, argument inputs...
        """
        if args[0] == "BorderColor":
            return self.lstact.append(actions.SetBorderColor(args[1], args[2], args[3], args[4]))
        elif args[0] == "TextColor":
            return self.lstact.append(actions.SetTextColor(args[1], args[2], args[3], args[4]))
        elif args[0] == "BackgroundColor":
            return self.lstact.append(actions.SetBackgroundColor(args[1], args[2],
                                                                 args[3], args[4]))
        elif args[0] == "FontSize":
            return self.lstact.append(actions.SetFontSize(args[1]))
        elif args[0] == "AlertSound":
            return self.lstact.append(actions.PlayAlertSound(args[1], args[2]))
        elif args[0] == "AlertSoundPositional":
            return self.lstact.append(actions.PlayAlertSoundPositional(args[1], args[2]))
        elif args[0] == "CustomAlertSound":
            return self.lstact.append(actions.CustomAlertSound(args[1]))
        elif args[0] == "MinimapIcon":
            return self.lstact.append(actions.MinimapIcon(args[1], args[2], args[3]))
        elif args[0] == "PlayEffect":
            return self.lstact.append(actions.PlayEffect(args[1], args[2]))
