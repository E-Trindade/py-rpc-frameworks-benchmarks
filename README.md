Parte do código utilizou a implementação de exemplo do gRPC disponibilizada em (https://grpc.io/docs/).

# Execução

Requisitos:
- Python 3
- grpcio-tools

Para rodar o xml-rpc:

```
$ python xmlrpc_server.py
(Em outro terminal)
$ python xmlrpc_client.py
```

Para rodar o grpc:

```
$ cd grpc
$ python grpc_server.py
(Em outro terminal)
$ python grpc_client.py
```

Os arquivos usados para gerar o código do gRPC se encontra na pasta grpc/protos

O código fonte do projeto também encontra-se em https://github.com/E-Trindade/py-rpc-frameworks-benchmarks
