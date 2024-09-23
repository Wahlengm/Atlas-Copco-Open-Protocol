from OpenProtocolInterpreter import *
from threading import Thread
import socket
import time
import select

class Tool:
    def __init__(self, host, port):
        self.buffer_size = 1024
        self.timeout = True
        self.host = host
        self.port = port
        
        self.keep_alive_message = '00209999001000000000' + chr(0)
        self.connect_attempts = 0
    
        #ESTABLISH A CONNECTION WITH THE TOOL
        self.connect()
        self.disconnect()
      
    def send(self, message):
        self.client_socket.send(message.encode())
        
    def receive(self, timeout):
        ready = select.select([self.client_socket], [], [], timeout)
        return interpret_message(self.client_socket.recv(self.buffer_size).decode())
        
    def subscribe_to_tightening_results(self):
        #SEND MID0060 TO START SUBSCRIBING TO LAST TORQUE DATA
        print('Attempting to Subscribe')
        self.send(create_message(60))
        
        #CHECK TO SEE IF SUBSCRIPTION WAS ACCEPTED
        if self.receive(1)['MID'] == 5: print('Subscription Successful')
        else: print('Subscription Failed')
        
    def set_program(self, program_id):
        self.send(create_message(18, program_id=program_id))
        response = self.receive(1)
        if  response['MID'] == 5: 
            print(f'Program ID Set to {program_id}')
            return True
        else: 
            print(f'Program ID Not Set\n{response}')
            return False
        
    def acknowledge_torque_data(self):
        self.send(create_message(62))
        
    def unlock_tool(self):
        self.send(create_message(43))
        if self.receive(1)['MID'] == 5: print('Tool Unlocked')
        else: print('Tool Failed to Unlock')
        
    def lock_tool(self):
        self.send(create_message(42))
        if self.receive(1)['MID'] == 5: print('Tool Locked')
        else: print('Tool Failed to Lock')
        
    def wait_for_ok_result(self, file_path, window):
        results = []
        self.unlock_tool()
        while self.client_socket:
            tightening_data = None
            while not tightening_data:
                response = self.keep_alive()
                try: tightening_data = self.receive(7)
                except socket.error: print('No Tightening')
                if window.is_restarting: break
                if not response == '':
                    if response['MID'] == 61: tightening_data = response
            if window.is_restarting: break
            self.acknowledge_torque_data()
            results.append(tightening_data)
             
            if tightening_data['TIGHTENING STATUS'] == 'OK': break
        self.lock_tool()
        return results
    
    def write_torque_result(self, file_path, data):
        with open(file_path, 'a') as file:
            file.write(f'Tightening: {data}\n\n')
    
    def keep_alive(self):
        self.send(self.keep_alive_message)
        return self.receive(1)
    
    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.client_socket.setblocking(0)
        
        #SEND MID0001 TO START COMMUNICATION WITH TOOL
        print('Establishing Communication with Tool')
        self.send(create_message(1))
        response = self.receive(3)
        
        #CHECK TO SEE IF COMMUNICATION WITH TOOL WAS SUCCESSFUL
        try:
            if response['MID'] == 2: 
                print('Communication Successful')   
                self.subscribe_to_tightening_results()
                self.lock_tool()
                self.connect_attempts = 0
            else: 
                print('Communication Failed')
                self.disconnect()
        except: print('Communication Failed')

    
    def turn_lights_on(self):
        self.send(create_message(254, states='00000000', device_id=6))
        print(self.receive(2))
    def disconnect(self):
        try:
            self.set_program(0)
            self.send(create_message(3))
            self.client_socket.close()
            self.client_socket = None
            print('Tool Disconnected')
        except: print('Already Disconnected')