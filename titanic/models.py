import pandas as pd
from icecream import ic
from context.models import Model
from context.domains import Dataset

class TitanicModel(object):
    def __init__(self, train_fname, test_fname):
        self.dataset = Dataset()
        self.model = Model()
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # self.preprocess(df=self.train)
        # id 추출

    def preprocess(self):
        df = self.train
        ic(f'트레인 컬럼 {self.df.columns}')
        ic(f'트레인 헤드 {self.df.head()}')
        ic(self.df)
        df = self.drop_feature(df)
        df = self.crate_train(df)
        df = self.create_label(df)
        df = self.pclass_ordinal(df)
        df = self.name_norminal(df)
        df = self.fare_ratio(df)
        df = self.embarked_norminal(df)
        df = self.sex_norminal(df)
        df = self.age_ratio(df)
        return df

    @staticmethod
    def create_label(df) -> object:
        return df

    @staticmethod
    def crate_train(df) -> object:
        return df

    def drop_feature(self, df) -> object:
        a = [i for i in []]
        '''
        self.sib_sp_garbage(df)
        self.parch_garbage(df)
        self.ticket_garbage(df)
        self.cabin_garbage(df)
        return df
        '''

    '''
    Categorical vs Quantitativa
    cate -> naminal(이름) vs oridnla(순서)
    Quan -> interval(상대적) vs ratio(기준점 존재,절대)
    '''

    @staticmethod
    def pclass_ordinal(df) -> object:
        return df

    @staticmethod
    def name_norminal(df) -> object:  # 성씨(계급을 나타냄 ex.Mr,Rev)만 이용함
        return df

    @staticmethod
    def sex_norminal(df) -> object:
        return df

    @staticmethod
    def age_ratio(df) -> object:
        return df

    @staticmethod
    def sib_sp_garbage(df) -> object:
        return df

    @staticmethod
    def parch_garbage() -> object:
        pass

    @staticmethod
    def ticket_garbage() -> object:
        pass

    @staticmethod
    def fare_ratio(df) -> object:
        return df

    @staticmethod
    def cabin_garbage() -> object:
        pass

    @staticmethod
    def embarked_norminal(df) -> object:
        return df
