def packet_size(packet):
    '''
    Return the size of the packet in bits
    >>> packet_size([0,1,0,1])
    4
    '''
    return len(packet)

def error_indices(packet1, packet2):
    '''
    Return a list indicating all the indices of the bit errors which occurred between the sending of packet1 and the receiving of packet2
    >>> error_indices([0,1,1,1], [1,1,0,1])
    [0, 2]
    >>> error_indices([1,1,0,1], [1,1,0,1])
    []
    '''
    error=[]
    for i in range( len(packet1) ):
        if packet1[i] != packet2[i]:
            error += [i]
    return error

def find_packet_diff(packet1, packet2):
    '''
    Return the number of bit errors that have occurred in the transmission from packet1 to packet2
    >>> find_packet_diff([0,1,0,1], [1,1,0,1])
    1
    >>> find_packet_diff([0,1,1,0], [0,1,1,0])
    0
    '''
    count=0
    for i in range( len(packet1) ):
        if packet1[i] != packet2[i]:
            count += 1
    return count

if __name__ == "__main__":
    # test your bit error rate detector here
    packet_sent = [0, 1, 1, 1]
    packet_received = [1, 1, 1, 1]
