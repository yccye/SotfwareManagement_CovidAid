from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from . import data_get
from . import data_map
import ast


# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type='application/json',
    )
    response["Access-Control-Allow-Origin"] = '*'
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string='error', code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {},
    }
    data.update(kwargs)
    return response_as_json(data)


def plot_map(data):
    global ct_map, cs_map, fi_map, gt_map, gs_map, fte_map
    wb_china = data_get.china_total_data(data)
    wb_global = data_get.global_total_data(data)
    ct_map, cs_map = data_map.china_total_map(wb_china)
    fi_map = data_map.china_daily_map(wb_china)
    gt_map, gs_map = data_map.global_total_map(wb_global)
    fte_map = data_map.foreign_daily_map(wb_global)


JsonResponse = json_response
JsonError = json_error
f = open('./statistic/covid_19.json', 'r', encoding='utf-8')
data = ast.literal_eval(f.read())
f.close()
plot_map(data)
maptype = 'ctmap'


def update(request):
    data = data_get.init()
    plot_map(data)
    return redirect('echarts:covid_19')


class CtView(APIView):
    def get(self, request, *args, **kwargs):
        global ct_map, maptype
        mathtype = request.GET.get('maptype')
        return JsonResponse(json.loads(ct_map))


class CsView(APIView):
    def get(self, request, *args, **kwargs):
        global cs_map, maptype
        mathtype = request.GET.get('maptype')
        return JsonResponse(json.loads(cs_map))


class CdView(APIView):
    def get(self, request, *args, **kwargs):
        global fi_map, maptype
        mathtype = request.GET.get('maptype')
        return JsonResponse(json.loads(fi_map))


class GtView(APIView):
    def get(self, request, *args, **kwargs):
        global gt_map, maptype
        mathtype = request.GET.get('maptype')
        return JsonResponse(json.loads(gt_map))


class GsView(APIView):
    def get(self, request, *args, **kwargs):
        global gs_map, maptype
        mathtype = request.GET.get('maptype')
        return JsonResponse(json.loads(gs_map))


class GdView(APIView):
    def get(self, request, *args, **kwargs):
        global gs_map, maptype
        mathtype = request.GET.get('maptype')
        return JsonResponse(json.loads(fte_map))


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        global maptype
        context = {'maptype': maptype}
        return render(request, 'echarts/covid_19.html', context=context)


from django.shortcuts import render

# Create your views here.
