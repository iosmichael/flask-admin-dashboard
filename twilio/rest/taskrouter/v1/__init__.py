# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from admin.twilio.base.version import Version
from admin.twilio.rest.taskrouter.v1.workspace import WorkspaceList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Taskrouter

        :returns: V1 version of Taskrouter
        :rtype: twilio.rest.taskrouter.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._workspaces = None

    @property
    def workspaces(self):
        """
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceList
        """
        if self._workspaces is None:
            self._workspaces = WorkspaceList(self)
        return self._workspaces

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1>'
