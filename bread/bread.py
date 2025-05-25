class Bread():
    def __init__(self, loaves, rolls):
        self._loaves = loaves
        self._rolls = rolls

    def get_display_values(self):
        initial_flour_and_water = int(self._loaves * 25 + self._rolls * 6.25)
        yeast = self._loaves * .25 + self._rolls * .0625
        remaining_flour = int(self._loaves * 225 + self._rolls * 56.25)
        remaining_water = int(self._loaves * 180 + self._rolls * 45)
        total_flour = initial_flour_and_water + remaining_flour
        total_water = initial_flour_and_water + remaining_water

        flour_increments = int(remaining_flour/6)
        flour_increments -= flour_increments % 50
        if flour_increments < 50:
            flour_increments = 50

        salt = int(self._loaves * 6 + self._rolls * 1.5)

        portion_split = self._loaves + int(self._rolls/4)

        return {
            "loaves": self._loaves,
            "rolls": self._rolls,
            "initial_flour": initial_flour_and_water,
            "initial_water": initial_flour_and_water,
            "remaining_flour": remaining_flour,
            "remaining_water": remaining_water,
            "flour_increments": flour_increments,
            "total_flour": total_flour,
            "total_water": total_water,
            "yeast": yeast,
            "salt": salt,
            "portion_split": portion_split,
        }