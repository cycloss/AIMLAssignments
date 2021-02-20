class Data:
    def __init__(self, height: str, glasses: str, favMusic: str, ageGrp: str):
        self.height = float(height)
        self.glasses = self.__convertYNToBool(glasses)
        self.favMusic = favMusic
        self.ageGrp = ageGrp

    def __convertYNToBool(self, yn: str) -> bool:
        if yn == 'Yes':
            return True
        elif yn == 'No':
            return False
        else:
            raise Exception(f'Could not parse {yn}')

    outClasses = [
        'Toddler', 'Child', 'Teenager', 'Young Adult', 'Adult', 'Elderly'
    ]
    # groups the data by output class
    @classmethod
    def groupData(cls, data: list, classes=list[str]) -> dict:
        resDict: dict[str, Data] = dict()
        for c in cls.outClasses:
            resDict[c] = list(filter(lambda item: item.ageGrp == c, data))
        return resDict

    def __str__(self) -> str:
        return str(
            f'Height: {self.height}, Glasses: {self.glasses}, Favourite Music: {self.favMusic}, Age Group: {self.ageGrp}'
        )