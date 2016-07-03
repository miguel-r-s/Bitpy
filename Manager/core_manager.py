import os
from Packets.PacketCreator import *
from Packets.control_messages import *
from Packets.data_messages import *

__author__ = 'alexisgallepe'


class Manager:
    def __init__(self, senderQueue):
        self.senderQueue = senderQueue
        self.get_order_client()

    def get_order_client(self):

        # send first Version + verack
        self.order(0)
        self.order(1)

        print "Version & VerAck sent, connected to node."

        while True:
            print "Enter your command number:"
            print "11: Exit"
            print "(0: Version)"
            print "(1: verack)"
            print "2: getAddr"
            print "3: Ping"
            print "4: GetBlocks (block hash already defined)"

            cmd = input(">")
            self.order(cmd)

    def order(self, cmd):
        packet = ""

        if cmd == 11:
            os._exit(0)

        elif cmd == 0:
            version = Version.EncodeVersion()
            packet = PacketCreator(version).forge_packet()

        elif cmd == 1:
            verack = Verack.EncodeVerack()
            packet = PacketCreator(verack).forge_packet()

        elif cmd == 2:
            getAddr = GetAddr.EncodeGetaddr()
            packet = PacketCreator(getAddr).forge_packet()

        elif cmd == 3:
            ping = Ping.EncodePing()
            packet = PacketCreator(ping).forge_packet()

        elif cmd == 4:
            print "Enter your block Hash(es): (you can write as many blocks as you want, separated by a coma)"
            print "i.e: 5c3e6403d40837110a2e8afb602b1c01714bda7ce23bea0a0000000000000000,951b7b286867a7e074865cd08a1ed99783bdfb189c90e6400000000000000000"
            hashes = raw_input(">")
            hashes = [ hash.strip() for hash in hashes.split(',') ]
            print hashes
            getBlocks = GetBlocks.EncodeGetblocks(hashes)
            packet = PacketCreator(getBlocks).forge_packet()

        self.senderQueue.put(packet)

def send_version_msg():
    version = Version.EncodeVersion()
    packet = PacketCreator(version).forge_packet()

def send_verack_msg():
    verack = Verack.EncodeVerack()
    packet = PacketCreator(verack).forge_packet()


def send_getAddr_msg():
    getAddr = GetAddr.EncodeGetaddr()
    packet = PacketCreator(getAddr).forge_packet()


def send_ping_msg():
    ping = Ping.EncodePing()
    packet = PacketCreator(ping).forge_packet()

def send_getBlocks_msg():
    getBlocks = GetBlocks.EncodeGetblocks(["0000000000000000046e09c981bfdb38799de1a80dc568470e7a768682b7b159"])
    packet = PacketCreator(getBlocks).forge_packet()