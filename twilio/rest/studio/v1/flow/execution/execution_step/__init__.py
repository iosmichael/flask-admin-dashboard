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
from admin.twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context import ExecutionStepContextList


class ExecutionStepList(ListResource):
    """  """

    def __init__(self, version, flow_sid, execution_sid):
        """
        Initialize the ExecutionStepList

        :param Version version: Version that contains the resource
        :param flow_sid: Flow Sid.
        :param execution_sid: Execution Sid.

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepList
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepList
        """
        super(ExecutionStepList, self).__init__(version)

        # Path Solution
        self._solution = {'flow_sid': flow_sid, 'execution_sid': execution_sid, }
        self._uri = '/Flows/{flow_sid}/Executions/{execution_sid}/Steps'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams ExecutionStepInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ExecutionStepInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ExecutionStepInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ExecutionStepInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ExecutionStepPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ExecutionStepInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ExecutionStepInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ExecutionStepPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ExecutionStepContext

        :param sid: Step Sid.

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepContext
        """
        return ExecutionStepContext(
            self._version,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a ExecutionStepContext

        :param sid: Step Sid.

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepContext
        """
        return ExecutionStepContext(
            self._version,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.ExecutionStepList>'


class ExecutionStepPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the ExecutionStepPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param flow_sid: Flow Sid.
        :param execution_sid: Execution Sid.

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepPage
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepPage
        """
        super(ExecutionStepPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ExecutionStepInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepInstance
        """
        return ExecutionStepInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.ExecutionStepPage>'


class ExecutionStepContext(InstanceContext):
    """  """

    def __init__(self, version, flow_sid, execution_sid, sid):
        """
        Initialize the ExecutionStepContext

        :param Version version: Version that contains the resource
        :param flow_sid: Flow Sid.
        :param execution_sid: Execution Sid.
        :param sid: Step Sid.

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepContext
        """
        super(ExecutionStepContext, self).__init__(version)

        # Path Solution
        self._solution = {'flow_sid': flow_sid, 'execution_sid': execution_sid, 'sid': sid, }
        self._uri = '/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{sid}'.format(**self._solution)

        # Dependents
        self._step_context = None

    def fetch(self):
        """
        Fetch a ExecutionStepInstance

        :returns: Fetched ExecutionStepInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ExecutionStepInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
            sid=self._solution['sid'],
        )

    @property
    def step_context(self):
        """
        Access the step_context

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextList
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextList
        """
        if self._step_context is None:
            self._step_context = ExecutionStepContextList(
                self._version,
                flow_sid=self._solution['flow_sid'],
                execution_sid=self._solution['execution_sid'],
                step_sid=self._solution['sid'],
            )
        return self._step_context

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.ExecutionStepContext {}>'.format(context)


class ExecutionStepInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, flow_sid, execution_sid, sid=None):
        """
        Initialize the ExecutionStepInstance

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepInstance
        """
        super(ExecutionStepInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'flow_sid': payload['flow_sid'],
            'execution_sid': payload['execution_sid'],
            'name': payload['name'],
            'context': payload['context'],
            'transitioned_from': payload['transitioned_from'],
            'transitioned_to': payload['transitioned_to'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {
            'flow_sid': flow_sid,
            'execution_sid': execution_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ExecutionStepContext for this ExecutionStepInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepContext
        """
        if self._context is None:
            self._context = ExecutionStepContext(
                self._version,
                flow_sid=self._solution['flow_sid'],
                execution_sid=self._solution['execution_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Step.
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
    def flow_sid(self):
        """
        :returns: Flow Sid.
        :rtype: unicode
        """
        return self._properties['flow_sid']

    @property
    def execution_sid(self):
        """
        :returns: Execution Sid.
        :rtype: unicode
        """
        return self._properties['execution_sid']

    @property
    def name(self):
        """
        :returns: The event that caused the flow to transition to this Step.
        :rtype: unicode
        """
        return self._properties['name']

    @property
    def context(self):
        """
        :returns: The context
        :rtype: dict
        """
        return self._properties['context']

    @property
    def transitioned_from(self):
        """
        :returns: The Widget that preceded the Widget for this Step.
        :rtype: unicode
        """
        return self._properties['transitioned_from']

    @property
    def transitioned_to(self):
        """
        :returns: The Widget that will follow the Widget for this Step.
        :rtype: unicode
        """
        return self._properties['transitioned_to']

    @property
    def date_created(self):
        """
        :returns: The date this Step was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Step was updated
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
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a ExecutionStepInstance

        :returns: Fetched ExecutionStepInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.ExecutionStepInstance
        """
        return self._proxy.fetch()

    @property
    def step_context(self):
        """
        Access the step_context

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextList
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextList
        """
        return self._proxy.step_context

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.ExecutionStepInstance {}>'.format(context)
