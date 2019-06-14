# Various Helper Classes for filter generation


# =================================================================================================
# Conditions
# =================================================================================================
class Conditions():

    def ItemLevel(self, itemlevel, operator=0):
        """Item level the item was generated at

        :param itemlevel: item level
        :input itemlevel: int 0-100
        """
        return "ItemLevel    " + itemlevel + " " + operator

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
