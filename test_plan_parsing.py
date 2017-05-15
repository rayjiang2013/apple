'''
1. {'ID':'plan_1', 'suite':[{'ID':'plan_2','suite':[...],...}, {'ID':'test_1','result':'XXX',...}], ...}
find result of test_1
2. logs are written to "test_1_year:month:day:hr:min:sec.log"
in the log it has "year:month:day:hr:min:sec [Error] XXXXXXXX"
please search through the host and return how many times each error has happened. 
'''
def searchResult(id, results):
    if isinstance(results, dict):
        #for result in results:
        if 'suite' in results and isinstance(results['suite'], list):
            for sub_test in results['suite']:
                return_value = searchResult(id, sub_test)
                if return_value:
                    return return_value
        elif 'suite' in results and not isinstance(results['suite'], list):
            raise Exception
        else:
            if 'result' in results:
                if results.get('ID') == id:
                    return results.get('result')
                else:
                    return
            else:
                raise Exception
    else:
        raise Exception

results = {'ID':'plan_1', 'suite':[{'ID':'plan_2','suite':[{'ID':'test_2', 'result':'YYY'}]}, {'ID':'test_1','result':'XXX'}]}
print searchResult('test_3', results)

import os
for root, dirs,files in os.walk('/', topdown=True):
    for name in files:
        path = os.path.join(root, name)
