import lizard


def calculate_code_metrics(filePath):
    cocomo_dict = lizard.analyze_file(filePath)
    
    result = cocomo_dict.__dict__
    
    function_list = []    
    for i in range(len(result['function_list'])):
        function_list.append(cocomo_dict.function_list[i].__dict__)
    
    result['function_list'] = function_list
    
    return result