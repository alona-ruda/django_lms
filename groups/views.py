from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render

from webargs.fields import Str
from webargs.djangoparser import use_args

from .forms import CreateGroupForm
from .forms import UpdateGroupForm
from .models import Group


@use_args(
    {
        'name_of_group': Str(required=False),
        'start_date': Str(required=False),
    },
    location='query'
)
def get_groups(request, args):
    groups = Group.objects.all()

    if len(args) != 0 and args.get('name_of_group'):
        groups = groups.filter(
            Q(name_of_group=args.get('name_of_group', ''))
        )

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'title': 'List of groups',
            'groups': groups
        }
    )


def detail_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'groups/detail.html', {'group': group})


def create_group(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>    
            <input type="submit" value="Submit">
        </form> 
    '''

    return HttpResponse(html_form)


def update_group(request, group_id):
    group = Group.objects.get(pk=group_id)

    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>    
            <input type="submit" value="Submit">
        </form> 
    '''

    return HttpResponse(html_form)
