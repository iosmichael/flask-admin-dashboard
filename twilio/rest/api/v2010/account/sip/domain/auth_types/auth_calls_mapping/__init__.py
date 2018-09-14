# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base.instance_resource import InstanceResource
from admin.twilio.base.list_resource import ListResource
from admin.twilio.base.page import Page
from admin.twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.auth_calls_credential_list_mapping import AuthCallsCredentialListMappingList
from admin.twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.auth_calls_ip_access_control_list_mapping import AuthCallsIpAccessControlListMappingList


class AuthTypeCallsList(ListResource):
    """  """

    def __init__(self, version, account_sid, domain_sid):
        """
        Initialize the AuthTypeCallsList

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the account that sent the call
        :param domain_sid: A string that uniquely identifies the SIP Domain

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.AuthTypeCallsList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.AuthTypeCallsList
        """
        super(AuthTypeCallsList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'domain_sid': domain_sid, }

        # Components
        self._credential_list_mappings = None
        self._ip_access_control_list_mappings = None

    @property
    def credential_list_mappings(self):
        """
        Access the credential_list_mappings

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingList
        """
        if self._credential_list_mappings is None:
            self._credential_list_mappings = AuthCallsCredentialListMappingList(
                self._version,
                account_sid=self._solution['account_sid'],
                domain_sid=self._solution['domain_sid'],
            )
        return self._credential_list_mappings

    @property
    def ip_access_control_list_mappings(self):
        """
        Access the ip_access_control_list_mappings

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.auth_calls_ip_access_control_list_mapping.AuthCallsIpAccessControlListMappingList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.auth_calls_ip_access_control_list_mapping.AuthCallsIpAccessControlListMappingList
        """
        if self._ip_access_control_list_mappings is None:
            self._ip_access_control_list_mappings = AuthCallsIpAccessControlListMappingList(
                self._version,
                account_sid=self._solution['account_sid'],
                domain_sid=self._solution['domain_sid'],
            )
        return self._ip_access_control_list_mappings

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthTypeCallsList>'


class AuthTypeCallsPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the AuthTypeCallsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The unique id of the account that sent the call
        :param domain_sid: A string that uniquely identifies the SIP Domain

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.AuthTypeCallsPage
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.AuthTypeCallsPage
        """
        super(AuthTypeCallsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AuthTypeCallsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.AuthTypeCallsInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.AuthTypeCallsInstance
        """
        return AuthTypeCallsInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            domain_sid=self._solution['domain_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthTypeCallsPage>'


class AuthTypeCallsInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid, domain_sid):
        """
        Initialize the AuthTypeCallsInstance

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.AuthTypeCallsInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.AuthTypeCallsInstance
        """
        super(AuthTypeCallsInstance, self).__init__(version)

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, 'domain_sid': domain_sid, }

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthTypeCallsInstance>'
