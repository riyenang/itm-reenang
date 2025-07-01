def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.'''
    firstperson = to_member in social_graph[from_member]["following"]
    secondperson = from_member in social_graph[to_member]["following"]

    if  firstperson and  secondperson: #if 1st follows other
        return "friends"
    elif  firstperson: #only 1st
        return "follower"
    elif  secondperson: #only 2nd
        return "followed by"
    else: #not mutuals
        return "no relationship"

def tic_tac_toe(board):
    size = len(board)

    for row in board: #rows
        if len(set(row)) == 1 and row[0] != '':
            return row[0]

    for column in range(size): #columns
        col_element = [board[row][column] for row in range(size)]
        if len(set(col_element)) == 1 and col_element[0] != '':
            return col_element[0]

    if len(set([board[i][i] for i in range(size)])) == 1 and board[0][0] != '': #diagonal1
        return board[0][0]

    if len(set([board[i][size - 1 - i] for i in range(size)])) == 1 and board[0][size - 1] != '':     #diag2        
        return board[0][size - 1]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
 
    current_stop = first_stop #start
    total_time = 0

    while current_stop != second_stop: #to count total
        for (start, end), travel_info in route_map.items():
            if start == current_stop:
                total_time += travel_info["travel_time_mins"]
                current_stop = end
                break

    return total_time
