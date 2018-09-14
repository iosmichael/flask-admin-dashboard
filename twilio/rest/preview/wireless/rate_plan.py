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


class RatePlanList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the RatePlanList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanList
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanList
        """
        super(RatePlanList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/RatePlans'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams RatePlanInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.wireless.rate_plan.RatePlanInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists RatePlanInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.wireless.rate_plan.RatePlanInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of RatePlanInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return RatePlanPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RatePlanInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return RatePlanPage(self._version, response, self._solution)

    def create(self, unique_name=values.unset, friendly_name=values.unset,
               data_enabled=values.unset, data_limit=values.unset,
               data_metering=values.unset, messaging_enabled=values.unset,
               voice_enabled=values.unset, commands_enabled=values.unset,
               national_roaming_enabled=values.unset,
               international_roaming=values.unset):
        """
        Create a new RatePlanInstance

        :param unicode unique_name: The unique_name
        :param unicode friendly_name: The friendly_name
        :param bool data_enabled: The data_enabled
        :param unicode data_limit: The data_limit
        :param unicode data_metering: The data_metering
        :param bool messaging_enabled: The messaging_enabled
        :param bool voice_enabled: The voice_enabled
        :param bool commands_enabled: The commands_enabled
        :param bool national_roaming_enabled: The national_roaming_enabled
        :param unicode international_roaming: The international_roaming

        :returns: Newly created RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        data = values.of({
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
            'DataEnabled': data_enabled,
            'DataLimit': data_limit,
            'DataMetering': data_metering,
            'MessagingEnabled': messaging_enabled,
            'VoiceEnabled': voice_enabled,
            'CommandsEnabled': commands_enabled,
            'NationalRoamingEnabled': national_roaming_enabled,
            'InternationalRoaming': serialize.map(international_roaming, lambda e: e),
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return RatePlanInstance(self._version, payload, )

    def get(self, sid):
        """
        Constructs a RatePlanContext

        :param sid: The sid

        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        """
        return RatePlanContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a RatePlanContext

        :param sid: The sid

        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        """
        return RatePlanContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless.RatePlanList>'


class RatePlanPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the RatePlanPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanPage
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanPage
        """
        super(RatePlanPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RatePlanInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        return RatePlanInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless.RatePlanPage>'


class RatePlanContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sid):
        """
        Initialize the RatePlanContext

        :param Version version: Version that contains the resource
        :param sid: The sid

        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        """
        super(RatePlanContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/RatePlans/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a RatePlanInstance

        :returns: Fetched RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return RatePlanInstance(self._version, payload, sid=self._solution['sid'], )

    def update(self, unique_name=values.unset, friendly_name=values.unset):
        """
        Update the RatePlanInstance

        :param unicode unique_name: The unique_name
        :param unicode friendly_name: The friendly_name

        :returns: Updated RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        data = values.of({'UniqueName': unique_name, 'FriendlyName': friendly_name, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return RatePlanInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the RatePlanInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.RatePlanContext {}>'.format(context)


class RatePlanInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, sid=None):
        """
        Initialize the RatePlanInstance

        :returns: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        super(RatePlanInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'unique_name': payload['unique_name'],
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'data_enabled': payload['data_enabled'],
            'data_metering': payload['data_metering'],
            'data_limit': deserialize.integer(payload['data_limit']),
            'messaging_enabled': payload['messaging_enabled'],
            'voice_enabled': payload['voice_enabled'],
            'national_roaming_enabled': payload['national_roaming_enabled'],
            'international_roaming': payload['international_roaming'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: RatePlanContext for this RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanContext
        """
        if self._context is None:
            self._context = RatePlanContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: The unique_name
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def data_enabled(self):
        """
        :returns: The data_enabled
        :rtype: bool
        """
        return self._properties['data_enabled']

    @property
    def data_metering(self):
        """
        :returns: The data_metering
        :rtype: unicode
        """
        return self._properties['data_metering']

    @property
    def data_limit(self):
        """
        :returns: The data_limit
        :rtype: unicode
        """
        return self._properties['data_limit']

    @property
    def messaging_enabled(self):
        """
        :returns: The messaging_enabled
        :rtype: bool
        """
        return self._properties['messaging_enabled']

    @property
    def voice_enabled(self):
        """
        :returns: The voice_enabled
        :rtype: bool
        """
        return self._properties['voice_enabled']

    @property
    def national_roaming_enabled(self):
        """
        :returns: The national_roaming_enabled
        :rtype: bool
        """
        return self._properties['national_roaming_enabled']

    @property
    def international_roaming(self):
        """
        :returns: The international_roaming
        :rtype: unicode
        """
        return self._properties['international_roaming']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a RatePlanInstance

        :returns: Fetched RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        return self._proxy.fetch()

    def update(self, unique_name=values.unset, friendly_name=values.unset):
        """
        Update the RatePlanInstance

        :param unicode unique_name: The unique_name
        :param unicode friendly_name: The friendly_name

        :returns: Updated RatePlanInstance
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanInstance
        """
        return self._proxy.update(unique_name=unique_name, friendly_name=friendly_name, )

    def delete(self):
        """
        Deletes the RatePlanInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.RatePlanInstance {}>'.format(context)
