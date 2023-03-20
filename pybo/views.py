from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse,JsonResponse,HttpRequest
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def table_product(request):
    outputProduct = []
    with connection.cursor() as cursor:
        sqlQueryProduct = "SELECT makerName, modelNumber, modelType FROM product;"
        cursor.execute(sqlQueryProduct)
        fetchResultProduct = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultProduct:
            eachRow = {'makername': temp[0], 'modelnumber': temp[1], 'modeltype': temp[2]}
            outputProduct.append(eachRow)
    
    data={'rendered_table' : render_to_string('table_product.html',context = {'products':outputProduct})}
    return JsonResponse(data)

def table_pc(request):
    outputPC = []
    with connection.cursor() as cursor:
        sqlQueryPC = "SELECT modelnumber, speed, ramSize, hdSize, price FROM pc;"
        cursor.execute(sqlQueryPC)
        fetchResultPC = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultPC:
            eachRow = {'modelnumber': temp[0], 'speed': temp[1], 'ramsize': temp[2],
                'hdsize' : temp[3], 'price' : temp[4]}
            outputPC.append(eachRow)

    data = {'rendered_table' : render_to_string('table_pc.html',context = {'pcs':outputPC})}
    return JsonResponse(data)

def table_laptop(request):
    outputLaptop = []
    with connection.cursor() as cursor:
        sqlQueryLaptop = "SELECT modelnumber, speed, ramSize, hdSize, screen, price FROM laptop;"
        cursor.execute(sqlQueryLaptop)
        fetchResultLaptop = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultLaptop:
            eachRow = {'modelnumber': temp[0], 'speed': temp[1], 'ramsize': temp[2],
                'hdsize' : temp[3], 'screen':temp[4] ,'price' : temp[5]}
            outputLaptop.append(eachRow)

    data = {'rendered_table' : render_to_string('table_laptop.html',context = {'laptops':outputLaptop})}
    return JsonResponse(data)

def table_printer(request):
    outputPrinter = []
    with connection.cursor() as cursor:
        sqlQueryPrinter = "SELECT modelnumber, color, inkType, price FROM printer;"
        cursor.execute(sqlQueryPrinter)
        fetchResultPrinter = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultPrinter:
            eachRow = {'modelnumber': temp[0], 'color': temp[1], 'inktype': temp[2], 'price':temp[3]}
            outputPrinter.append(eachRow)
    data = {'rendered_table' : render_to_string('table_printer.html',context = {'printers':outputPrinter})}
    return JsonResponse(data)

def table_query_01(request):
    outputQuery = []
    with connection.cursor() as cursor:
        sqlQuery = "SELECT AVG(hdSize) from pc"
        cursor.execute(sqlQuery)
        fetchResultQuery = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultQuery:
            eachRow = {'avg' : temp[0]}
            outputQuery.append(eachRow)
    data = {'rendered_table' : render_to_string('query_01.html',context={'query_01':outputQuery})}
    return JsonResponse(data)

def table_query_02(request):
    outputQuery = []
    with connection.cursor() as cursor:
        sqlQuery = """SELECT makerName,AVG(speed) 
                    FROM laptop l, product p 
                    WHERE l.modelNumber = p.modelNumber 
                    GROUP BY p.makerName"""
        cursor.execute(sqlQuery)
        fetchResultQuery = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultQuery:
            eachRow = {'makername': temp[0], 'speed': temp[1]}
            outputQuery.append(eachRow)

    data = {'rendered_table' : render_to_string('query_02.html',context={'query_02':outputQuery})}
    return JsonResponse(data)

def table_query_03(request):
    outputQuery = []
    with connection.cursor() as cursor:
        sqlQuery = """SELECT P.makerName, l.price
                    FROM laptop l, product p
                    WHERE l.modelNumber = p.modelNumber
                    GROUP BY p.makerName
                    HAVING count(*) = 1
                    """
        cursor.execute(sqlQuery)
        fetchResultQuery = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultQuery:
            eachRow = {'makername': temp[0], 'price': temp[1]}
            outputQuery.append(eachRow)

    data = {'rendered_table' : render_to_string('query_03.html',context={'query_03':outputQuery})}
    return JsonResponse(data)

def table_query_04(request):
    outputQuery = []
    with connection.cursor() as cursor:
        sqlQuery = """SELECT makerName, p1.modelNumber, MAX(price)
                    FROM printer p1, product p2 
                    WHERE p1.modelNumber = p2.modelNumber 
                    GROUP BY p2.makerName
                    """
        cursor.execute(sqlQuery)
        fetchResultQuery = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultQuery:
            eachRow = {'makername': temp[0], 'modelnumber': temp[1], 'maxprice' : temp[2]}
            outputQuery.append(eachRow)

    data = {'rendered_table' : render_to_string('query_04.html',context={'query_04':outputQuery})}
    return JsonResponse(data)