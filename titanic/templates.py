from icecream import ic

import titanic
from context.domains import Dataset
from context.models import Model
from titanic.models import TitanicModel

class TitanicTemplates(object):
    def __init__(self, train_fname, test_fname):
        self.dataset = Dataset()
        self.model = Model()
        self.titanic = TitanicModel(train_fname,test_fname)



