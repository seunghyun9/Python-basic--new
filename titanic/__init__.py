#https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic.views import TiatanicView
from titanic.models import TitanicModel
from titanic.templates import TitanicTemplates
if __name__ == '__main__':
    while 1:
        view = TiatanicView()

        menu = input('1.템플릿 2.전처리')
        if menu == '1':
            print(' #### 1. 템플릿 #### ')
            templates = TitanicTemplates(fname='train.csv')
            templates.visualize()
            # view.preprocess('train.csv','test.csv')
            break
        elif menu == '2':
            print(' #### 2. 전처리 #### ')
            model = TitanicModel()
            model.learning(train_fname='train.csv',
                                 test_fname='test.csv')
            break
