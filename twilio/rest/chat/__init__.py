# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base.domain import Domain
from admin.twilio.rest.chat.v1 import V1
from admin.twilio.rest.chat.v2 import V2


class Chat(Domain):

    def __init__(self, twilio):
        """
        Initialize the Chat Domain

        :returns: Domain for Chat
        :rtype: twilio.rest.chat.Chat
        """
        super(Chat, self).__init__(twilio)

        self.base_url = 'https://chat.twilio.com'

        # Versions
        self._v1 = None
        self._v2 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of chat
        :rtype: twilio.rest.chat.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def v2(self):
        """
        :returns: Version v2 of chat
        :rtype: twilio.rest.chat.v2.V2
        """
        if self._v2 is None:
            self._v2 = V2(self)
        return self._v2

    @property
    def credentials(self):
        """
        :rtype: twilio.rest.chat.v2.credential.CredentialList
        """
        return self.v2.credentials

    @property
    def services(self):
        """
        :rtype: twilio.rest.chat.v2.service.ServiceList
        """
        return self.v2.services

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat>'
