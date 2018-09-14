# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base.version import Version
from admin.twilio.rest.fax.v1.fax import FaxList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Fax

        :returns: V1 version of Fax
        :rtype: twilio.rest.fax.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._faxes = None

    @property
    def faxes(self):
        """
        :rtype: twilio.rest.fax.v1.fax.FaxList
        """
        if self._faxes is None:
            self._faxes = FaxList(self)
        return self._faxes

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Fax.V1>'
