def row_to_dict(row):
    # TODO: check if list of objects
    dic = dict(row.__dict__)
    dic.pop('_sa_instance_state', None)
    return(dic)
    