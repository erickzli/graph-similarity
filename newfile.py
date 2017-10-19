''' Set the authority and the hub values of all the vertex.
    vertex.authority = 0
    vertex.hub = 0
    
    Iteration with n steps:
        Add all the children's authority, assign the value to vertex.authority
        vertex.authority += children.authority
        
        Add all the children's hub, assign the value to vertex.hub
        vertex.hub += children.hub
    
    (Version without normalization.
'''
