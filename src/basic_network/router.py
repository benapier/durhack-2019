from __future__ import annotations
from edge import Edge
from packet import Packet


class Router:
    def __init__(self, address: str):
        self.edges = []
        self.connected_to = []
        self.address = address
        self.distance_vector = {}  # Empty distance vector initially constructed from information about neighbours
        for address in self.connected_to:
            for edge in self.edges:
                if edge.a.address == address:
                    self.distance_vector[address] = edge.a.ticks_per_packet
                    break
                elif edge.b.address == address:
                    self.distance_vector[address] = edge.b.ticks_per_packet
                    break

    def send_distance_vector(self):
        """Sends current distance vector to all neighbours"""
        for edge in self.edges:
            if edge.a == self:
                self.send_packet(edge.b, Packet({"HEAD": "DV", "CONTENT": self.distance_vector}))
            else:
                self.send_packet(edge.a, Packet({"HEAD": "DV", "CONTENT": self.distance_vector}))

    def update_distance_vector(self, received_vector: Packet):
        """Upon receiving a distance vector from neighbours, each Router updates its vector to contain the most recent
        information regarding the optimum distance to other nodes"""
        for node in received_vector["CONTENT"]:
            if node not in self.distance_vector:
                self.distance_vector[node] = received_vector["CONTENT"][node]
            else:
                self.distance_vecotr[node] = min([self.distance_vector[node], received_vector["CONTENT"][node]])

    def next_node(self, packet: Packet):
        """Returns the next address of the next router for a routed packet"""
        return self.distance_vector[packet.to_addr]

    def send_packet(self, addr: str, packet: Packet):
        """Sends packet to addr. If this is unknown,
        query network layer over where to send it to.

        Arguments:
            addr {str} -- The address of the target.
            packet {Packet} -- The packet to send."""
        raise NotImplementedError("test test")

    def recieve_packet(self, packet: Packet):
        raise NotImplementedError("test setsers")
