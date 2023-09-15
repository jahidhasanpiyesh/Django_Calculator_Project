import re
from django.shortcuts import render


# Create your views here.
def index(request):
    result = 0
    # print(request.method)
    if request.method == "POST":
        a = request.POST.get('display')
        input_string = str(a)
        operators = re.findall(r'[+\-*/]', input_string)
        numbers = re.findall(r'\d+', input_string)
        numbers = [int(number) for number in numbers]
        first_number = numbers[0]
        second_number = numbers[1]
        print("input Value is:", input_string)  # len = 5
        # print(operators)
        if operators == ["+"]:
            result = first_number + second_number
            print("Output is:", result)
            # data1 = int(input_string[0])
            # data2 = int(input_string[4])
            # s = (data1 + data2)
            # print("Output is:", s)
        elif operators == ["-"]:
            result = first_number - second_number
            print("Output is:", result)
            # data1 = int(input_string[0])
            # data2 = int(input_string[4])
            # s = (data1 - data2)
            # print("Output is:", s)
        elif operators == ["*"]:
            result = first_number * second_number
            print("Output is:", result)
            # data1 = int(input_string[0])
            # data2 = int(input_string[4])
            # s = (data1 * data2)
            # print("Output is:", s)
        elif operators == ["/"]:
            result = first_number / second_number
            print("Output is:", result)
            # data1 = int(input_string[0])
            # data2 = int(input_string[4])
            # s = (data1 / data2)
            # print("Output is:", s)
    return render(request, "CalculatorApp/index.html", {'output': result})
