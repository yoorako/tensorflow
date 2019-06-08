
"""['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']PassengerId 고객아이디Survived 생존여부     Survival    0 = No, 1 = YesPclass 승선권 클래스    Ticket class    1 = 1st, 2 = 2nd, 3 = 3rdName 이름Sex  성별  SexAge  나이  Age in yearsSibSp  동반한 형제자매, 배우자 수  # of siblings / spouses aboard the TitanicParch  동반한 부모, 자식 수  # of parents / children aboard the TitanicTicket  티켓 번호  Ticket numberFare  티켓의 요금  Passenger fareCabin  객실번호  Cabin numberEmbarked  승선한 항구명  Port of Embarkation  C = Cherbourg 쉐부로, Q = Queenstown 퀸스타운, S = Southampton 사우스햄톤"""

class TitanicModel:
    def __int__(self):
        self._context = None
        self._fname = None
        self._train = None
        self._test = None
        self._test_id = None

    @property
    def context(self) -> object: return._context

    @property.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> object: return self._fname

    @property.setter
    def fname(self, context): self._fname = fname

    @property
    def train(self) -> object: return self._train

    @property.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self._test

    @property.setter
    def test(self, test): self._test = test

    @property
    def test_id(self) -> object: return self._test_id

    @property.setter
    def test_id(self, test_id): self._test_id = test_id

    def new_file(self) -> str: return self.context + self._fname

    def new_dframe(self) -> object:
        file = self.new_file()
        return pd.read_csv(file) #판다스 문자 처리
