# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base import deserialize
from admin.twilio.base import values
from admin.twilio.base.instance_context import InstanceContext
from admin.twilio.base.instance_resource import InstanceResource
from admin.twilio.base.list_resource import ListResource
from admin.twilio.base.page import Page
from admin.twilio.rest.studio.v1.flow.engagement import EngagementList
from admin.twilio.rest.studio.v1.flow.execution import ExecutionList


class FlowList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the FlowList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.studio.v1.flow.FlowList
        :rtype: twilio.rest.studio.v1.flow.FlowList
        """
        super(FlowList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Flows'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams FlowInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v1.flow.FlowInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FlowInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v1.flow.FlowInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of FlowInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return FlowPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FlowInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return FlowPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a FlowContext

        :param sid: A string that uniquely identifies this Flow.

        :returns: twilio.rest.studio.v1.flow.FlowContext
        :rtype: twilio.rest.studio.v1.flow.FlowContext
        """
        return FlowContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a FlowContext

        :param sid: A string that uniquely identifies this Flow.

        :returns: twilio.rest.studio.v1.flow.FlowContext
        :rtype: twilio.rest.studio.v1.flow.FlowContext
        """
        return FlowContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.FlowList>'


class FlowPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the FlowPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.studio.v1.flow.FlowPage
        :rtype: twilio.rest.studio.v1.flow.FlowPage
        """
        super(FlowPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FlowInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.studio.v1.flow.FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowInstance
        """
        return FlowInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.FlowPage>'


class FlowContext(InstanceContext):
    """  """

    def __init__(self, version, sid):
        """
        Initialize the FlowContext

        :param Version version: Version that contains the resource
        :param sid: A string that uniquely identifies this Flow.

        :returns: twilio.rest.studio.v1.flow.FlowContext
        :rtype: twilio.rest.studio.v1.flow.FlowContext
        """
        super(FlowContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Flows/{sid}'.format(**self._solution)

        # Dependents
        self._engagements = None
        self._executions = None

    def fetch(self):
        """
        Fetch a FlowInstance

        :returns: Fetched FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return FlowInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the FlowInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def engagements(self):
        """
        Access the engagements

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementList
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementList
        """
        if self._engagements is None:
            self._engagements = EngagementList(self._version, flow_sid=self._solution['sid'], )
        return self._engagements

    @property
    def executions(self):
        """
        Access the executions

        :returns: twilio.rest.studio.v1.flow.execution.ExecutionList
        :rtype: twilio.rest.studio.v1.flow.execution.ExecutionList
        """
        if self._executions is None:
            self._executions = ExecutionList(self._version, flow_sid=self._solution['sid'], )
        return self._executions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.FlowContext {}>'.format(context)


class FlowInstance(InstanceResource):
    """  """

    class Status(object):
        DRAFT = "draft"
        PUBLISHED = "published"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the FlowInstance

        :returns: twilio.rest.studio.v1.flow.FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowInstance
        """
        super(FlowInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'status': payload['status'],
            'version': deserialize.integer(payload['version']),
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FlowContext for this FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowContext
        """
        if self._context is None:
            self._context = FlowContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Flow.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description of this resource.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def status(self):
        """
        :returns: The Status of this Flow
        :rtype: FlowInstance.Status
        """
        return self._properties['status']

    @property
    def version(self):
        """
        :returns: The latest version number of this Flow's definition.
        :rtype: unicode
        """
        return self._properties['version']

    @property
    def date_created(self):
        """
        :returns: The date this Flow was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Flow was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: Nested resource URLs.
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a FlowInstance

        :returns: Fetched FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the FlowInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def engagements(self):
        """
        Access the engagements

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementList
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementList
        """
        return self._proxy.engagements

    @property
    def executions(self):
        """
        Access the executions

        :returns: twilio.rest.studio.v1.flow.execution.ExecutionList
        :rtype: twilio.rest.studio.v1.flow.execution.ExecutionList
        """
        return self._proxy.executions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.FlowInstance {}>'.format(context)
