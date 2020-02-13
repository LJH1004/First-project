from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.db import connections

# Create your views here.
def login(request):
    return render(request,'login/login.html',{})
@csrf_exempt
def api_login(request):
    ID = request.POST.get('ID')
    Password = request.POST.get('Password')
    print("ID => ", ID)
    print("Password => ", Password)
    with connections['default'].cursor() as cur:
        query = '''
            select *
            from  user
            where ID = '{ID}' and Password = '{Password}'
        	'''.format(
            ID=ID,
            Password=Password
        )
        cur.execute(query)
        rows = cur.fetchall()

        if len(rows) == 1:
            print('로그인 성공')
            return JsonResponse({'result': 'success'})

        elif len(rows) == 0:
            print('로그인 실패')
            return JsonResponse({'result': 'fail'})
        else:
            print('관리자에게 문의하세요')
            return JsonResponse({'result': 'fail'})