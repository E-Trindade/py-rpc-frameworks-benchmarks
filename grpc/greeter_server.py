# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import time


import grpc

import helloworld_pb2
import helloworld_pb2_grpc
import functions_pb2
import functions_pb2_grpc
import functions

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        from datetime import datetime
        datetime.now()
        request.name = request.name + ' '+ str(datetime.now())
        return helloworld_pb2.HelloReply(message='Hello, %s!' %request.name)
    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello again, %s!' % request.name)


class EpFunctions(functions_pb2_grpc.EpFunctionsServicer):
    from functions import Employee 
    from datetime import datetime

    def f1_noop(self, request, context):
        from datetime import datetime
        print ('f1_noop: '+str(datetime.now())) 
        functions.f1_noop()
        return functions_pb2.Empty()
    def f2_square(self, request, context):
        from datetime import datetime
        print ('f2_square: '+str(datetime.now()))
        return functions_pb2.NumberReply(num=functions.f2_square(request.num))
    def f3_mean_8(self, request, context):
        from datetime import datetime
        reply = functions.f3_mean_8(request.n1,request.n2,request.n3,request.n4,request.n5,request.n6,request.n7,request.n8)
        print ('f3_mean_8: '+str(datetime.now()))
        return functions_pb2.MeanReply(n1=reply)
    def f4_str_is_palindrome(self, request, context):
        from datetime import datetime
        print ('f4_str_is_palindrome: '+str(datetime.now()))
        print(request.palindrome)
        reply = functions.f4_str_is_palindrome(request.palindrome)
        return functions_pb2.PalindromeReply(palindrome=reply)
    def f5_exp_rep_string(self, request, context):
        from datetime import datetime
        print ('f5_exp_rep_string: '+str(datetime.now()))
        n = request.num * len(request.num)
        return functions_pb2.LongReply(num=n)
    def f6_create_employee(self, request, context):
        from datetime import datetime
        print ('f6_create_employee: '+str(datetime.now()))
        e = functions.Employee
        e.id = request.id
        e.name = request.name
        e.age = request.age
        e.manager = request.manager
        functions.f6_create_employee(e)
        return functions_pb2.Empty()
    def f7_get_employee(self, request, context):
        from datetime import datetime
        print ('f7_get_employee: '+str(datetime.now()))
        e = functions.f7_get_employee(request.id)
        return functions_pb2.Employee(id=e.id,name=e.name,age=e.age,manager=e.manager)
    def f8_get_employee_complete(self, request, context):
        from datetime import datetime
        print ('f8_get_employee_complete: '+str(datetime.now()))
        e = functions.f8_get_employee_complete(request.id)
        print('id:'+str(e.id)+' n:'+str(e.name)+' a:'+str(e.age)+' m:'+str(e.manager.id)+'.'+str(e.manager.name)+'.'+str(e.manager.age)+'.'+str(e.manager.manager))
        m = functions_pb2.Employee(id=e.manager.id,name=e.manager.name,age=e.manager.age,manager=e.manager.manager)
        ec = functions_pb2.Employee(id=e.id,name=e.name,age=e.age,manager=m)
        return functions_pb2.EmployeeComplete(e=ec)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    #adicionando os servicos do EP ao servidor
    functions_pb2_grpc.add_EpFunctionsServicer_to_server(EpFunctions(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
