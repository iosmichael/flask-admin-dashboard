# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base import values
from admin.twilio.base.instance_context import InstanceContext
from admin.twilio.base.instance_resource import InstanceResource
from admin.twilio.base.list_resource import ListResource
from admin.twilio.base.page import Page


class StepContextList(ListResource):
    """  """

    def __init__(self, version, flow_sid, engagement_sid, step_sid):
        """
        Initialize the StepContextList

        :param Version version: Version that contains the resource
        :param flow_sid: Flow Sid.
        :param engagement_sid: Engagement Sid.
        :param step_sid: Step Sid.

        :returns: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextList
        :rtype: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextList
        """
        super(StepContextList, self).__init__(version)

        # Path Solution
        self._solution = {'flow_sid': flow_sid, 'engagement_sid': engagement_sid, 'step_sid': step_sid, }

    def get(self):
        """
        Constructs a StepContextContext

        :returns: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextContext
        :rtype: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextContext
        """
        return StepContextContext(
            self._version,
            flow_sid=self._solution['flow_sid'],
            engagement_sid=self._solution['engagement_sid'],
            step_sid=self._solution['step_sid'],
        )

    def __call__(self):
        """
        Constructs a StepContextContext

        :returns: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextContext
        :rtype: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextContext
        """
        return StepContextContext(
            self._version,
            flow_sid=self._solution['flow_sid'],
            engagement_sid=self._solution['engagement_sid'],
            step_sid=self._solution['step_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.StepContextList>'


class StepContextPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the StepContextPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param flow_sid: Flow Sid.
        :param engagement_sid: Engagement Sid.
        :param step_sid: Step Sid.

        :returns: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextPage
        :rtype: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextPage
        """
        super(StepContextPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of StepContextInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextInstance
        """
        return StepContextInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            engagement_sid=self._solution['engagement_sid'],
            step_sid=self._solution['step_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.StepContextPage>'


class StepContextContext(InstanceContext):
    """  """

    def __init__(self, version, flow_sid, engagement_sid, step_sid):
        """
        Initialize the StepContextContext

        :param Version version: Version that contains the resource
        :param flow_sid: Flow Sid.
        :param engagement_sid: Engagement Sid.
        :param step_sid: Step Sid.

        :returns: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextContext
        :rtype: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextContext
        """
        super(StepContextContext, self).__init__(version)

        # Path Solution
        self._solution = {'flow_sid': flow_sid, 'engagement_sid': engagement_sid, 'step_sid': step_sid, }
        self._uri = '/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps/{step_sid}/Context'.format(**self._solution)

    def fetch(self):
        """
        Fetch a StepContextInstance

        :returns: Fetched StepContextInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return StepContextInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            engagement_sid=self._solution['engagement_sid'],
            step_sid=self._solution['step_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.StepContextContext {}>'.format(context)


class StepContextInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, flow_sid, engagement_sid, step_sid):
        """
        Initialize the StepContextInstance

        :returns: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextInstance
        """
        super(StepContextInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'context': payload['context'],
            'engagement_sid': payload['engagement_sid'],
            'flow_sid': payload['flow_sid'],
            'step_sid': payload['step_sid'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'flow_sid': flow_sid, 'engagement_sid': engagement_sid, 'step_sid': step_sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: StepContextContext for this StepContextInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextContext
        """
        if self._context is None:
            self._context = StepContextContext(
                self._version,
                flow_sid=self._solution['flow_sid'],
                engagement_sid=self._solution['engagement_sid'],
                step_sid=self._solution['step_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def context(self):
        """
        :returns: Flow state.
        :rtype: dict
        """
        return self._properties['context']

    @property
    def engagement_sid(self):
        """
        :returns: Engagement Sid.
        :rtype: unicode
        """
        return self._properties['engagement_sid']

    @property
    def flow_sid(self):
        """
        :returns: Flow Sid.
        :rtype: unicode
        """
        return self._properties['flow_sid']

    @property
    def step_sid(self):
        """
        :returns: Step Sid.
        :rtype: unicode
        """
        return self._properties['step_sid']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a StepContextInstance

        :returns: Fetched StepContextInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.step.step_context.StepContextInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.StepContextInstance {}>'.format(context)
