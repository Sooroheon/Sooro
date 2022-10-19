'''

mutable - 메모리 값을 변경 가능
       리스트list, 세트set, 딕셔너리dict

'''

me = [1,2,3]
print(id(me))
me.append(4)
print(id(me))

'''
immutable - 메모리 값 변경 불가
       정수int, 실수float, 문자열str, 튜플tuple
'''
me = 10
print(id(me))
me +=1
print(id(me))



