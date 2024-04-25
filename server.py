import socket
import json
import time
import os

def GET_Responce_Content(reponce):
    return reponce.split("?")[1].split(" ")[0]



def main():
    ALLUSERS = []
    ip = "127.0.0.1"
    port = 12345
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_server.bind((ip, port))
    socket_server.listen(5)

    print(f"http://{ip}:{port}")

    while True:
        socket_client, socket_adrres = socket_server.accept()
        request = socket_client.recv(1024)
        request_content = request.decode()
        FULL_RESPONCE = GET_Responce_Content(request_content)
        print(f">> {socket_adrres} >> {FULL_RESPONCE}")
        
        isExist = False
        
        if len(ALLUSERS) > 0:
            for el in range(0, len(ALLUSERS)):
                if ALLUSERS[el].split("&")[0].split("=")[1] == FULL_RESPONCE.split("&")[0].split("=")[1]:
                    isExist = True
                    del ALLUSERS[el]
                    ALLUSERS.append(FULL_RESPONCE)
        else:
            isExist = False

        if isExist == False: 
            ALLUSERS.append(FULL_RESPONCE)
        
        print(ALLUSERS)
        
        call_data = {"call": ALLUSERS}
        json_data = json.dumps(call_data)
        responce= (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json\r\n"
            "Content-Length: {}\r\n"
            "\r\n"
            "{}".format(len(json_data), json_data)
        )
        socket_client.sendall(responce.encode())

        socket_client.close()


main()