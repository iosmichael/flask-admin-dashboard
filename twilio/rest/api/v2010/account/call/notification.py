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


class NotificationList(ListResource):
    """  """

    def __init__(self, version, account_sid, call_sid):
        """
        Initialize the NotificationList

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param call_sid: The call_sid

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationList
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationList
        """
        super(NotificationList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'call_sid': call_sid, }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Notifications.json'.format(**self._solution)

    def stream(self, log=values.unset, message_date_before=values.unset,
               message_date=values.unset, message_date_after=values.unset,
               limit=None, page_size=None):
        """
        Streams NotificationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode log: The log
        :param date message_date_before: The message_date
        :param date message_date: The message_date
        :param date message_date_after: The message_date
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.call.notification.NotificationInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            log=log,
            message_date_before=message_date_before,
            message_date=message_date,
            message_date_after=message_date_after,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, log=values.unset, message_date_before=values.unset,
             message_date=values.unset, message_date_after=values.unset, limit=None,
             page_size=None):
        """
        Lists NotificationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode log: The log
        :param date message_date_before: The message_date
        :param date message_date: The message_date
        :param date message_date_after: The message_date
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.call.notification.NotificationInstance]
        """
        return list(self.stream(
            log=log,
            message_date_before=message_date_before,
            message_date=message_date,
            message_date_after=message_date_after,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, log=values.unset, message_date_before=values.unset,
             message_date=values.unset, message_date_after=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of NotificationInstance records from the API.
        Request is executed immediately

        :param unicode log: The log
        :param date message_date_before: The message_date
        :param date message_date: The message_date
        :param date message_date_after: The message_date
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationPage
        """
        params = values.of({
            'Log': log,
            'MessageDate<': serialize.iso8601_date(message_date_before),
            'MessageDate': serialize.iso8601_date(message_date),
            'MessageDate>': serialize.iso8601_date(message_date_after),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return NotificationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of NotificationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return NotificationPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a NotificationContext

        :param sid: The sid

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationContext
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationContext
        """
        return NotificationContext(
            self._version,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a NotificationContext

        :param sid: The sid

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationContext
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationContext
        """
        return NotificationContext(
            self._version,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NotificationList>'


class NotificationPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the NotificationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The account_sid
        :param call_sid: The call_sid

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationPage
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationPage
        """
        super(NotificationPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NotificationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        return NotificationInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NotificationPage>'


class NotificationContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, call_sid, sid):
        """
        Initialize the NotificationContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param call_sid: The call_sid
        :param sid: The sid

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationContext
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationContext
        """
        super(NotificationContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'call_sid': call_sid, 'sid': sid, }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Notifications/{sid}.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch a NotificationInstance

        :returns: Fetched NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return NotificationInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the NotificationInstance

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
        return '<Twilio.Api.V2010.NotificationContext {}>'.format(context)


class NotificationInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid, call_sid, sid=None):
        """
        Initialize the NotificationInstance

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        super(NotificationInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'api_version': payload['api_version'],
            'call_sid': payload['call_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'error_code': payload['error_code'],
            'log': payload['log'],
            'message_date': deserialize.rfc2822_datetime(payload['message_date']),
            'message_text': payload['message_text'],
            'more_info': payload['more_info'],
            'request_method': payload['request_method'],
            'request_url': payload['request_url'],
            'sid': payload['sid'],
            'uri': payload['uri'],
            'request_variables': payload.get('request_variables'),
            'response_body': payload.get('response_body'),
            'response_headers': payload.get('response_headers'),
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'call_sid': call_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: NotificationContext for this NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationContext
        """
        if self._context is None:
            self._context = NotificationContext(
                self._version,
                account_sid=self._solution['account_sid'],
                call_sid=self._solution['call_sid'],
                sid=self._solution['sid'],
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
    def api_version(self):
        """
        :returns: The api_version
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def call_sid(self):
        """
        :returns: The call_sid
        :rtype: unicode
        """
        return self._properties['call_sid']

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
    def error_code(self):
        """
        :returns: The error_code
        :rtype: unicode
        """
        return self._properties['error_code']

    @property
    def log(self):
        """
        :returns: The log
        :rtype: unicode
        """
        return self._properties['log']

    @property
    def message_date(self):
        """
        :returns: The message_date
        :rtype: datetime
        """
        return self._properties['message_date']

    @property
    def message_text(self):
        """
        :returns: The message_text
        :rtype: unicode
        """
        return self._properties['message_text']

    @property
    def more_info(self):
        """
        :returns: The more_info
        :rtype: unicode
        """
        return self._properties['more_info']

    @property
    def request_method(self):
        """
        :returns: The request_method
        :rtype: unicode
        """
        return self._properties['request_method']

    @property
    def request_url(self):
        """
        :returns: The request_url
        :rtype: unicode
        """
        return self._properties['request_url']

    @property
    def request_variables(self):
        """
        :returns: The request_variables
        :rtype: unicode
        """
        return self._properties['request_variables']

    @property
    def response_body(self):
        """
        :returns: The response_body
        :rtype: unicode
        """
        return self._properties['response_body']

    @property
    def response_headers(self):
        """
        :returns: The response_headers
        :rtype: unicode
        """
        return self._properties['response_headers']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: unicode
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch a NotificationInstance

        :returns: Fetched NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the NotificationInstance

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
        return '<Twilio.Api.V2010.NotificationInstance {}>'.format(context)
