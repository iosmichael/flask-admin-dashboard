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
from admin.twilio.rest.video.v1.room.room_participant.room_participant_published_track import PublishedTrackList
from admin.twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track import SubscribedTrackList


class ParticipantList(ListResource):
    """  """

    def __init__(self, version, room_sid):
        """
        Initialize the ParticipantList

        :param Version version: Version that contains the resource
        :param room_sid: A system-generated 34-character string that uniquely identifies.

        :returns: twilio.rest.video.v1.room.room_participant.ParticipantList
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantList
        """
        super(ParticipantList, self).__init__(version)

        # Path Solution
        self._solution = {'room_sid': room_sid, }
        self._uri = '/Rooms/{room_sid}/Participants'.format(**self._solution)

    def stream(self, status=values.unset, identity=values.unset,
               date_created_after=values.unset, date_created_before=values.unset,
               limit=None, page_size=None):
        """
        Streams ParticipantInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param ParticipantInstance.Status status: Only show Participants with the given Status.
        :param unicode identity: Only show Participants that connected to the Room using the provided Identity.
        :param datetime date_created_after: Only show Participants that started after this date, given as an UTC ISO 8601 Timestamp.
        :param datetime date_created_before: Only show Participants that started before this date, given as an UTC ISO 8601 Timestamp.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.room_participant.ParticipantInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            status=status,
            identity=identity,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, status=values.unset, identity=values.unset,
             date_created_after=values.unset, date_created_before=values.unset,
             limit=None, page_size=None):
        """
        Lists ParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param ParticipantInstance.Status status: Only show Participants with the given Status.
        :param unicode identity: Only show Participants that connected to the Room using the provided Identity.
        :param datetime date_created_after: Only show Participants that started after this date, given as an UTC ISO 8601 Timestamp.
        :param datetime date_created_before: Only show Participants that started before this date, given as an UTC ISO 8601 Timestamp.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.room_participant.ParticipantInstance]
        """
        return list(self.stream(
            status=status,
            identity=identity,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, identity=values.unset,
             date_created_after=values.unset, date_created_before=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately

        :param ParticipantInstance.Status status: Only show Participants with the given Status.
        :param unicode identity: Only show Participants that connected to the Room using the provided Identity.
        :param datetime date_created_after: Only show Participants that started after this date, given as an UTC ISO 8601 Timestamp.
        :param datetime date_created_before: Only show Participants that started before this date, given as an UTC ISO 8601 Timestamp.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantPage
        """
        params = values.of({
            'Status': status,
            'Identity': identity,
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ParticipantPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ParticipantPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ParticipantContext

        :param sid: The sid

        :returns: twilio.rest.video.v1.room.room_participant.ParticipantContext
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantContext
        """
        return ParticipantContext(self._version, room_sid=self._solution['room_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a ParticipantContext

        :param sid: The sid

        :returns: twilio.rest.video.v1.room.room_participant.ParticipantContext
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantContext
        """
        return ParticipantContext(self._version, room_sid=self._solution['room_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.ParticipantList>'


class ParticipantPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the ParticipantPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param room_sid: A system-generated 34-character string that uniquely identifies.

        :returns: twilio.rest.video.v1.room.room_participant.ParticipantPage
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantPage
        """
        super(ParticipantPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ParticipantInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.room.room_participant.ParticipantInstance
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantInstance
        """
        return ParticipantInstance(self._version, payload, room_sid=self._solution['room_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.ParticipantPage>'


class ParticipantContext(InstanceContext):
    """  """

    def __init__(self, version, room_sid, sid):
        """
        Initialize the ParticipantContext

        :param Version version: Version that contains the resource
        :param room_sid: The room_sid
        :param sid: The sid

        :returns: twilio.rest.video.v1.room.room_participant.ParticipantContext
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantContext
        """
        super(ParticipantContext, self).__init__(version)

        # Path Solution
        self._solution = {'room_sid': room_sid, 'sid': sid, }
        self._uri = '/Rooms/{room_sid}/Participants/{sid}'.format(**self._solution)

        # Dependents
        self._published_tracks = None
        self._subscribed_tracks = None

    def fetch(self):
        """
        Fetch a ParticipantInstance

        :returns: Fetched ParticipantInstance
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ParticipantInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            sid=self._solution['sid'],
        )

    def update(self, status=values.unset):
        """
        Update the ParticipantInstance

        :param ParticipantInstance.Status status: Set to disconnected to remove participant.

        :returns: Updated ParticipantInstance
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantInstance
        """
        data = values.of({'Status': status, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return ParticipantInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            sid=self._solution['sid'],
        )

    @property
    def published_tracks(self):
        """
        Access the published_tracks

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_published_track.PublishedTrackList
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_published_track.PublishedTrackList
        """
        if self._published_tracks is None:
            self._published_tracks = PublishedTrackList(
                self._version,
                room_sid=self._solution['room_sid'],
                participant_sid=self._solution['sid'],
            )
        return self._published_tracks

    @property
    def subscribed_tracks(self):
        """
        Access the subscribed_tracks

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackList
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackList
        """
        if self._subscribed_tracks is None:
            self._subscribed_tracks = SubscribedTrackList(
                self._version,
                room_sid=self._solution['room_sid'],
                subscriber_sid=self._solution['sid'],
            )
        return self._subscribed_tracks

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.ParticipantContext {}>'.format(context)


class ParticipantInstance(InstanceResource):
    """  """

    class Status(object):
        CONNECTED = "connected"
        DISCONNECTED = "disconnected"

    def __init__(self, version, payload, room_sid, sid=None):
        """
        Initialize the ParticipantInstance

        :returns: twilio.rest.video.v1.room.room_participant.ParticipantInstance
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantInstance
        """
        super(ParticipantInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'room_sid': payload['room_sid'],
            'account_sid': payload['account_sid'],
            'status': payload['status'],
            'identity': payload['identity'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'start_time': deserialize.iso8601_datetime(payload['start_time']),
            'end_time': deserialize.iso8601_datetime(payload['end_time']),
            'duration': deserialize.integer(payload['duration']),
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {'room_sid': room_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ParticipantContext for this ParticipantInstance
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantContext
        """
        if self._context is None:
            self._context = ParticipantContext(
                self._version,
                room_sid=self._solution['room_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def room_sid(self):
        """
        :returns: A system-generated 34-character string that uniquely identifies.
        :rtype: unicode
        """
        return self._properties['room_sid']

    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account associated with this Room.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def status(self):
        """
        :returns: A string representing the status of the Participant.
        :rtype: ParticipantInstance.Status
        """
        return self._properties['status']

    @property
    def identity(self):
        """
        :returns: The unique name identifier that is assigned to this Participant.
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created, given as a UTC ISO 8601 Timestamp.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated, given as a UTC ISO 8601 Timestamp.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def start_time(self):
        """
        :returns: The time of Participant connected to the Room, given as a UTC ISO 8601 Timestamp.
        :rtype: datetime
        """
        return self._properties['start_time']

    @property
    def end_time(self):
        """
        :returns: The time of Participant disconnected from the Room, given as a UTC ISO 8601 Timestamp.
        :rtype: datetime
        """
        return self._properties['end_time']

    @property
    def duration(self):
        """
        :returns: Duration of time in seconds this Participant was connected.
        :rtype: unicode
        """
        return self._properties['duration']

    @property
    def url(self):
        """
        :returns: The absolute URL for this resource.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a ParticipantInstance

        :returns: Fetched ParticipantInstance
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantInstance
        """
        return self._proxy.fetch()

    def update(self, status=values.unset):
        """
        Update the ParticipantInstance

        :param ParticipantInstance.Status status: Set to disconnected to remove participant.

        :returns: Updated ParticipantInstance
        :rtype: twilio.rest.video.v1.room.room_participant.ParticipantInstance
        """
        return self._proxy.update(status=status, )

    @property
    def published_tracks(self):
        """
        Access the published_tracks

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_published_track.PublishedTrackList
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_published_track.PublishedTrackList
        """
        return self._proxy.published_tracks

    @property
    def subscribed_tracks(self):
        """
        Access the subscribed_tracks

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackList
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackList
        """
        return self._proxy.subscribed_tracks

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.ParticipantInstance {}>'.format(context)
