def test_function(dict,filename,result):
    for key,value in dict.items():
        if filename == key:
            if 'answer' in value and value['answer'] != None:
                if result == value['answer']:
                    print(f'File: \'{filename}\'  Correct answer obtained = {result}')
                elif result < value['answer']:
                    print(f'File: \'{filename}\'  Answer too low. Answer obtained = {result}, answer expected = {value['answer']}')
                else:
                    print(f'File: \'{filename}\'  Answer too high. Answer obtained = {result}, answer expected = {value['answer']}')
                return

            if 'attempts' in value and value['attempts'] != None:
                if result in value['attempts']:
                    print(f'File: \'{filename}\'  Incorrect answer. Answer has already been attempted')

            if 'low' in value and value['low'] != None:
                if result == value['low']:
                    print(f'File: \'{filename}\'  Answer already submitted. Answer too low. Answer = {result}')
                if result < value['low']:
                    print(f'File: \'{filename}\'  Answer too low. Answer = {result}, but should be more than {value['low']}')

            if 'high' in value and value['high'] != None:
                if result == value['high']:
                    print(f'File: \'{filename}\'  Answer already submitted. Answer too high. Answer = {result}')
                if result > value['high']:
                    print(f'File: \'{filename}\'  Answer too high. Answer = {result}, but should be less than {value['high']}')
'''
Dictionary format is as below:
dict = {
    filename_as_string:{'attempts':(None),'low':None,'high':None,'answer':None},
}
'''