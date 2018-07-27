def Build_connection_string(params):
    """
    Takes a dictionary parameter and outputs a String
    """
    return ';'.join("%s = %s" % (i,j) for i,j in params.items())

if __name__ == "__main__":
    params = {'my':'name','is':'khan'}
    print(Build_connection_string(params))
