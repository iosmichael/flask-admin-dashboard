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


class CommandList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the CommandList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.wireless.command.CommandList
        :rtype: twilio.rest.preview.wireless.command.CommandList
        """
        super(CommandList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Commands'.format(**self._solution)

    def stream(self, device=values.unset, sim=values.unset, status=values.unset,
               direction=values.unset, limit=None, page_size=None):
        """
        Streams CommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode device: The device
        :param unicode sim: The sim
        :param unicode status: The status
        :param unicode direction: The direction
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.wireless.command.CommandInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            device=device,
            sim=sim,
            status=status,
            direction=direction,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, device=values.unset, sim=values.unset, status=values.unset,
             direction=values.unset, limit=None, page_size=None):
        """
        Lists CommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode device: The device
        :param unicode sim: The sim
        :param unicode status: The status
        :param unicode direction: The direction
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.wireless.command.CommandInstance]
        """
        return list(self.stream(
            device=device,
            sim=sim,
            status=status,
            direction=direction,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, device=values.unset, sim=values.unset, status=values.unset,
             direction=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of CommandInstance records from the API.
        Request is executed immediately

        :param unicode device: The device
        :param unicode sim: The sim
        :param unicode status: The status
        :param unicode direction: The direction
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandPage
        """
        params = values.of({
            'Device': device,
            'Sim': sim,
            'Status': status,
            'Direction': direction,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return CommandPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CommandInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CommandPage(self._version, response, self._solution)

    def create(self, command, device=values.unset, sim=values.unset,
               callback_method=values.unset, callback_url=values.unset,
               command_mode=values.unset, include_sid=values.unset):
        """
        Create a new CommandInstance

        :param unicode command: The command
        :param unicode device: The device
        :param unicode sim: The sim
        :param unicode callback_method: The callback_method
        :param unicode callback_url: The callback_url
        :param unicode command_mode: The command_mode
        :param unicode include_sid: The include_sid

        :returns: Newly created CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        data = values.of({
            'Command': command,
            'Device': device,
            'Sim': sim,
            'CallbackMethod': callback_method,
            'CallbackUrl': callback_url,
            'CommandMode': command_mode,
            'IncludeSid': include_sid,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return CommandInstance(self._version, payload, )

    def get(self, sid):
        """
        Constructs a CommandContext

        :param sid: The sid

        :returns: twilio.rest.preview.wireless.command.CommandContext
        :rtype: twilio.rest.preview.wireless.command.CommandContext
        """
        return CommandContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a CommandContext

        :param sid: The sid

        :returns: twilio.rest.preview.wireless.command.CommandContext
        :rtype: twilio.rest.preview.wireless.command.CommandContext
        """
        return CommandContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless.CommandList>'


class CommandPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the CommandPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.wireless.command.CommandPage
        :rtype: twilio.rest.preview.wireless.command.CommandPage
        """
        super(CommandPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CommandInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.wireless.command.CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        return CommandInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless.CommandPage>'


class CommandContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sid):
        """
        Initialize the CommandContext

        :param Version version: Version that contains the resource
        :param sid: The sid

        :returns: twilio.rest.preview.wireless.command.CommandContext
        :rtype: twilio.rest.preview.wireless.command.CommandContext
        """
        super(CommandContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Commands/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a CommandInstance

        :returns: Fetched CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return CommandInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.CommandContext {}>'.format(context)


class CommandInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, sid=None):
        """
        Initialize the CommandInstance

        :returns: twilio.rest.preview.wireless.command.CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        super(CommandInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'device_sid': payload['device_sid'],
            'sim_sid': payload['sim_sid'],
            'command': payload['command'],
            'command_mode': payload['command_mode'],
            'status': payload['status'],
            'direction': payload['direction'],
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

        :returns: CommandContext for this CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandContext
        """
        if self._context is None:
            self._context = CommandContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def device_sid(self):
        """
        :returns: The device_sid
        :rtype: unicode
        """
        return self._properties['device_sid']

    @property
    def sim_sid(self):
        """
        :returns: The sim_sid
        :rtype: unicode
        """
        return self._properties['sim_sid']

    @property
    def command(self):
        """
        :returns: The command
        :rtype: unicode
        """
        return self._properties['command']

    @property
    def command_mode(self):
        """
        :returns: The command_mode
        :rtype: unicode
        """
        return self._properties['command_mode']

    @property
    def status(self):
        """
        :returns: The status
        :rtype: unicode
        """
        return self._properties['status']

    @property
    def direction(self):
        """
        :returns: The direction
        :rtype: unicode
        """
        return self._properties['direction']

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
        Fetch a CommandInstance

        :returns: Fetched CommandInstance
        :rtype: twilio.rest.preview.wireless.command.CommandInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.CommandInstance {}>'.format(context)
