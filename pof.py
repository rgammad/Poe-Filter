# Various Classes for filter generation


# =================================================================================================
# Conditions
# =================================================================================================
class Conditions():

    def ItemLevel(self, itemlevel, operator=0):
        """Item level the item was generated at

        :param itemlevel: item level
        :input itemlevel: int 0-100
        """

    def DropLevel(self, droplevel, operator=0):
        """Level the item starts dropping at

        :param droplevel: level item starts dropping at
        :input droplevel: int 0-100
        """

    def Quality(self, quality, operator=0):
        """Amount of Quality on item

        :param quality: item quality
        :input quality: int 0-20
        """

    def Rarity(self, rarity, operator=0):
        """Rarity of the item

        :param rarity: item rarity
        :input rarity: string rarity name, Normal, Magic, Rare, Unique
        """

    def ItemClass(self, itemclass):
        """The item class.
            Specifying part of a class name is allowed and will match any classes
                with that text in the name.
            So for example "One Hand" will match both "One Hand Sword" and "One Hand Axe".

        :param itemclass: item class
        :input itemclass: string, full or partial name
        """

    def BaseType(self, basetype):
        """The base type of the item.
            Specifying part of the base type name is allowed and will match any of the base types
            with that text in the name

        :param basetype: item base
        :input basetype: string, full or partial name
        """

    def SocketAmount(self, socketamount, operator=0):
        """Total number of sockets the item has

        :param socketamount: amount of sockets
        :input socketamount: 0-6
        :param operator: comparison operators
        :input operator: 0-5
        """

    def LinkedSockets(self, linkedsockets, operator=0):
        """Size of the largest group of linked sockets the item has

        :param linkedsockets: amount of sockets linked
        :input linkedsockets: 0-6
        :param operator: comparison operators
        :input operator: 0-5
        """

    def SocketGroup(self, socketgroup):
        """A group of linked sockets that contains the specified combination.
            Each letter is short-hand for the colour (i.e. Red = R).
            For example, RRG will match any group that contains
            two red sockets linked with a green socket.

        :param socketgroup: socket group combinations
        :input socketgroup: string R,G,B,W
        """

    def MapTier(self, maptier, operator=0):
        """The map tier of the item

        :param maptier: tier of map
        :input maptier: 1-17
        :param operator: comparison operators
        :input operator: 0-5
        """


class Actions():
    def Show(self, show=true):

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
