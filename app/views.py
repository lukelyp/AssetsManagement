# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Host
from .form import HostForm
from ansible.runner import Runner
import json

DANGER_COMMAND = ('rm', 'reboot', 'shutdown', 'init')

@login_required()
def index(request):
    return render(request, 'index.html')


@login_required()
def host_list(request):
    host_list = Host.objects.all()
    return render(request, 'hosts.html', locals())


@login_required()
def host_edit(request, id=None):
    if id:
        host_list = get_object_or_404(Host, pk=id)
        action = 'edit'
    else:
        host_list = Host()
        action = 'add'

    if request.method == 'GET':
        delete = request.GET.get('delete')
        id = request.GET.get('id')
        if delete:
            host_list = get_object_or_404(Host, pk=id)
            host_list.delete()
            return redirect('/host_list/')

    elif request.method == 'POST':
        form = HostForm(request.POST, instance=host_list)

        operate = request.POST.get('operate')
        if form.is_valid():
            if action == 'add':
                form.save()
                #ret.append(form.cleaned_data['ip'])
		return redirect('/host_list/')
            if operate:
                if operate == 'update':
                    form.save()
		    return redirect('/host_list/')
                else:
                    pass
    else:
        form = HostForm(instance=host_list)

    return render(request, 'host_edit.html', locals())


@login_required()
def exec_command(request):
    ret = ''
    if request.method == 'POST':
        action = request.get_full_path().split('=')[1]
        if action == 'exec':
            target = request.POST.get('target')
            command = request.POST.get('command')
            tgtcheck = Host.objects.filter(name=target)
            argcheck =  command not in DANGER_COMMAND
            if tgtcheck and argcheck:
                results = Runner(pattern=target, forks=10,
                                 module_name='command', module_args=command).run()
                if results.get('dark'):
                    ret = 'Failed. Please run again.'
                else:
                    ret = results.get('contacted')
                    
            elif not tgtcheck:
                ret = 'No specific host.'
            elif not argcheck:
                ret = 'Please contact admistrator.'

    return render(request, 'exec_command.html', locals())
