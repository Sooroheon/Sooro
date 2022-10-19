class calculator:

    def input_ecpr(self):
        expr = input('수식을 입력하세요 >> ')
        self.expr = expr

    def calculate(self):
        return eval(self.expr)

calc = calculator()
calc.input_ecpr()
print('수식 결과는 {}입니다.'.format(calc.calculate()))
