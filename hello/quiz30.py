import numpy as np
import pandas as pd
from icecream import ic
from hello import Quiz20
from hello.domains import myRandom, members
import random
import string
from context.models import Model

class Quiz30:
    def quiz30_df_4_by_3(self) -> None:
        """
            데이터프레임 문제 Q02
        ic| df:     A   B   C
                1   1   2   3
                2   4   5   6
                3   7   8   9
                4  10  11  12

        df = pd.DataFrame([[1,2,3],
                          [4,5,6],
                          [7,8,9],
                          [10,11,12]], index=range(1,5), columns=['A','B','C'])
        # 위 식을 리스트결합 형태로 분해해서 조립하시오
        ic(df)
        """
        columns = Quiz20.askicode(65, 68)
        d1 = [i for i in range(1, 13)]
        d2 = [d1[i:i + 3] for i in range(0, len(d1), 3)]

        df = pd.DataFrame(d2, index=range(1, 5), columns=columns)
        ic(df)

        d = {'1': range(1, 4),
             '2': range(4, 7),
             '3': range(7, 10),
             '4': range(10, 13)}
        df2 = pd.DataFrame.from_dict(d, orient="index", columns=['A', 'B', 'C'])
        ic(df2)
        return None

    def quiz31_rand_2_by_3(self) -> object:
        # 1
        # data = Quiz30.random_cutter(10, 100, 6, 3)
        # df = pd.DataFrame(data, index=range(0, 2), columns=range(0, 3))
        # 2
        l1 = [[myRandom(0, 100) for i in range(3)] for i in range(2)]
        l2 = [str(i) for i in range(2)]
        columns = [str(i) for i in range(3)]
        df2 = pd.DataFrame(l1, index=l2, columns=columns)
        # 3 넘파이 사용한 예제
        df = pd.DataFrame(np.random.randint(10, 100, size=(2, 3)))
        ic(df)
        return None

    @staticmethod
    def id(chr_size) -> str: return ''.join([random.choice(string.ascii_letters) for i in range(chr_size)])

    def quiz32_df_grade(self) -> object:
        '''
                데이터프레임 문제 Q04.
                국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
                 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기

                  ic| df4:        국어  영어  수학  사회
                            lDZid  57  90  55  24
                            Rnvtg  12  66  43  11
                            ljfJt  80  33  89  10
                            ZJaje  31  28  37  34
                            OnhcI  15  28  89  19
                            claDN  69  41  66  74
                            LYawb  65  16  13  20
                            QDBCw  44  32   8  29
                            PZOTP  94  78  79  96
                            GOJKU  62  17  75  49
        '''
        scores = np.random.randint(0, 100, (10, 4))  # 자체가 리스트화됨
        idx = [self.id(5) for i in range(10)]
        subjects = ['국어', '영어', '수학', '사회']
        df1 = pd.DataFrame(scores, index=idx, columns=subjects)
        print('-------------------------------------')
        data2 = np.random.randint(0, 100, (10, 4))
        idx2 = [self.id(5) for i in range(10)]
        df2 = pd.DataFrame.from_dict(dict(zip(idx2, data2)), orient="index", columns=subjects)
        print('-------------------------------------')
        zop = {i: j for i, j in zip(idx2, data2)}
        df3 = pd.DataFrame.from_dict(zop, orient="index", columns=subjects)

        ic(df1)
        ic(df2)
        ic(df3)
        return None

    def quiz33_df_loc(self) -> object:
        a = ['a', 'b', 'c', 'd']
        d = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
             {'a': 100, 'b': 200, 'c': 300, 'd': 400},
             {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
        d2 = [dict(zip(['a', 'b', 'c', 'd'], np.random.randint(1, 100, 4))) for i in range(3)]
        df = pd.DataFrame(d2)
        df2 = self.createDf(keys=['a', 'b', 'c', 'd'], vals=np.random.randint(1, 100, 4), len=3)
        students = members()
        scores = np.random.randint(1, 100, (24,4))
        subjects = ['자바', '파이썬', '자바스크립트', 'SQL']
        student_scores ={student:score for student,score in zip(students,scores)}
        df3 = pd.DataFrame.from_dict(student_scores,orient="index",columns=subjects)
        df4 = pd.DataFrame(np.random.randint(1, 100, (24, 4)), index=members(), columns=subjects)
        #ic(df4)
        # model.save_model(fname='grade.csv', dframe=students_scores_df)
        model = Model()
        grade_df = model.new_model(fname='grade.csv')
        #ic(grade_df)
        print('Q1. 파이썬의 점수만 출력하시오')
        python_scores = grade_df.loc[:,'파이썬']
        ic(type(python_scores))
        ic(python_scores)
        print('Q2. 조현국의 점수만 출력하시오')
        cho_scores = grade_df.loc['조현국']
        ic(type(cho_scores))
        ic(cho_scores)
        print('Q3. 조현국의 과목별 점수만 출력하시오')
        cho_subjects_scores = grade_df.loc[['조현국']]
        ic(type(cho_subjects_scores))
        ic(cho_subjects_scores)


        return None

    @staticmethod
    def createDf(keys, vals, len):
        return pd.DataFrame([dict(zip(keys, vals)) for _ in range(len)])

    def quiz34_iloc(self) -> str:
        '''
              ic| df2.iloc[0]:
                       a    96
                       b    57
                       c    77
                       d    34
                       Name: 0, dtype: int32
              ic| df.iloc[[0]]:
                            a   b   c   d
                        0  44  60  58  94
              ic| df.iloc[[0,1]]:
                              a   b   c   d
                          0  29  96   3  39
                          1  59   7  86  16
              ic| df.iloc[:3]:
                          a   b   c   d
                       0  15  69  76  45
                       1  51  44   3  81
                       2  33   5   3  21
              ic| df.iloc[[True, False, True]]:
                            a   b   c   d
                        0  44  44  62  68
                        2  44  38  19  60
              ic| df.iloc[lambda x: x.index % 2 == 0]:
                          a   b   c   d
                       0  67  52   4  54
                       2  45  94  98  92
              df.iloc[0, 1]:
                              76
              ic| df.iloc[[0, 2], [1, 3]]:
                                       b   d
                                   0  42   9
                                   2  92  25
                       ic| df.iloc[1:3, 0:3]:
                            a   b   c
                         1  20  43  49
                         2   9  27  43
              ic| df.iloc[:, [True, False, True, False]]:
                                  a   c
                              0   7  57
                              1  25  21
                              2  83  15
              ic| df.iloc[:, lambda df: [0, 2]]:
                                 a   c
                             0  57  44
                             1  46   2
                             2  87  39
                       '''
        return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None
