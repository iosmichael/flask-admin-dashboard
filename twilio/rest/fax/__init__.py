# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base.domain import Domain
from admin.twilio.rest.fax.v1 import V1


class Fax(Domain):

    def __init__(self, twilio):
        """
        Initialize the Fax Domain

        :returns: Domain for Fax
        :rtype: twilio.rest.fax.Fax
        """
        super(Fax, self).__init__(twilio)

        self.base_url = 'https://fax.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of fax
        :rtype: twilio.rest.fax.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def faxes(self):
        """
        :rtype: twilio.rest.fax.v1.fax.FaxList
        """
        return self.v1.faxes

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Fax>'
