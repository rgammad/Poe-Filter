# Actions class for poefilter


# =================================================================================================
# Actions
# =================================================================================================
class Actions():

    def SetBorderColor(self, r, g, b, a=255):
        """
        Sets the border colour of the item box in RGB values from 0-255
        with optional Alpha (opacity) value of 0-255
        """

    def SetTextColor(self, r, g, b, a=255):
        """
        Sets the text colour of the item box in RGB values from 0-255
        with optional Alpha (opacity) value of 0-255
        """

    def SetBackgroundColor(self, r, g, b, a=255):
        """
        Sets the colour of the item box in RGB values from 0-255
        with optional Alpha (opacity) value of 0-255
        """

    def SetFontSize(self, fontsize=32):
        """Sets the font size of the item text."""

    def PlayAlertSound(self, id, volume):
        """Plays the specified Alert Sound with optional volume when dropped.

        Only one sound can be played at a time.
        """

    def PlayAlertSoundPositional(self, id, volume):
        """Plays the specified Alert Sound with optional volume when dropped.

        Only one sound can be played at a time.
        """

    def CustomAlertSound(self, filepath):
        """
        Plays the specified custom sound when a specified item drops.
        (almost all of the common file extensions should be supported)
        """

    def MinimapIcon(self, size, color, shape):
        """Displays an icon on the minimap for specified items."""

    def PlayEffect(self, color, temp):
        """
            Displays a coloured beam of light above an item highlighted by an item filter.
            Use the Temp parameter to have a beam only appear as the item drops.
            Otherwise, it will be permanently visible.
        """
