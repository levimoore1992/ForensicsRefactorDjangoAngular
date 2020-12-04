# from .utils import get_date_from_json
from abc import ABC, abstractmethod


class ChartMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._chart = None

    def results(self):
        results = super().results()
        results['chart'] = self.chart
        results['chart_layout'] = self.get_chart_layout()
        return results

    def chart_date(self, dte):
        if dte:
            return dte.timestamp() * 1000
        return dte

    @property
    def chart(self):
        if self._chart is None:
            self._chart = self.get_chart()

        return self._chart

    def get_chart(self):
        raise NotImplementedError('Query must specify a get_chart method')

    def get_chart_layout(self):
        return {}
