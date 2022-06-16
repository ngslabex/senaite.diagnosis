# -*- coding: utf-8 -*-

import collections
from bika.lims import senaiteMessageFactory as _s
from bika.lims.utils import get_link_for
from senaite.app.listing import ListingView
from senaite.core.catalog import SETUP_CATALOG


class AetiologicAgentsListingView(ListingView):
    """Aetiologic Agents listing view
    """

    def __init__(self, context, request):
        super(AetiologicAgentsListingView, self).__init__(context, request)

        self.catalog = SETUP_CATALOG

        self.contentFilter = {
            "portal_type": "AetiologicAgent",
            "sort_on": "sortable_title",
            "sort_order": "ascending",
        }

        self.context_actions = {
            _s("Add"): {
                "url": "++add++AetiologicAgent",
                "icon": "add.png"}
            }

        self.show_select_column = True

        self.columns = collections.OrderedDict((
            ("Title", {
                "title": _s("Title"),
                "index": "sortable_title"
            }),
            ("Description", {
                "title": _s("Description"),
                "index": "Description"
            }),
        ))

        self.review_states = [
            {
                "id": "default",
                "title": _s("Active"),
                "contentFilter": {"is_active": True},
                "transitions": [],
                "columns": self.columns.keys(),
            }, {
                "id": "inactive",
                "title": _s("Inactive"),
                "contentFilter": {'is_active': False},
                "transitions": [],
                "columns": self.columns.keys(),
            }, {
                "id": "all",
                "title": _s("All"),
                "contentFilter": {},
                "columns": self.columns.keys(),
            },
        ]

    def update(self):
        """Update hook
        """
        super(AetiologicAgentsListingView, self).update()

    def before_render(self):
        """Before template render hook
        """
        super(AetiologicAgentsListingView, self).before_render()

    def folderitem(self, obj, item, index):
        """Service triggered each time an item is iterated in folderitems.
        The use of this service prevents the extra-loops in child objects.
        :obj: the instance of the class to be foldered
        :item: dict containing the properties of the object to be used by
            the template
        :index: current index of the item
        """
        item["replace"]["Title"] = get_link_for(obj)
        return item

    def get_children_hook(self, parent_uid, child_uids=None):
        """Hook to get the children of an item
        """
        super(AetiologicAgentsListingView, self).get_children_hook(
            parent_uid, child_uids=child_uids)
