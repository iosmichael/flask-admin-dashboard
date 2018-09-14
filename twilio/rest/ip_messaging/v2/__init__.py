# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base.version import Version
from admin.twilio.rest.ip_messaging.v2.credential import CredentialList
from admin.twilio.rest.ip_messaging.v2.service import ServiceList


class V2(Version):

    def __init__(self, domain):
        """
        Initialize the V2 version of IpMessaging

        :returns: V2 version of IpMessaging
        :rtype: twilio.rest.ip_messaging.v2.V2.V2
        """
        super(V2, self).__init__(domain)
        self.version = 'v2'
        self._credentials = None
        self._services = None

    @property
    def credentials(self):
        """
        :rtype: twilio.rest.chat.v2.credential.CredentialList
        """
        if self._credentials is None:
            self._credentials = CredentialList(self)
        return self._credentials

    @property
    def services(self):
        """
        :rtype: twilio.rest.chat.v2.service.ServiceList
        """
        if self._services is None:
            self._services = ServiceList(self)
        return self._services

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2>'
