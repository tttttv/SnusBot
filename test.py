class Test():
    def __init__(self):
        self.name = self.met()


class SubTest(Test):
    def met(self):
        return ('1')


st = SubTest()
print(st.name)


### city=NNO#