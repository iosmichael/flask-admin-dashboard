# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base.version import Version
from admin.twilio.rest.preview.acc_security.service import ServiceList


class AccSecurity(Version):

    def __init__(self, domain):
        """
        Initialize the AccSecurity version of Preview

        :returns: AccSecurity version of Preview
        :rtype: twilio.rest.preview.acc_security.AccSecurity.AccSecurity
        """
        super(AccSecurity, self).__init__(domain)
        self.version = 'Verification'
        self._services = None

    @property
    def services(self):
        """
        :rtype: twilio.rest.preview.acc_security.service.ServiceList
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
        return '<Twilio.Preview.AccSecurity>'
