from icecream import ic
from context.domains import Dataset
from context.models import Model
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc, font_manager

rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())

'''
데이터 시각화
엔티티(개체)를 차트로 표현 하는 것

모든 feature 를 다 그려야 하지만, 시간관계상
survived, pclass, sex, embarked 의 4개만 그리겠습니다.
템플릿 메소드 패턴으로 구성하시오

'''
class TitanicTemplates(object):
    def __init__(self, fname):
        self.dataset = Dataset()
        self.model = Model()
        self.entity = self.model.new_model(fname)
        this = self.entity
        ic(f'트레인의 타입: {type(this)}')
        ic(f'트레인의 컬럼: {this.columns}')
        ic(f'트레인의 상위5행: {this.head}')
        ic(f'트레인의 하위5행: {this.tail}')

    def visualize(self)->None: #원데이터에 가공하는 것
        this = self.entity
        self.draw_survived(this)
        #self.draw_pclass(this)
        #self.draw_sex(this)
        #self.draw_embarked(this)

    @staticmethod
    def draw_survived(this) ->None:
        f, ax =plt.subplots(1, 2, figsize=(18, 8))  # nrows=1, ncols=2,figisize 18inch 8inch
        this['Survived'].value_counts().plot.pie(explode=[0,0.1], autopct='%1.1f%%',ax=ax[0], shadow=True)
        ax[0].set_title('0.사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

    @staticmethod
    def draw_pclass() -> None:
        plt.show()

    @staticmethod
    def draw_sex() -> None:
        plt.show()

    @staticmethod
    def draw_embarked() -> None:
        plt.show()
