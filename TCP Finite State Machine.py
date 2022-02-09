# All states
CLOSED = "CLOSED"
LISTEN = "LISTEN"
SYN_SENT = "SYN_SENT"
SYN_RCVD = "SYN_RCVD"
ESTABLISHED = "ESTABLISHED"
CLOSE_WAIT = "CLOSE_WAIT"
LAST_ACK = "LAST_ACK"
FIN_WAIT_1 = "FIN_WAIT_1"
FIN_WAIT_2 = "FIN_WAIT_2"
CLOSING = "CLOSING"
TIME_WAIT = "TIME_WAIT"
    
# All events
APP_PASSIVE_OPEN = "APP_PASSIVE_OPEN"
APP_ACTIVE_OPEN = "APP_ACTIVE_OPEN"
APP_SEND = "APP_SEND"
APP_CLOSE = "APP_CLOSE"
APP_TIMEOUT = "APP_TIMEOUT"
RCV_SYN = "RCV_SYN"
RCV_ACK = "RCV_ACK"
RCV_SYN_ACK = "RCV_SYN_ACK"
RCV_FIN = "RCV_FIN"
RCV_FIN_ACK = "RCV_FIN_ACK"

def traverse_TCP_states(events):
    state = CLOSED  # initial state, always
    
    for event in events:
        new_state = get_new_state(state, event)
        if new_state == "ERROR":
            return "ERROR"
        else:
            state = new_state
    
    return state
    
def get_new_state(state, event):
    transitions = [
        (CLOSED, APP_PASSIVE_OPEN, LISTEN),
        (CLOSED, APP_ACTIVE_OPEN, SYN_SENT),
        (LISTEN, RCV_SYN, SYN_RCVD),
        (LISTEN, APP_SEND, SYN_SENT),
        (LISTEN, APP_CLOSE, CLOSED),
        (SYN_RCVD, APP_CLOSE, FIN_WAIT_1),
        (SYN_RCVD, RCV_ACK, ESTABLISHED),
        (SYN_SENT, RCV_SYN, SYN_RCVD),
        (SYN_SENT, RCV_SYN_ACK, ESTABLISHED),
        (SYN_SENT, APP_CLOSE, CLOSED),
        (ESTABLISHED, APP_CLOSE, FIN_WAIT_1),
        (ESTABLISHED, RCV_FIN, CLOSE_WAIT),
        (FIN_WAIT_1, RCV_FIN, CLOSING),
        (FIN_WAIT_1, RCV_FIN_ACK, TIME_WAIT),
        (FIN_WAIT_1, RCV_ACK, FIN_WAIT_2),
        (CLOSING, RCV_ACK, TIME_WAIT),
        (FIN_WAIT_2, RCV_FIN, TIME_WAIT),
        (TIME_WAIT, APP_TIMEOUT, CLOSED),
        (CLOSE_WAIT, APP_CLOSE, LAST_ACK),
        (LAST_ACK, RCV_ACK, CLOSED)
    ]
    
    transition = list(filter(lambda x: (x[0] == state and x[1] == event), transitions))
    
    if transition:
        return transition[0][2]
    else:
        return "ERROR"
