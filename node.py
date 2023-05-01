import random
import re
import sys
import os
from typing import Tuple
import grpc
import threading
from concurrent import futures
from datetime import datetime, timedelta
from time import time, sleep, mktime
from itertools import combinations
import multiprocessing

import bookshop_pb2
import bookshop_pb2_grpc


#--------------- configuration --------------#

MIN_PID, MAX_PID = 1, 3
# pid lower than min_pid yields min_pid and pid higher than max_pid yields max_pid
PID = max(min(int(sys.argv[1]), MAX_PID), MIN_PID)
PORTS = [20040 + i for i in range(1, MAX_PID + 1)]


#----------------- servicer -----------------#

class BookshopServicer(bookshop_pb2_grpc.BookshopServicer):
    def __init__(self):
        self.processes = set()

    def write(self, request, context):
        self.storage[request.key] = (request.value, time())
        return bookshop_pb2.WriteResponse()
    
    def read(self, request, context):
        try:
            return bookshop_pb2.ReadResponse(value=self.storage[request.key], timestamp=time())
        except KeyError:
            # When key is not present, respond without value
            return bookshop_pb2.ReadResponse(timestamp=time())
    
    def create_processes(self, request, context):
        self.processes.update([BookshopProcess(name=f"Node{PID}-ps{i+1}") for i in range(request.num_processes)])
        return bookshop_pb2.CreateProcessesResponse()

    def get_processes(self, request, context):
        return bookshop_pb2.GetProcesses(process_list=[ps.name for ps in self.processes])


class BookshopProcess:
    def __init__(self, name:str):
        self.name = name
        self.db = {}
        self.predecessor = None
        self.successor = None

    def get_value(self, key:str) -> Tuple[str, float]:
        return self.db[key]
    
    def set_value(self, key:str, value:str) -> None:
        self.db[key] = (value, time())


#------------------ server ------------------#

class BookshopServer:
    def __init__(self):
        self.server = None
    
    def serve(self) -> None:
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
        bookshop_pb2_grpc.add_BookshopServicer_to_server(BookshopServicer(), self.server)
        self.server.add_insecure_port(f'[::]:{PORTS[PID]}')
        self.server.start()
        print_n(f"Server started, CONNECTED to port {PORTS[PID]}")
        self.server.wait_for_termination()


#------------------ client ------------------#

class BookshopClient:
    def __init__(self):
        pass

    def create_processes(self, num_processes:int) -> None:
        with grpc.insecure_channel(f"localhost:{PORTS[PID]}") as channel:
            stub = bookshop_pb2_grpc.TicTacToeStub(channel)
            stub.create_processes(bookshop_pb2.CreateProcessesRequest(num_processes=num_processes))


#------------------- main -------------------#

def print_n(string:str) -> None:
    print(string)
    print(f"Node-{PID}> ",end="")
    return


def main():
    client = BookshopClient()
    server = BookshopServer()

    chain_exists = False
    
    print_n("Waiting for command")
    while True:
        command = input()
        args = command.split(" ")

        if args[0].lower() == "local-store-ps":
            client.create_processes(int(args[1]))
            
        elif args[0].lower() == "create-chain":
            if chain_exists:
                print("Warning! A chain already exists. Do you want to re-creating the chain. y/n ")
                command = input().lower()
                if command == "y":
                    # re-creating the chain
                    pass

        elif args[0].lower() == "list-chain":
            # list the current status of the chain
            pass

        elif args[0].lower() == "write-operation":
            data = args[1].split(", ")
            name = data[0].strip("<").strip("\"")
            price = float(data[1].strip(">"))

        elif args[0].lower() == "list-books":
            # lists the available books in the store
            pass

        elif args[0].lower() == "read-operation":
            name = args[1].strip("\"")

        elif args[0].lower() == "time-out":
            time = int(args[1])

        elif args[0].lower() == "data-status":
            # list the status of each data item
            pass

        elif args[0].lower() == "remove-head":
            # remove the current head from the chain
            pass

        elif args[0].lower() == "restore-head":
            # restore the most recent removed head back to chain
            pass

        else:
            print_n("Command not found")


if __name__ == "__main__":
    main()