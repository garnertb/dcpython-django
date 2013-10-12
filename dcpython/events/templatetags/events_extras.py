from django import template

from dcpython.app.integration import youtube

register = template.Library()


def format_event_date(start_time, end_time):
    if end_time and (end_time - start_time).days > 0:
        multi_day = True
    else:
        multi_day = False

    return {"start_time": start_time, "end_time": end_time,
            "multi_day": multi_day}

register.inclusion_tag('events/event-datetime-range.html')(format_event_date)


def display_event(event, truncate_description=None, omit_title=False, omit_time=False,
                  omit_youtube=False):
    return {"event": event, "truncate_description": truncate_description,
            "omit_title": omit_title, "omit_time": omit_time, 'omit_youtube': omit_youtube}

register.inclusion_tag('events/event-body.html')(display_event)


def youtube_playlist(name, date):
    playlist_id = youtube.find_playlist(name, date)

    return {"name": name,
            "date": date,
            "playlist_id": playlist_id}


register.inclusion_tag('events/youtube_playlist_embed.html')(youtube_playlist)
