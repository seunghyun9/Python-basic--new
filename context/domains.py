# context, fname, train, test, id , label
# class Dataset:
from abc import ABC
from dataclasses import dataclass
from abc import *

import pandas as pd
import googlemaps


@dataclass
class Dataset:
    context: str
    sname: str
    dname: str
    fname: str
    train: str
    test: str
    id: str
    label: str

    @property
    def dname(self) -> str: return self._dname

    @dname.setter
    def dname(self, dname): self._dname = dname

    @property
    def sname(self) -> str: return self._sname

    @sname.setter
    def sname(self, sname): self._sname = sname

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label


@dataclass
class File(object):
    context: str
    fname: str
    dframe: object

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def dframe(self) -> str: return self._dframe

    @dframe.setter
    def dframe(self, dframe): self._dframe = dframe


class PrinterBase(metaclass=ABCMeta):  # abc 모듈을 가지고 오면 추상클래스
    @abstractmethod
    def dframe(self):
        pass
    # new file, csv, xls, json


class ReaderBase(metaclass=ABCMeta):
    @abstractmethod
    def new_file(self, file) -> str:
        pass

    @abstractmethod
    def csv(self) -> object:
        pass

    @abstractmethod
    def xls(self) -> object:
        pass

    @abstractmethod
    def json(self) -> object:
        pass


# Reader
class Reader(ReaderBase):  # Reader가 ReaderBase의 자식이라는 뜻이다.
    def new_file(self, file) -> str:  # 리턴만O str, 서플라이어 // 둘다 있으면 펑션(함수)
        return file.context + file.fname

    def csv(self, fname) -> object:
        return pd.read_csv(f'{self.new_file(fname)}.csv', encoding='UTF-8', thousands=',')

    def xls(self, fname, hearder, cols) -> object:
        return pd.read_excel(f'{self.new_file(fname)}.xls', header=hearder, usecols=cols)

    def json(self, fname) -> object:
        return pd.read_json(f'{self.new_file(fname)}.json', encoding='UTF-8')

    def gmaps(self) -> object:
        return googlemaps.Client(key='')


# Printer
class Printer(PrinterBase):
    def dframe(self, this):  # 파라미터 O 리턴X 컨슈머
        print('*' * 100)
        print(f'1. Target type \n {type(this)} ')
        print(f'2. Target column \n {this.columns} ')
        print(f'3. Target top 1개 행\n {this.head(1)} ')
        print(f'4. Target bottom 1개 행\n {this.tail(1)} ')
        print(f'4. Target null 의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)


if __name__ == '__main__':
    r = Reader()
    r.csv(r.new_file('...'))
