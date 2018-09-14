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
from admin.twilio.rest.api.v2010.account.available_phone_number.local import LocalList
from admin.twilio.rest.api.v2010.account.available_phone_number.machine_to_machine import MachineToMachineList
from admin.twilio.rest.api.v2010.account.available_phone_number.mobile import MobileList
from admin.twilio.rest.api.v2010.account.available_phone_number.national import NationalList
from admin.twilio.rest.api.v2010.account.available_phone_number.shared_cost import SharedCostList
from admin.twilio.rest.api.v2010.account.available_phone_number.toll_free import TollFreeList
from admin.twilio.rest.api.v2010.account.available_phone_number.voip import VoipList


class AvailablePhoneNumberCountryList(ListResource):
    """  """

    def __init__(self, version, account_sid):
        """
        Initialize the AvailablePhoneNumberCountryList

        :param Version version: Version that contains the resource
        :param account_sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryList
        """
        super(AvailablePhoneNumberCountryList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, }
        self._uri = '/Accounts/{account_sid}/AvailablePhoneNumbers.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams AvailablePhoneNumberCountryInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AvailablePhoneNumberCountryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of AvailablePhoneNumberCountryInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return AvailablePhoneNumberCountryPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AvailablePhoneNumberCountryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return AvailablePhoneNumberCountryPage(self._version, response, self._solution)

    def get(self, country_code):
        """
        Constructs a AvailablePhoneNumberCountryContext

        :param country_code: The country_code

        :returns: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryContext
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryContext
        """
        return AvailablePhoneNumberCountryContext(
            self._version,
            account_sid=self._solution['account_sid'],
            country_code=country_code,
        )

    def __call__(self, country_code):
        """
        Constructs a AvailablePhoneNumberCountryContext

        :param country_code: The country_code

        :returns: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryContext
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryContext
        """
        return AvailablePhoneNumberCountryContext(
            self._version,
            account_sid=self._solution['account_sid'],
            country_code=country_code,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AvailablePhoneNumberCountryList>'


class AvailablePhoneNumberCountryPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the AvailablePhoneNumberCountryPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryPage
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryPage
        """
        super(AvailablePhoneNumberCountryPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AvailablePhoneNumberCountryInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryInstance
        """
        return AvailablePhoneNumberCountryInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AvailablePhoneNumberCountryPage>'


class AvailablePhoneNumberCountryContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, country_code):
        """
        Initialize the AvailablePhoneNumberCountryContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param country_code: The country_code

        :returns: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryContext
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryContext
        """
        super(AvailablePhoneNumberCountryContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'country_code': country_code, }
        self._uri = '/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}.json'.format(**self._solution)

        # Dependents
        self._local = None
        self._toll_free = None
        self._mobile = None
        self._national = None
        self._voip = None
        self._shared_cost = None
        self._machine_to_machine = None

    def fetch(self):
        """
        Fetch a AvailablePhoneNumberCountryInstance

        :returns: Fetched AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return AvailablePhoneNumberCountryInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            country_code=self._solution['country_code'],
        )

    @property
    def local(self):
        """
        Access the local

        :returns: twilio.rest.api.v2010.account.available_phone_number.local.LocalList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.local.LocalList
        """
        if self._local is None:
            self._local = LocalList(
                self._version,
                account_sid=self._solution['account_sid'],
                country_code=self._solution['country_code'],
            )
        return self._local

    @property
    def toll_free(self):
        """
        Access the toll_free

        :returns: twilio.rest.api.v2010.account.available_phone_number.toll_free.TollFreeList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.toll_free.TollFreeList
        """
        if self._toll_free is None:
            self._toll_free = TollFreeList(
                self._version,
                account_sid=self._solution['account_sid'],
                country_code=self._solution['country_code'],
            )
        return self._toll_free

    @property
    def mobile(self):
        """
        Access the mobile

        :returns: twilio.rest.api.v2010.account.available_phone_number.mobile.MobileList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.mobile.MobileList
        """
        if self._mobile is None:
            self._mobile = MobileList(
                self._version,
                account_sid=self._solution['account_sid'],
                country_code=self._solution['country_code'],
            )
        return self._mobile

    @property
    def national(self):
        """
        Access the national

        :returns: twilio.rest.api.v2010.account.available_phone_number.national.NationalList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.national.NationalList
        """
        if self._national is None:
            self._national = NationalList(
                self._version,
                account_sid=self._solution['account_sid'],
                country_code=self._solution['country_code'],
            )
        return self._national

    @property
    def voip(self):
        """
        Access the voip

        :returns: twilio.rest.api.v2010.account.available_phone_number.voip.VoipList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.voip.VoipList
        """
        if self._voip is None:
            self._voip = VoipList(
                self._version,
                account_sid=self._solution['account_sid'],
                country_code=self._solution['country_code'],
            )
        return self._voip

    @property
    def shared_cost(self):
        """
        Access the shared_cost

        :returns: twilio.rest.api.v2010.account.available_phone_number.shared_cost.SharedCostList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.shared_cost.SharedCostList
        """
        if self._shared_cost is None:
            self._shared_cost = SharedCostList(
                self._version,
                account_sid=self._solution['account_sid'],
                country_code=self._solution['country_code'],
            )
        return self._shared_cost

    @property
    def machine_to_machine(self):
        """
        Access the machine_to_machine

        :returns: twilio.rest.api.v2010.account.available_phone_number.machine_to_machine.MachineToMachineList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.machine_to_machine.MachineToMachineList
        """
        if self._machine_to_machine is None:
            self._machine_to_machine = MachineToMachineList(
                self._version,
                account_sid=self._solution['account_sid'],
                country_code=self._solution['country_code'],
            )
        return self._machine_to_machine

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AvailablePhoneNumberCountryContext {}>'.format(context)


class AvailablePhoneNumberCountryInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid, country_code=None):
        """
        Initialize the AvailablePhoneNumberCountryInstance

        :returns: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryInstance
        """
        super(AvailablePhoneNumberCountryInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'country_code': payload['country_code'],
            'country': payload['country'],
            'uri': payload['uri'],
            'beta': payload['beta'],
            'subresource_uris': payload['subresource_uris'],
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'country_code': country_code or self._properties['country_code'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: AvailablePhoneNumberCountryContext for this AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryContext
        """
        if self._context is None:
            self._context = AvailablePhoneNumberCountryContext(
                self._version,
                account_sid=self._solution['account_sid'],
                country_code=self._solution['country_code'],
            )
        return self._context

    @property
    def country_code(self):
        """
        :returns: The ISO Country code to lookup phone numbers for.
        :rtype: unicode
        """
        return self._properties['country_code']

    @property
    def country(self):
        """
        :returns: The country
        :rtype: unicode
        """
        return self._properties['country']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def beta(self):
        """
        :returns: True if new to Twilio platform.
        :rtype: bool
        """
        return self._properties['beta']

    @property
    def subresource_uris(self):
        """
        :returns: The subresource_uris
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    def fetch(self):
        """
        Fetch a AvailablePhoneNumberCountryInstance

        :returns: Fetched AvailablePhoneNumberCountryInstance
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryInstance
        """
        return self._proxy.fetch()

    @property
    def local(self):
        """
        Access the local

        :returns: twilio.rest.api.v2010.account.available_phone_number.local.LocalList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.local.LocalList
        """
        return self._proxy.local

    @property
    def toll_free(self):
        """
        Access the toll_free

        :returns: twilio.rest.api.v2010.account.available_phone_number.toll_free.TollFreeList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.toll_free.TollFreeList
        """
        return self._proxy.toll_free

    @property
    def mobile(self):
        """
        Access the mobile

        :returns: twilio.rest.api.v2010.account.available_phone_number.mobile.MobileList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.mobile.MobileList
        """
        return self._proxy.mobile

    @property
    def national(self):
        """
        Access the national

        :returns: twilio.rest.api.v2010.account.available_phone_number.national.NationalList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.national.NationalList
        """
        return self._proxy.national

    @property
    def voip(self):
        """
        Access the voip

        :returns: twilio.rest.api.v2010.account.available_phone_number.voip.VoipList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.voip.VoipList
        """
        return self._proxy.voip

    @property
    def shared_cost(self):
        """
        Access the shared_cost

        :returns: twilio.rest.api.v2010.account.available_phone_number.shared_cost.SharedCostList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.shared_cost.SharedCostList
        """
        return self._proxy.shared_cost

    @property
    def machine_to_machine(self):
        """
        Access the machine_to_machine

        :returns: twilio.rest.api.v2010.account.available_phone_number.machine_to_machine.MachineToMachineList
        :rtype: twilio.rest.api.v2010.account.available_phone_number.machine_to_machine.MachineToMachineList
        """
        return self._proxy.machine_to_machine

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AvailablePhoneNumberCountryInstance {}>'.format(context)
