from django.shortcuts import render

from . import lastfmhelper


DEFAULT_LIMIT = 10


def get_limit(request):
    try:
        limit = int(request.GET.get("limit", DEFAULT_LIMIT))
    except (ValueError, TypeError):
        limit = DEFAULT_LIMIT
    return limit


def index(request):
    return render(request, "music/index.html")


def top_by_country(request):
    country = request.GET["country"]
    type_ = request.GET["type"]
    limit = get_limit(request)
    data = lastfmhelper.get_top_by_country(country=country, type_=type_, limit=limit)
    return render(request, "music/top_by_country.html", {"data": data, "limit": limit})


def search(request):
    type_ = request.GET["search_type"]
    query = request.GET["query"]
    limit = get_limit(request)
    data = lastfmhelper.search(type_=type_, query=query, limit=limit)
    return render(request, "music/search_results.html", {"data": data, "type": type_, "limit": limit})


def charts(request):
    type_ = request.GET["chart_type"]
    limit = get_limit(request)
    data = lastfmhelper.get_charts(type_=type_, limit=limit)
    return render(request, "music/charts.html", {"data": data, "type": type_, "limit": limit})
