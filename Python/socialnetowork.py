# -------------------------------- #
# Intro to CS Final Project        #
# Gaming Social Network [Option 1] #
# -------------------------------- #
#
# For students who have paid for the full course experience:
# please check submission instructions in the Instructor Note below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <username> is connected to <name1>, <name2>,...,<nameN>. 
# <username> likes to play <game1>,...,<gameN>.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a gamer profile. For example:
# 
# John is connected to Bryant, Debra, Walter. 
# John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two - (e.g. lists of dictionaries). Pick one which
# will allow you to manage the data above and implement the procedures below. 
# 
# You can assume that <username> is a unique identifier for a user. In other
# words, there is only one John in the network. Furthermore, connections are not
# symmetric - if John is connected with Alice, it does not mean that Alice is
# connected with John. 
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
# Some details:  Each sentence will be separated from one another with only
# a period (there will not be whitespace or new lines between sentences)
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

example_input_alternate="""John is connected to Bryant, Debra, Walter. John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner. Bryant is connected to Olive, Ollie, Freda, Mercedes. Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man. Mercedes is connected to Walter, Robin, Bryant. Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures. Olive is connected to John, Ollie. Olive likes to play The Legend of Corgi, Starfleet Commander. Debra is connected to Walter, Levi, Jennie, Robin. Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords. Walter is connected to John, Levi, Bryant. Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man. Levi is connected to Ollie, John, Walter. Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma. Ollie is connected to Mercedes, Freda, Bryant. Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game. Jennie is connected to Levi, John, Freda, Robin. Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms. Robin is connected to Ollie. Robin likes to play Call of Arms, Dwarves and Swords. Freda is connected to Olive, John, Debra. Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."""

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information. 
# 
# Arguments: 
#   string_input: block of text containing the network information
# 
# Return: 
#   The new network data structure
def create_data_structure(string_input):
    '''Parses a string of text into a dictionary of users and thier connections 
       and games. Creats a dictionary with the following format:
       {'user': {'connections': [], 'games': []}.'''  
    network = {}
    # uses the split fuction to split on "." in the text string and outputs 
    # splits into an empty list
    split_strings = string_input.split('.')
    split_strings.pop()
    # uses a for loop to extract user, connections and games from each split 
    # string and adds the values to an empty dictonary.
    for element in split_strings:
        split_string = element.split()
        if split_string[0] not in network:
            network[split_string[0]] = {'connections': [] , 'games': []}
        if [split_string[1], split_string[2], split_string[3]] == ['is', 'connected', 'to']:
            network[split_string[0]]['connections'] = ' '.join(split_string[4:]).split(', ')
        if [split_string[1], split_string[2], split_string[3]] == ['likes', 'to', 'play']:  
            network[split_string[0]]['games'] = ' '.join(split_string[4:]).split(',')
    return network

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections a user has.
#
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of the user.
# 
# Return: 
#   A list of all connections the user has. If the user has no connections, 
#   return an empty list. If the user is not in network, return None.  
def get_connections(network, user):
    '''returns a user's connections from the dictionary created in 
    create_data_structure(string_input).'''
    if user not in network:
        return None
    return network[user]['connections']

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:  String with the name of the user ("Gary")
#   user_B:  String with the name of the user that will be the new connection.
#
# Return: 
#   The updated network with the new connection added (if necessary), or False 
#   if user_A or user_B do not exist in network.
def add_connection(network, user_A, user_B):
    '''Appends user_B to user_A's connection list with the get_connections
       function.'''
    if user_A not in network or user_B not in network:
        return False
    if user_B in get_connections(network, user_A):
        return network
    get_connections(network, user_A).append(user_B)
    return network

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user:    String containing the users name to be added (e.g. "Dave")
#   games:   List containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. If the 
#   user is already in the network, update their game preferences as necessary.
def add_new_user(network, user, games):
    '''Adds a new user to the network or updates the user's games 
       if the user is aready in the network.'''
    if user in network:
        network[user]['games'] = games
    if user not in network:
        network[user] = {'connections': [] , 'games': games}  
    return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections, i.e. connections of connections, of a 
#   given user.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of a user.
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   If the user is not in the network, return None. If a user has no primary 
#   connections to begin with, you should return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    '''Returns a user's secondary connections adding the connections 
       of a user's connections to an empty list'''
    secondary_connections = []
    if user not in network:
        return None
    if get_connections(network, user) == []:
        return []
    # uses get_connections on each of the user's connections and extends the 
    # returned list of connections into an empty list.
    for friend in get_connections(network, user):
        secondary_connections.extend(get_connections(network, friend))
    return secondary_connections

# ----------------------------------------------------------------------------- 	
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:    String containing the name of user_A.
#   user_B:    String containing the name of user_B.
#
# Return: 
#   The number of connections in common (integer). Should return False if 
#   user_A or user_B are not in network.
def connections_in_common(network, user_A, user_B):
    '''Finds the connections in common between two users.'''
    count = 0
    if user_A not in network or user_B not in network:
        return False
    # gets a list of connections in common between two users with the 
    # set function and returns the length of the list
    count = len(set(get_connections(network, user_A)) & set(get_connections(network, user_B)))
    return count

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user, connection): 
#   Finds the connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#                   Solve this problem using recursion. 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A List showing the path from user_A to user_B. If such a path does not 
#   exist, return None
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hint: 
#   Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
def path_to_friend(network, user, connection):
    # your RECURSIVE solution here!
    '''Adds the user to the begining of the path to a connection list of connections.''' 
    if user not in network:
        return None
    path = [user]
    if path_to_friend_helper(network, user, connection, []) != None:
        return path + path_to_friend_helper(network, user, connection, [])
    return None    
