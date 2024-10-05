from django.shortcuts import render

# ODD or EVEN Checker
def odd_even_checker(request):
    number = request.GET.get('number')
    result = None
    if number:
       number = int(number)
       if number % 2 == 0:
          result = f"{number} is an even number"
    else:
        result = f"{number} is an odd number"
    return render(request, 'index.html', {'result': result})

# Name Filter
def name_filter(request):
    char = request.GET.get('char') 
    names = ["Hello", "Hai", "Welcome", "Goodbye"]
    filtered_names = [name for name in names if char and name.startswith(char)]
    return render(request, 'index.html', {'names': filtered_names, 'char': char})