import socket
import random
import time

MAX_TTL = 30
PORT = 1024

def create_receiver():
    s = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_RAW,
            proto=socket.IPPROTO_ICMP
        )
    # try:
    #     s.bind(('', 0))
    # except socket.error as e:
    #     raise IOError('Unable to bind receiver socket: {}'.format(e))
    return s

def create_sender(ttl):
    s = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_DGRAM,
        proto=socket.IPPROTO_UDP
    )
    s.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

    return s

def troy_the_tracer():
    port = random.choice(range(33434,33535))
    ttl = 0
    alvo = input('Endereço do Alvo: ')
    track_list = []
    # alvo = 'google.com'

    while True:
        ttl += 1
        alvo = socket.gethostbyname(alvo);
        # print('\nTTL: {}'.format(ttl))

        receiver = create_receiver()
        receiver.settimeout(10)
        receiver.bind(('', 0))

        send_time = time.time()
        sender = create_sender(ttl=ttl)
        sender.sendto(b'',(alvo, port))

        try:
            data, addr = receiver.recvfrom(1024)
            receive_time = time.time()
            exchange_time = (receive_time - send_time) * 1000
            # print('data: {}'.format(data))
            track_list.append(addr[0])
            print(f'{ttl}\t Endereço: {addr[0]} Alvo: {alvo} tempo de salto: {exchange_time:.3f} ms')

            if addr == alvo or ttl > MAX_TTL:
                break
            
        except socket.timeout:
            print('{}\t * * *'.format(ttl))

        if addr[0] == alvo or ttl > MAX_TTL:
            print('{}\t Endereço: {} Alvo: {} /n END'.format(ttl, addr[0], alvo))
            break

    receiver.close()                
    sender.close()
    return track_list
