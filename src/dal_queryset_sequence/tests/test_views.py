from django import test
from django import http
from django.contrib.auth.models import Group, User

from dal import autocomplete
from dal_queryset_sequence.views import BaseQuerySetSequenceView


class ViewTestCase(test.TestCase):
    def test_view(self):
        for i in range(0,3):
            Group.objects.create(name='foo%s' % i)

        view = autocomplete.Select2QuerySetSequenceView.as_view(
            queryset=autocomplete.QuerySetSequence(
                Group.objects.all(),
            ),
            create_field='name',
            paginate_by=2,
        )
        request = test.RequestFactory().get('?q=foo')
        response = view(request)
