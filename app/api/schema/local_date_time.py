from datetime import timezone

from marshmallow import fields
from flask import g
from zoneinfo import ZoneInfo

class LocalDateTime(fields.DateTime):

    def _serialize(self, value, attr, obj, **kwargs):

        if value is None:
            return None

        if value.tzinfo is None:
            value = value.replace(
                tzinfo=timezone.utc
            )

        local_dt = value.astimezone(
            ZoneInfo(g.timezone)
        )

        return super()._serialize(
            local_dt,
            attr,
            obj,
            **kwargs
        )

    def _deserialize(self, value, attr, data, **kwargs):

        local_dt = super()._deserialize(
            value,
            attr,
            data,
            **kwargs
        )

        utc_dt = local_dt.replace(
            tzinfo=ZoneInfo(g.timezone)
        ).astimezone(
            ZoneInfo("UTC")
        )

        return utc_dt