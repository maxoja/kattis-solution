stack_list = []
queue_list = []
pq_list = []

can_be_stack = True
can_be_queue = True
can_be_pq = True

def reset() :
    global stack_list
    global queue_list
    global pq_list
    global can_be_stack
    global can_be_queue
    global can_be_pq
    
    stack_list = []
    queue_list = []
    pq_list = []

    can_be_stack = True
    can_be_queue = True
    can_be_pq = True

def push_stack(e) :
    global stack_list
    stack_list = [e,] + stack_list

def pop_stack(e) :
    global stack_list
    if len(stack_list) == 0 :
        return False
    
    if stack_list[0] == e :
        del stack_list[0]
        return True

    return False

def add_queue(e) :
    global queue_list
    queue_list.append(e)

def pop_queue(e) :
    global queue_list
    if len(queue_list) == 0:
        return False
    
    if e == queue_list[0] :
        del queue_list[0]
        return True

    return False

def add_pq(e) :
    global pq_list
    pq_list.append(e)

def pop_pq(e) :
    global pq_list
    if len(pq_list) == 0:
        return False
    
    top = max(pq_list)
    top_id = pq_list.index(top)

    if top == e :
        del pq_list[top_id]
        return True

    return False

while True :
    try :
        reset()
        n = int(input())

        for i in range(n) :
            command = list(map(int,input().split()))
            cmd_type = command[0]
            element = command[1]
        
            if command[0] == 1 :
                push_stack(element)
                add_queue(element)
                add_pq(element)
            elif command[0] == 2 :
                if can_be_stack :
                    can_be_stack = pop_stack(element)
                if can_be_queue :
                    can_be_queue = pop_queue(element)
                if can_be_pq :
                    can_be_pq = pop_pq(element)

        if can_be_stack and ( not can_be_queue ) and ( not can_be_pq ) :
            print("stack")
        elif ( not can_be_stack ) and ( can_be_queue ) and ( not can_be_pq ) :
            print("queue")
        elif ( not can_be_stack ) and ( not can_be_queue ) and ( can_be_pq ) :
            print("priority queue")
        elif ( not can_be_stack ) and ( not can_be_queue ) and ( not can_be_pq ) :
            print("impossible")
        else :
            print("not sure")
    except EOFError :
        break
