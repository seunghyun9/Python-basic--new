import numpy as np
import pandas as pd
from icecream import ic
from context.models import Model
from context.domains import Dataset


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):  # 데이터를 계속해서 가공(정제)한다.
        this = self.dataset
        that = self.model
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare',
                   'Cabin', 'Embarked']
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']  # 검증을 위해서 id와 label을 사용
        this.label = this.train['Survived']
        # Entity에서 object로 전환
        this.train = this.train.drop('Survived', axis=1)  # 열방향은 숫자1로 표시
        this = self.drop_feature(this, 'Ticket', 'Parch', 'Cabin', 'SibSp')
        # self.kwargs_sample(name='이순신') # kwargs 예제
        this = self.extract_title_from_name(this) # Title을 뽑아냄
        title_mapping = self.remove_duplicate(this)
        this = self.title_nominal(this, title_mapping) #mapping ex) 학교 = school(1) 자연어를 기계어로 변환
        this = self.drop_feature(this, 'Name')
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')

        '''
        this = self.create_train(this)
        this = self.create_label(this)
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.embarked_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        '''
        self.print_this(this)
        self.df_info(this)
        return this

    @staticmethod
    def print_this(this):
        print('*' * 100)
        ic(f'1. Train 의 타입 : {type(this.train)}\n')
        ic(f'2. Train 의 컬럼 : {this.train.columns}\n')
        ic(f'3. Train 의 상위 1개 : {this.train.head(1)}\n')
        ic(f'4. Train 의 null의 개수 : {this.train.isnull().sum()}\n')
        ic(f'5. Test 의 타입 : {type(this.test)}\n')
        ic(f'6. Test 의 컬럼 : {this.test.columns}\n')
        ic(f'7. Test 의 상위 1개 : {this.test.head(1)}\n')
        ic(f'8. Test 의 null의 개수 : {this.test.isnull().sum()}\n')
        ic(f'9. id 의 타입 : {type(this.id)}\n')
        ic(f'10. id 의 상위 10개 : {this.id[:10]}\n')
        print('*' * 100)

    @staticmethod
    def df_info(this):
        [print(f'{i.info()}') for i in [this.train, this.test]]
        ic(this.train.head(3))
        ic(this.test.head(3))

    def create_this(self, dataset) -> object:
        this = dataset
        this.train = self.train
        this.test = self.test
        this.id = self.id
        return this

    @staticmethod
    def crate_train(this) -> object:
        return this

    @staticmethod
    def drop_feature(this, *feature) -> object:  # *= All,몇개인지 몰라 모든 컬럼들은 들고 온다는 뜻
        '''
        this.train = this.train.drop('SibSp', axis=1)
        this.train = this.train.drop('Parch', axis=1)
        this.train = this.train.drop('Cabin', axis=1)
        this.train = this.train.drop('Ticket', axis=1)
        '''
        ic(type(feature))  # 타입은 튜플(상수)
        [i.drop(j, axis=1, inplace=True) for i in [this.train, this.test] for j in feature]
        # [i.drop(list(feature), axis=1, inplace=True) for i in [this.train, this.test]]
        '''
        a = [i for i in feature]
        this.train = this.train.drop(a, axis=1)
        this.test = this.test.drop(a, axis=1)
        '''

        '''
        self.sib_sp_garbage(df)
        self.parch_garbage(df)
        self.ticket_garbage(df)
        self.cabin_garbage(df)
        '''

        return this

    '''
    Categorical vs Quantitativa
    cate -> naminal(이름) vs oridnla(순서)
    Quan -> interval(상대적) vs ratio(기준점 존재,절대)
    '''

    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        ic(type(kwargs))  # ic| type(feature): <class 'tuple'>
        {print(''.join(f'key:{i}, val:{j}')) for i, j in kwargs.items()}  # key:name, val:이순신

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def name_nominal(this) -> object:  # 성씨(계급을 나타냄 ex.Mr,Rev)만 이용함
        combine = [this.train, this.test] # this는 데이터셋 형식이다, 리스트형식으로 바꿔서 수정가능하게함
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.',expand=False)
            # ('[]')< 정규식으로 각 캐릭터를 뜻함 expands=False 뒤에 내용은 버리라는뜻
            ic(dataset['Title'])
        return this

    @staticmethod
    def extract_title_from_name(this) -> None:
        for these in [this.train, this.test]:
            these['Title'] = these.Name.str.extract('([A-Za-z]+)\.', expand=False)
        # ic(this.train.head(5))
        return this

    @staticmethod
    def remove_duplicate(this) -> None:
        a = []
        for these in [this.train, this.test]:
            a += list(set(these['Title']))
        a = list(set(a))
        # print(f'>>> {a}')
        '''
        ['Mr', 'Sir', 'Major', 'Don', 'Rev', 'Countess', 'Lady', 'Jonkheer', 'Dr',
        'Miss', 'Col', 'Ms', 'Dona', 'Mlle', 'Mme', 'Mrs', 'Master', 'Capt']
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme' ]
        Mr : ['Mlle']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs':3, 'Master':4, 'Royal':5, 'Rare': 6}
        return title_mapping

    @staticmethod
    def title_nominal(this, title_mapping) -> object:
        for these in [this.train, this.test]:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms') #replace 는 문자를 문자로 바꾼다
            # Master 는 변화없음
            # Mrs 는 변화없음
            these['Title'] = these['Title'].fillna(0) #fillna는 결측값은 0 으로 채운다는 뜻
            these['Title'] = these['Title'].map(title_mapping)
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        gender_mapping = {'male': 0, 'female': 1}
        for these in [this.train, this.test]:
            these['Gender'] = these.Sex.str.extract('([A-Za-z]+)')
            these['Gender'] = these['Gender'].map(gender_mapping) #.map 은 대신한다. 딕셔너리를 전달 하거나, 함수를 전달하여 다른 값으로 변경할 수 있다.
        return this

    @staticmethod
    def age_ratio(this) -> object:
        train = this.train
        test = this.test
        age_mapping = {'Unknown':0 , 'Baby': 1, 'Child': 2, 'Teenager' : 3, 'Student': 4,
                       'Young Adult': 5, 'Adult':6,  'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5) # Unknown 범위를 -1 <Unknown <0으로 정했으니 그 안에 들어가야함
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] #np.inf:특정 할 수 없는 값= 무한값
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        for these in train, test:
            # pd.cut() 을 사용하시오. 다른 곳은 고치지 말고 다음 두 줄만 코딩하시오 ,pd.cut = 데이터 값들을 특정 구간에 따라서 범주화 할 때, 사용
            these['AgeGroup'] = pd.cut(these['Age'], bins, right=True, labels=labels)# right=True 입력하면 60 < Senior <= np.inf 설정된다.
            these['AgeGroup'] = these['AgeGroup'].map(age_mapping)
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        embarked_mapping = {'S':1,'C':2,'Q':3}
        #this.train = this.train.fillna({'Embarked':'S'}) # 통상적으로 선착지가 null값으로 판단된 사람은 S로대체한다
        for these in [this.train, this.test]:
            these['Embarked'] = these['Embarked'].map(embarked_mapping)
            these['Embarked'] = these['Embarked'].fillna(1)
        return this
