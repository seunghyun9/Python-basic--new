#https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic.views import TiatanicView
from titanic.models import TitanicModel
from titanic.templates import TitanicTemplates
if __name__ == '__main__':
    while 1:


        menu = input('1.템플릿 2.전처리')
        if menu == '1':
            print(' #### 1. 템플릿 #### ')
            view = TiatanicView()
            templates = TitanicTemplates(train_fname='train.csv',
                                 test_fname='test.csv')
            # view.preprocess('train.csv','test.csv')
            break
        elif menu == '2':
            print(' #### 2. 전처리 #### ')
            view = TiatanicView()
            model = TitanicModel(train_fname='train.csv',
                                 test_fname='test.csv')
            break
