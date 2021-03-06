# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base import deserialize
from admin.twilio.base import serialize
from admin.twilio.base import values
from admin.twilio.base.instance_context import InstanceContext
from admin.twilio.base.instance_resource import InstanceResource
from admin.twilio.base.list_resource import ListResource
from admin.twilio.base.page import Page


class WorkersCumulativeStatisticsList(ListResource):
    """  """

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkersCumulativeStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsList
        """
        super(WorkersCumulativeStatisticsList, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, }

    def get(self):
        """
        Constructs a WorkersCumulativeStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        """
        return WorkersCumulativeStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __call__(self):
        """
        Constructs a WorkersCumulativeStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        """
        return WorkersCumulativeStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkersCumulativeStatisticsList>'


class WorkersCumulativeStatisticsPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the WorkersCumulativeStatisticsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The workspace_sid

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsPage
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsPage
        """
        super(WorkersCumulativeStatisticsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkersCumulativeStatisticsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsInstance
        """
        return WorkersCumulativeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkersCumulativeStatisticsPage>'


class WorkersCumulativeStatisticsContext(InstanceContext):
    """  """

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkersCumulativeStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        """
        super(WorkersCumulativeStatisticsContext, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, }
        self._uri = '/Workspaces/{workspace_sid}/Workers/CumulativeStatistics'.format(**self._solution)

    def fetch(self, end_date=values.unset, minutes=values.unset,
              start_date=values.unset, task_channel=values.unset):
        """
        Fetch a WorkersCumulativeStatisticsInstance

        :param datetime end_date: Filter cumulative statistics by a end date.
        :param unicode minutes: Filter cumulative statistics by up to 'x' minutes in the past.
        :param datetime start_date: Filter cumulative statistics by a start date.
        :param unicode task_channel: Filter cumulative statistics by TaskChannel.

        :returns: Fetched WorkersCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsInstance
        """
        params = values.of({
            'EndDate': serialize.iso8601_datetime(end_date),
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'TaskChannel': task_channel,
        })

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return WorkersCumulativeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkersCumulativeStatisticsContext {}>'.format(context)


class WorkersCumulativeStatisticsInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, workspace_sid):
        """
        Initialize the WorkersCumulativeStatisticsInstance

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsInstance
        """
        super(WorkersCumulativeStatisticsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'start_time': deserialize.iso8601_datetime(payload['start_time']),
            'end_time': deserialize.iso8601_datetime(payload['end_time']),
            'activity_durations': payload['activity_durations'],
            'reservations_created': deserialize.integer(payload['reservations_created']),
            'reservations_accepted': deserialize.integer(payload['reservations_accepted']),
            'reservations_rejected': deserialize.integer(payload['reservations_rejected']),
            'reservations_timed_out': deserialize.integer(payload['reservations_timed_out']),
            'reservations_canceled': deserialize.integer(payload['reservations_canceled']),
            'reservations_rescinded': deserialize.integer(payload['reservations_rescinded']),
            'workspace_sid': payload['workspace_sid'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'workspace_sid': workspace_sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: WorkersCumulativeStatisticsContext for this WorkersCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        """
        if self._context is None:
            self._context = WorkersCumulativeStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def start_time(self):
        """
        :returns: The start_time
        :rtype: datetime
        """
        return self._properties['start_time']

    @property
    def end_time(self):
        """
        :returns: The end_time
        :rtype: datetime
        """
        return self._properties['end_time']

    @property
    def activity_durations(self):
        """
        :returns: The minimum, average, maximum and total time Workers spent in each Activity
        :rtype: dict
        """
        return self._properties['activity_durations']

    @property
    def reservations_created(self):
        """
        :returns: The total number of Reservations that were created
        :rtype: unicode
        """
        return self._properties['reservations_created']

    @property
    def reservations_accepted(self):
        """
        :returns: The total number of Reservations that were accepted
        :rtype: unicode
        """
        return self._properties['reservations_accepted']

    @property
    def reservations_rejected(self):
        """
        :returns: The total number of Reservations that were rejected
        :rtype: unicode
        """
        return self._properties['reservations_rejected']

    @property
    def reservations_timed_out(self):
        """
        :returns: The total number of Reservations that were timed out
        :rtype: unicode
        """
        return self._properties['reservations_timed_out']

    @property
    def reservations_canceled(self):
        """
        :returns: The total number of Reservations that were canceled
        :rtype: unicode
        """
        return self._properties['reservations_canceled']

    @property
    def reservations_rescinded(self):
        """
        :returns: The total number of Reservations that were rescinded
        :rtype: unicode
        """
        return self._properties['reservations_rescinded']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, end_date=values.unset, minutes=values.unset,
              start_date=values.unset, task_channel=values.unset):
        """
        Fetch a WorkersCumulativeStatisticsInstance

        :param datetime end_date: Filter cumulative statistics by a end date.
        :param unicode minutes: Filter cumulative statistics by up to 'x' minutes in the past.
        :param datetime start_date: Filter cumulative statistics by a start date.
        :param unicode task_channel: Filter cumulative statistics by TaskChannel.

        :returns: Fetched WorkersCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsInstance
        """
        return self._proxy.fetch(
            end_date=end_date,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkersCumulativeStatisticsInstance {}>'.format(context)
