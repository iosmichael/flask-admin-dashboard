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
    """  """

    def __init__(self, version):
        """
        Initialize the CommandList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.wireless.v1.command.CommandList
        :rtype: twilio.rest.wireless.v1.command.CommandList
        """
        super(CommandList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Commands'.format(**self._solution)

    def stream(self, sim=values.unset, status=values.unset, direction=values.unset,
               limit=None, page_size=None):
        """
        Streams CommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode sim: Only return Commands to or from this SIM.
        :param CommandInstance.Status status: Only return Commands with this status value.
        :param CommandInstance.Direction direction: Only return Commands with this direction value.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.command.CommandInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(sim=sim, status=status, direction=direction, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, sim=values.unset, status=values.unset, direction=values.unset,
             limit=None, page_size=None):
        """
        Lists CommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode sim: Only return Commands to or from this SIM.
        :param CommandInstance.Status status: Only return Commands with this status value.
        :param CommandInstance.Direction direction: Only return Commands with this direction value.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.command.CommandInstance]
        """
        return list(self.stream(
            sim=sim,
            status=status,
            direction=direction,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, sim=values.unset, status=values.unset, direction=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of CommandInstance records from the API.
        Request is executed immediately

        :param unicode sim: Only return Commands to or from this SIM.
        :param CommandInstance.Status status: Only return Commands with this status value.
        :param CommandInstance.Direction direction: Only return Commands with this direction value.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandPage
        """
        params = values.of({
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
        :rtype: twilio.rest.wireless.v1.command.CommandPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CommandPage(self._version, response, self._solution)

    def create(self, command, sim=values.unset, callback_method=values.unset,
               callback_url=values.unset, command_mode=values.unset,
               include_sid=values.unset):
        """
        Create a new CommandInstance

        :param unicode command: The message body of the Command or a Base64 encoded byte string in binary mode.
        :param unicode sim: The Sid or UniqueName of the SIM to send the Command to.
        :param unicode callback_method: The HTTP method Twilio will use when making a request to the callback URL.
        :param unicode callback_url: Twilio will make a request to this URL when the Command has finished sending.
        :param CommandInstance.CommandMode command_mode: A string representing which mode to send the SMS message using.
        :param unicode include_sid: When sending a Command to a SIM in text mode, Twilio can automatically include the Sid of the Command in the message body, which could be used to ensure that the device does not process the same Command more than once.

        :returns: Newly created CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandInstance
        """
        data = values.of({
            'Command': command,
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

        :returns: twilio.rest.wireless.v1.command.CommandContext
        :rtype: twilio.rest.wireless.v1.command.CommandContext
        """
        return CommandContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a CommandContext

        :param sid: The sid

        :returns: twilio.rest.wireless.v1.command.CommandContext
        :rtype: twilio.rest.wireless.v1.command.CommandContext
        """
        return CommandContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.CommandList>'


class CommandPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the CommandPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.wireless.v1.command.CommandPage
        :rtype: twilio.rest.wireless.v1.command.CommandPage
        """
        super(CommandPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CommandInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.wireless.v1.command.CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandInstance
        """
        return CommandInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.CommandPage>'


class CommandContext(InstanceContext):
    """  """

    def __init__(self, version, sid):
        """
        Initialize the CommandContext

        :param Version version: Version that contains the resource
        :param sid: The sid

        :returns: twilio.rest.wireless.v1.command.CommandContext
        :rtype: twilio.rest.wireless.v1.command.CommandContext
        """
        super(CommandContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Commands/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a CommandInstance

        :returns: Fetched CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandInstance
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
        return '<Twilio.Wireless.V1.CommandContext {}>'.format(context)


class CommandInstance(InstanceResource):
    """  """

    class Direction(object):
        FROM_SIM = "from_sim"
        TO_SIM = "to_sim"

    class Status(object):
        QUEUED = "queued"
        SENT = "sent"
        DELIVERED = "delivered"
        RECEIVED = "received"
        FAILED = "failed"

    class CommandMode(object):
        TEXT = "text"
        BINARY = "binary"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the CommandInstance

        :returns: twilio.rest.wireless.v1.command.CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandInstance
        """
        super(CommandInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
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
        :rtype: twilio.rest.wireless.v1.command.CommandContext
        """
        if self._context is None:
            self._context = CommandContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The unique id of the Account that this Command belongs to.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def sim_sid(self):
        """
        :returns: The unique ID of the SIM that this Command was sent to or from.
        :rtype: unicode
        """
        return self._properties['sim_sid']

    @property
    def command(self):
        """
        :returns: The message being sent to or from the SIM.
        :rtype: unicode
        """
        return self._properties['command']

    @property
    def command_mode(self):
        """
        :returns: A string representing which mode the SMS was sent or received using.
        :rtype: CommandInstance.CommandMode
        """
        return self._properties['command_mode']

    @property
    def status(self):
        """
        :returns: A string representing the status of the Command.
        :rtype: CommandInstance.Status
        """
        return self._properties['status']

    @property
    def direction(self):
        """
        :returns: The direction of the Command.
        :rtype: CommandInstance.Direction
        """
        return self._properties['direction']

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created, given as GMT in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated, given as GMT in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The URL for this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a CommandInstance

        :returns: Fetched CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Wireless.V1.CommandInstance {}>'.format(context)
