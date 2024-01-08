class Container:
    is_empty=True
    value=None


a=Container()

def set_Container_value (class_name, parameter, value):
    class_name.is_empty=False
    return setattr (class_name, parameter, value)
    
def unset_Container_value(class_name):
    class_name.value=None
    class_name.is_empty=True

def print_Container (class_name):
    if isinstance(class_name, type):
        if class_name.is_empty==True:
            print (class_name.__name__, "is empty")
        else:
            return print (f'{class_name.__name__}<{class_name.value}>')
    else:
        print ("Obj Value=", class_name.value)    

print_Container (Container)
set_Container_value (Container, "value", 0)
print_Container (Container)

print (a.is_empty)