def path_to_friend_helper(network, user, connection, path_list):
    '''Searches a user's connections for a path to a target connection by 
        repeating path_to_friend_helper funtion on connections until the path terminates.'''
    if user not in network:
        return None
    connections = get_connections(network,user)
    # loops through a user's connections and appends connections not already 
    # in the list to an empty list.
    for friend in connections:
        if friend == connection:
            return [friend]
        elif not friend in path_list:
            path_list.append(friend)
            # repeats the path_to_friend_helper function on the selected connection
            path_part = path_to_friend_helper(network, friend, connection, path_list)
            if path_part != None:
                return [friend] + path_part
    return None        
        
    
    #for 
    #    if connection in get_connections(network,first):
    #        path.append(friend)
    #        break
    
    #return secondary_connections
    #if connection in get_connections(network, user):
    #    path = [user,connection]
    #    return path
    
    #return path    
 
# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.
# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!
#
 
def get_lists_of_secondary_connections(network, user):
    '''Gets the secondary connections of a user and returns the secondary 
       connections from each connection in a seperate list. Takes a list of 
       user connections [connection, connection, etc] and returns the users
       secondary connections in the following structure: 
       [[secondary connections],[secondary connections],[etc]].'''
    lists_of_secondary_connections = []
    for friend in get_connections(network, user):
        # uses append to add a friends connections as a seperate list
        lists_of_secondary_connections.append(get_connections(network, friend))
    return lists_of_secondary_connections
        
# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.
# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

import itertools
def create_friend_recomendations(network):
    '''Returns a dictonary of common secondary conections among a user's 
       connections and a degree of connection count in the following format:
       {'User':{1:[secondary connections],2:[secondary connections],etc...]}}.
       In 2:[secondary connections], two of the users connections have the 
       connnections in [secondary connection] in common. The function counts the 
       number of user connections and finds the secondary connections in common 
       between all of the connections. For (connections count - 1), all possible 
       combinations of (connections-1)/(total connections) are searched.'''
    friend_recomendations = {}
    # loops through each user in a network, adds the user to an empty 
    # dictionary, and returns their secondary connections with 
    # get_lists_of_secondary_connections
    for user in network.keys():
        friend_recomendations[user] = {}
        lists_of_secondary_connections = get_lists_of_secondary_connections(network, user)
        # counts the number of connection lists in the returned list 
        # of secondary connections and returns a sorted countdown list 
        # from the largest value to zero
        lists_of_secondary_connections_count = len(lists_of_secondary_connections)
        degrees_of_connection = range(lists_of_secondary_connections_count,0,-1)
        # loops over each numerical value in the countdown list and creates 
        # a list of all the possible combinations of a given number of 
        # the user's connections with itertools
        for degree in degrees_of_connection:
            degree_secondary_connections = []
            # uses itertools to find all of the possible combinations of
            # (connections-1)/(total connections) and the set and set.intersection 
            # function to search for common connections.
            connection_combinations = list(itertools.combinations(lists_of_secondary_connections, degree))
            # loops over each combination set and returns any common connections 
            # with the set set.interesction function
            for combination in connection_combinations:
                degree_secondary_connections.extend(set.intersection(*map(set, combination)))
            unique_degree_secondary_connections = list(set(degree_secondary_connections))
            # uses a for loop to remove the user, existing connections, and 
            # duplicate connections from the list
            if user in unique_degree_secondary_connections:
                unique_degree_secondary_connections.remove(user)
            for connection in get_connections(network, user):
                if connection in unique_degree_secondary_connections:
                     unique_degree_secondary_connections.remove(connection)
            # adds the users friend recomendations to a list
            friend_recomendations[user][degree] = unique_degree_secondary_connections 
    return friend_recomendations

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.
# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

def get_user_friend_recomendations(recomendations, user):
    '''Returns the friend recomendations of a user from the friend recomendations
    dictonary.'''
    if user not in recomendations:
        return None
    return recomendations[user]

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.
# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

def rank_user_friend_recomendations(recomendations, user):
    '''Returns a ranked list of friend recomnadtions with the most connections in
       common for a user from the friend friend recomendation dictronary. Ranks 
       friend recomendations with the most connections in common from left to right.'''
    if user not in recomendations:
        return None
    # creates and empty list
    rank_recomendations = []
    # gets a users friend recomendations from the dictionary
    friend_recomendations = get_user_friend_recomendations(recomendations, user)
    # sorts the user's friends recomendations returned from the dictionary by 
    # most number of connections in common with the sorted function
    ranks = sorted(friend_recomendations.keys(), reverse=True)
    # loops through each rank and loops through each element within a rank and
    # appends friends to an empty list
    for rank in ranks:
        for friend in friend_recomendations[rank]:
            # removes duplicates from list 
            if friend not in rank_recomendations:
                rank_recomendations.append(friend)
    return rank_recomendations    


net = create_data_structure(example_input)
#print net
#print path_to_friend(net, 'Ollie', 'John')
#print get_connections(net, "Debra")
#print add_new_user(net, "Debra", []) 
#net = add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_connections(net, "Mercedes")
#print add_connection(net, "John", "Freda")
#print get_secondary_connections(net, "Mercedes")
#print connections_in_common(net, "Mercedes", "John")
rec = create_friend_recomendations(net)
print rec
print get_user_friend_recomendations(rec,'John')
print rank_user_friend_recomendations(rec,'John')

