from icecream import ic
from context.domains import Dataset
from context.models import Model
import matplotlib.pyplot as plt

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

    def visualize(self)->None:
        this = self.entity
        self.draw_survived(this)
        self.draw_pclass(this)
        self.draw_sex(this)
        self.draw_embarked(this)

    @staticmethod
    def draw_survived(this) ->None:
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        this['Survived']
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
