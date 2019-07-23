from http.server import  BaseHTTPRequestHandler, HTTPServer
import urllib
from urllib.parse import urlparse

class ncbot_RequestHandler(BaseHTTPRequestHandler):
    '''
    def do_POST(self):
        print("path: %sn" % self.path)
        o = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(o.query)
        print(params)
        self.wfile.write(bytes("Hello Client" , "utf8"))
        return
'''
    def do_GET(self):
        # parsed_path = urlparse(self.path)
        # message_parts = ['hello Client']
        # message = '<br>'.join(message_parts)
        # self.send_response(200)
        # self.end_headers()
        # self.wfile.write(message.encode('utf-8'))
        # return None
        self.route()
    def route(self):
        # 요청 값에 따라 처리할 함수를 중계함.

        if '/store' in self.path:
            data = self.path.split("/")
            if len(data) <= 2 or data[2] == "":
                self.store()
            else:
                self.storeone(data[2])
        elif '/waiting' in self.path:
            data = self.path.split("/")
            if len(data) == 3:
                self.waiting()
            elif len(data) == 4:
                self.handover()
            elif len(data) == 5 :
                self.checkmyqueue()
        elif '/account' in self.path:
            data = self.path.split("/")
            if data[2] == 'off':
                self.offlinewaiting()
            elif data[2] == 'confirm':
                self.confirm()
            elif data[2] == 'cancel':
                self.cancel()
#        else:
#            self.reponse_404_not_found()
        # if self.path == '':
        #     self.blank()
        # elif self.path == '/hello':
        #     self.hello()
        # elif self.path == '/test':
        #     self.test()
        # elif self.path == '/python':
        #     self.python()
        # elif self.path == '/barcode1':
        #     self.barcode1()
        # elif self.path == '/barcode2':
        #     self.barcode2()
        # else:
        #     self.reponse_404_not_found()

        #############################################
        #  하단 URL루트에 정보들을 입력해야 합니다. #
        #############################################

    # 가게 전체정보
    def store(self):
        self.response(200,'store')
    # 가게 단일정보
    def storeone(self, a):
        b=""
        if a == "202151745":
            b = '{"storenum": "202151745","storename": "매화반점","category": "중식","latitude": "37.538381","longitude": "127.068479","intro": "탕수육과 양꼬치로 유명한 중국요리 전문점입니다. 저녁시간에는 줄을 서서 기다려 먹어야 할 만큼 인기가 많습니다. 이 곳에 메인 요리인 양꼬치는 한 번 구워서 나오기 때문에 연하고 부드러운 최상의 상태로 맛을 볼 수 있습니다. 또한 식감이 매우 좋은 가지 튀김도 인기 메뉴입니다.","menu": "깐풍기:12000/깐쇼새우:12000/양갈비:13000/매화식가지볶음:8000/매화식탕수육:10000/양꼬치:9000/꿔바로우:8000/가지볶음:8000","inform": "주소 서울특별시 광진구 자양4동 동일로18길 105 / 전화번호 02-498-1939 / OPEN 12:00 CLOSE 01: 00", "latencytime": "30"}'
        elif a == '204684235':
            b = '{"storenum": "204684235","storename": "페스타마레","category": "이태리양식","latitude": "37.539480","longitude": "127.069581","intro": "Hand made 이탈리안 피자 & 스파게티 전문 페스타마레 입니다.","menu": "빠네까르보나라:10000/빠네씨푸드크림:11000/빠네크랩:11000/빠네포르마지오:11000/빠네맥앤치즈:11000/봉골레비앙코:7500/알리오올리오:8000","inform": "주소 서울특별시 광진구 자양4동 2-14 / 전화번호 02-497-9982 / OPEN 11:30 CLOSE20:00","latencytime": "25"}'
        elif
            
        self.response(200, b)
       
            
        self.response(200, b)
    #줄서기
    def waiting(self):
        self.response(200,'waiting')
    #미루기
    def handover(self):
        self.response(200, 'handover')
    #현재순서 확인
    def checkmyqueue(self):
        self.response(200,'checkmyqueue')
    #오프줄서기
    def offlinewaiting(self):
        self.response(200, 'offlinewaiting')
    #확인
    def confirm(self):
        self.response(200,'confirm')
    #취소
    def cancel(self):
        self.response(200, 'cancel')


    # def blank(self):
    #     self.response(200,'hello world')
    # def hello(self):
    #     self.response(200,'안녕하세요!')
    # def test(self):
    #     self.response(200,'테스트 성공!')
    # def python(self):
    #     self.response(200,'파이썬 서버 테스트')
    # def barcode1(self):
    #     self.response(200,'8802342034956')
    # def barcode2(self):
    #     self.response(200,'8809683905938')
    
#    def response_404_not_found(self):
#        self.response(404,'요청하신 문서를 찾을 수 없습니다.')
    def response(self,status_code,body):
        #상태코드 전송
        self.send_response(status_code)

        #헤더 전송
        self.send_header('Content-type','text/plain; charset=utf-8')
       # self.send_header('Content-type', 'application/json')

        self.end_headers()

        #본문 전송
        self.wfile.write(body.encode('utf-8'))

# 테스트입니다
def run():
    print('Starting server')
    server_address = ('192.168.0.8', 8000)
    httpd = HTTPServer(server_address, ncbot_RequestHandler)

    print("Running the server")
    httpd.serve_forever()

run()
