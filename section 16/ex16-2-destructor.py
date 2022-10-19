'''
인스턴스가 소멸될 때 자동으로 호출된다.

'''

class Service:
    def __init__(self, service):
        self.service = service
        print('{} Service가 시작되었습니다.'.format(self.service))

        del __del__(self):
            print('{}서비스가 종료되었습니다.'.format(self.service))