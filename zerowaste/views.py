from .models import Campaign, Shop, Member, Nkreview, Oreview, Ask
from .forms import AskForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import CommentForm, OreviewForm

info_list = Shop.objects.all().order_by('id')
search_list = Shop.objects.all().order_by('id')
Nkreview_list = Nkreview.objects.all().order_by('id')

# 문의하기
def ask_new(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            ask = form.save()
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(ask)
    else:
        form = AskForm()

    return render(request, "owaste/index.html", {
        "form": form,
    })


# index
def index(request):
    shop_map = Shop.objects.all().order_by('-id')
    return render(
        request,
        'owaste/index.html',
        {
            'shop_map' : shop_map
        }
    )

# campaign_list

def campaign_list(request):
    campaign_list = Campaign.objects.all().order_by('-id')
    return render(
        request,
        'owaste/campaign_list.html',
        {
            'campaign_list' : campaign_list
        }
    )

def search(request):

    info_list = Shop.objects.all().order_by('id')
    search_list = []
    search_key = request.GET.get('search_key', '')
    print(search_key)

    category_one = request.GET.get('category', '')
    subject_list = request.GET.getlist('subject', '')
    facility_list = request.GET.getlist('facility', '')
    offday_list = request.GET.getlist("day", '')
    q = Q()

    if search_key != '':
        search_list = info_list.filter(
            Q(name__icontains=search_key))  # 이름으로 찾기
        print('search_list', search_list)

        # search_list에서 시설, 추가해서 filter해서
        if category_one:
            q.add(Q(category=category_one), q.AND)
        if subject_list:
            for i in range(0, len(subject_list)):
                q.add(Q(subject__icontains=subject_list[i]), q.AND)
        if facility_list:
            for i in range(0, len(facility_list)):
                q.add(Q(facility__icontains=facility_list[i]), q.AND)
        if offday_list:
            week_names = ["day_mon", "day_tue", "day_wed",
                          "day_thu", "day_fri", "day_sat", "day_sun"]
            field_names = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
            fields_dict = dict(zip(week_names, field_names))

            for day in offday_list:
                field_name = fields_dict[day]
                conditions = {field_name: '휴무'}
                q.add(~Q(**conditions), q.AND)

        search_list = search_list.filter(q)

    else:
        search_list = info_list

        # search_list에서 시설, 추가해서 filter해서
        if category_one:
            q.add(Q(category=category_one), q.AND)
        if subject_list:
            for i in range(0, len(subject_list)):
                q.add(Q(subject__icontains=subject_list[i]), q.AND)
        if facility_list:
            for i in range(0, len(facility_list)):
                q.add(Q(facility__icontains=facility_list[i]), q.AND)

        if offday_list:
            week_names = ["day_mon", "day_tue", "day_wed",
                          "day_thu", "day_fri", "day_sat", "day_sun"]
            field_names = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
            fields_dict = dict(zip(week_names, field_names))

            for day in offday_list:
                field_name = fields_dict[day]
                conditions = {field_name: '휴무'}
                q.add(~Q(**conditions), q.AND)

        search_list = search_list.filter(q)

    subject = ','.join(subject_list)
    facility = ','.join(facility_list)
    day = ','.join(offday_list)
    print(subject)

    # ----

    # ---
    # search_list들을 info_list라는 이름으로 shop_search에 넘김
    return render(request, "owaste/shop_search.html", {'info_list': search_list,
                                                          'search_key': search_key,
                                                          'categories': category_one,
                                                          'subjects': subject,
                                                          'facilities': facility,
                                                          'days': day})


def info(request):
    all = []
    category_one = request.GET.get('category', None)
    subject_list = request.GET.getlist('subject', None)
    facility_list = request.GET.getlist('facility', None)

    q = Q()
    if category_one:
        # q &= Q(category__in=category_one)
        q.add(Q(category=category_one), q.AND)
    # if subject_list:
    #     q.add(Q(subject__in=subject_list), q.AND)
    if subject_list:
        for i in range(0, len(subject_list)):
            q.add(Q(subject__icontains=subject_list[i]), q.AND)
    if facility_list:
        for i in range(0, len(facility_list)):
            q.add(Q(facility__icontains=facility_list[i]), q.AND)

    print(q)
    products = Shop.objects.filter(q)
    for product in products:
        all.append(product)
    print('all : ', all)
    return render(request, 'owaste/shop_search.html', {'all': all})


def shop_detail(request, id):
    shop_detail = get_object_or_404(Shop, pk=id)
    # id와 똑같은 Nkreview 불러오기
    # form = CommentForm()

    oreview_form = OreviewForm()

    oreview_qs = Oreview.objects.filter(
        shop=shop_detail).select_related("user")

    review_detail = Nkreview.objects.filter(
        shop=id)  # detail은 1개의 의미. _list, _qs 목록
    context = {
        'shop_detail': shop_detail,
        'oreview_form': oreview_form,
        'oreview_qs': oreview_qs,
        'review_detail': review_detail,
    }
    return render(request, 'owaste/shop_detail.html', context)


@login_required
def review_new(request, shop_pk):
    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == "POST":
        form = OreviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = shop
            review.user = request.user
            review.save()
            return redirect(f"/owaste/detail/{shop_pk}")  # TODO: URL Reverse
    else:
        form = OreviewForm()

    return render(request, "owaste/review_form.html", {
        "form": form,
    })

@login_required
def review_edit(request, shop_pk, pk):
    review = get_object_or_404(Oreview, pk=pk)

    if request.method == "POST":
        form = OreviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(f"/owaste/detail/{shop_pk}")  # TODO: URL Reverse
    else:
        form = OreviewForm(instance=review)

    return render(request, "owaste/review_form.html", {
        "form": form,
    })

@login_required
def review_delete(request, shop_pk, pk):
    review = get_object_or_404(Oreview, pk=pk)

    if request.method == "POST":
        review.delete()
        return redirect(f"/owaste/detail/{shop_pk}")
    return render(request, "owaste/review_confirm_delete.html", {
        "review": review,
    })