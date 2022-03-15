from icecream import ic
from context.models import Model
from context.domains import Dataset


class TitanicModel(object):
    def __init__(self, train_fname, test_fname):
        self.dataset = Dataset()
        self.model = Model()
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출
        ic(f'트레인 컬럼 {self.train.columns}')
        ic(f'트레인 헤드 {self.train.head()}')
        ic(self.train)

    def preprocess(self):
        self.sib_sp_garbage()
        self.parch_garbage()
        self.ticket_garbage()
        self.cabin_garbage()

        self.crate_train()
        self.create_label()
        self.pclass_ordinal()
        self.name_norminal()
        self.fare_ratio()
        self.embarked_norminal()
        self.sex_norminal()
        self.age_ratio()

    def create_label(self) -> object:
        pass

    def crate_train(self) -> object:
        pass

    def drop_feature(self) -> object:
        pass

    '''
    Categorical vs Quantitativa
    cate -> naminal(이름) vs oridnla(순서)
    Quan -> interval(상대적) vs ratio(기준점 존재,절대)
    '''

    def pclass_ordinal(self)-> object:
        pass

    def name_norminal(self)-> object:  # 성씨(계급을 나타냄 ex.Mr,Rev)만 이용함
        pass

    def sex_norminal(self)-> object:
        pass

    def age_ratio(self)-> object:
        pass

    def sib_sp_garbage(self)-> object:
        self.drop_feature()

    def parch_garbage(self)-> object:
        self.drop_feature()

    def ticket_garbage(self)-> object:
        self.drop_feature()

    def fare_ratio(self)-> object:
        pass

    def cabin_garbage(self)-> object:
        self.drop_feature()

    def embarked_norminal(self)-> object:
        pass
