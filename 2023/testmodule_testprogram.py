dict = {
    'input.txt':{'attempts':(6,1,5,6,4),'low':4,'high':8},
    'test1input.txt':{'low':None,'high':None}
}
from testmodule import test_function

filename = 'input.txt'
result = 4

test_function(dict,filename,result)