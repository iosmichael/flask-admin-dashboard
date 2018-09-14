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
from admin.twilio.rest.api.v2010.account.recording.add_on_result.payload import PayloadList


class AddOnResultList(ListResource):
    """  """

    def __init__(self, version, account_sid, reference_sid):
        """
        Initialize the AddOnResultList

        :param Version version: Version that contains the resource
        :param account_sid: The unique sid that identifies this account
        :param reference_sid: A string that uniquely identifies the recording.

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultList
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultList
        """
        super(AddOnResultList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'reference_sid': reference_sid, }
        self._uri = '/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams AddOnResultInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AddOnResultInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of AddOnResultInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return AddOnResultPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AddOnResultInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return AddOnResultPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a AddOnResultContext

        :param sid: Fetch by unique result Sid

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        """
        return AddOnResultContext(
            self._version,
            account_sid=self._solution['account_sid'],
            reference_sid=self._solution['reference_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a AddOnResultContext

        :param sid: Fetch by unique result Sid

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        """
        return AddOnResultContext(
            self._version,
            account_sid=self._solution['account_sid'],
            reference_sid=self._solution['reference_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AddOnResultList>'


class AddOnResultPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the AddOnResultPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The unique sid that identifies this account
        :param reference_sid: A string that uniquely identifies the recording.

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultPage
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultPage
        """
        super(AddOnResultPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AddOnResultInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance
        """
        return AddOnResultInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            reference_sid=self._solution['reference_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AddOnResultPage>'


class AddOnResultContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, reference_sid, sid):
        """
        Initialize the AddOnResultContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param reference_sid: The reference_sid
        :param sid: Fetch by unique result Sid

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        """
        super(AddOnResultContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'reference_sid': reference_sid, 'sid': sid, }
        self._uri = '/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{sid}.json'.format(**self._solution)

        # Dependents
        self._payloads = None

    def fetch(self):
        """
        Fetch a AddOnResultInstance

        :returns: Fetched AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return AddOnResultInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            reference_sid=self._solution['reference_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the AddOnResultInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def payloads(self):
        """
        Access the payloads

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadList
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadList
        """
        if self._payloads is None:
            self._payloads = PayloadList(
                self._version,
                account_sid=self._solution['account_sid'],
                reference_sid=self._solution['reference_sid'],
                add_on_result_sid=self._solution['sid'],
            )
        return self._payloads

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AddOnResultContext {}>'.format(context)


class AddOnResultInstance(InstanceResource):
    """  """

    class Status(object):
        CANCELED = "canceled"
        COMPLETED = "completed"
        DELETED = "deleted"
        FAILED = "failed"
        IN_PROGRESS = "in-progress"
        INIT = "init"
        PROCESSING = "processing"
        QUEUED = "queued"

    def __init__(self, version, payload, account_sid, reference_sid, sid=None):
        """
        Initialize the AddOnResultInstance

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance
        """
        super(AddOnResultInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'status': payload['status'],
            'add_on_sid': payload['add_on_sid'],
            'add_on_configuration_sid': payload['add_on_configuration_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'date_completed': deserialize.rfc2822_datetime(payload['date_completed']),
            'reference_sid': payload['reference_sid'],
            'subresource_uris': payload['subresource_uris'],
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'reference_sid': reference_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: AddOnResultContext for this AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        """
        if self._context is None:
            self._context = AddOnResultContext(
                self._version,
                account_sid=self._solution['account_sid'],
                reference_sid=self._solution['reference_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this result
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The unique sid that identifies this account
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def status(self):
        """
        :returns: The status of this result.
        :rtype: AddOnResultInstance.Status
        """
        return self._properties['status']

    @property
    def add_on_sid(self):
        """
        :returns: A string that uniquely identifies the Add-on.
        :rtype: unicode
        """
        return self._properties['add_on_sid']

    @property
    def add_on_configuration_sid(self):
        """
        :returns: A string that uniquely identifies the Add-on configuration.
        :rtype: unicode
        """
        return self._properties['add_on_configuration_sid']

    @property
    def date_created(self):
        """
        :returns: The date this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def date_completed(self):
        """
        :returns: The date this result was completed.
        :rtype: datetime
        """
        return self._properties['date_completed']

    @property
    def reference_sid(self):
        """
        :returns: A string that uniquely identifies the recording.
        :rtype: unicode
        """
        return self._properties['reference_sid']

    @property
    def subresource_uris(self):
        """
        :returns: A dictionary of URIs for related resources
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    def fetch(self):
        """
        Fetch a AddOnResultInstance

        :returns: Fetched AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the AddOnResultInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def payloads(self):
        """
        Access the payloads

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadList
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadList
        """
        return self._proxy.payloads

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AddOnResultInstance {}>'.format(context)
