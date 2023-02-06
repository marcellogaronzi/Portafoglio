#!python3

import lizard


def calculate_code_metrics(filePath):
    code_metrics_dict = lizard.analyze_file(filePath)

    result = code_metrics_dict.__dict__

    function_list = []
    for i in range(len(result['function_list'])):
        function_list.append(code_metrics_dict.function_list[i].__dict__)

    result['function_list'] = function_list

    return result
