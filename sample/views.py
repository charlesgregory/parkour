from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import NucleicAcidType, SampleProtocol, Sample, FileSample
from .forms import SampleForm

import logging
import json

logger = logging.getLogger('db')


def get_nucleic_acid_types(request):
    """ Get the list of all nucleic acid types. """
    data = [
        {
            'id': nat.id,
            'name': nat.name,
            'type': nat.type,
        }
        for nat in NucleicAcidType.objects.all()
    ]
    return JsonResponse(data, safe=False)


def get_sample_protocols(request):
    """ Get the list of all sample protocols. """
    sample_type = request.GET.get('type')
    sample_protocols = SampleProtocol.objects.filter(type=sample_type)

    data = [
        {
            'id': protocol.id,
            'name': protocol.name,
            'type': protocol.type,
            'provider': protocol.provider,
            'catalog': protocol.catalog,
            'explanation': protocol.explanation,
            'inputRequirements': protocol.input_requirements,
            'typicalApplication': protocol.typical_application,
            'comments': protocol.comments,
        }
        for protocol in sample_protocols
    ]

    return JsonResponse(data, safe=False)


@login_required
def save_sample(request):
    """ Add a new sample or update an existing one. """
    error = ''
    data = []

    if request.method == 'POST':
        mode = request.POST.get('mode')
        sample_id = request.POST.get('sample_id')
        files = json.loads(request.POST.get('files'))

        if mode == 'add':
            form = SampleForm(request.POST)
        elif mode == 'edit':
            smpl = Sample.objects.get(pk=sample_id)
            form = SampleForm(request.POST, instance=smpl)

        if form.is_valid():
            smpl = form.save()

            if mode == 'add':
                smpl.files.add(*files)

                data = {
                    'name': smpl.name,
                    'recordType': 'S',
                    'sampleId': smpl.id,
                    'barcode': smpl.barcode,
                }

            elif mode == 'edit':
                # import pdb; pdb.set_trace()
                old_files = [file for file in smpl.files.all()]
                smpl.files.clear()
                smpl.save()
                smpl.files.add(*files)
                new_files = [file for file in smpl.files.all()]

                # Delete files
                files_to_delete = list(set(old_files) - set(new_files))
                for file in files_to_delete:
                    file.delete()
        else:
            error = str(form.errors)
            logger.debug(form.errors.as_data())

    return JsonResponse({
        'success': not error,
        'error': error,
        'data': data
    })


@login_required
def delete_sample(request):
    record_id = request.POST.get('record_id')
    sample = Sample.objects.get(pk=record_id)
    sample.delete()
    return JsonResponse({'success': True})


@login_required
def upload_files(request):
    """ """
    error = ''
    file_ids = []

    if request.method == 'POST' and any(request.FILES):
        try:
            for file in request.FILES.getlist('files'):
                f = FileSample(name=file.name, file=file)
                f.save()
                file_ids.append(f.id)

        except Exception as e:
            error = str(e)
            logger.exception(error)

    return JsonResponse({
        'success': not error,
        'error': error,
        'fileIds': file_ids
    })


@login_required
def get_files(request):
    """ """
    error = ''
    data = []

    file_ids = json.loads(request.GET.get('file_ids'))

    try:
        files = [f for f in FileSample.objects.all() if f.id in file_ids]
        data = [
            {
                'id': file.id,
                'name': file.name,
                'size': file.file.size,
                'path': settings.MEDIA_URL + file.file.name,
            }
            for file in files
        ]

    except Exception as e:
        error = str(e)
        logger.exception(error)

    return JsonResponse({
        'success': not error,
        'error': error,
        'data': data
    })
