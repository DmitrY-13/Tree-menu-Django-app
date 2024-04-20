from django import template
from django.template import Context
from django.utils.safestring import mark_safe, SafeString

from tree_menu_app.models import MenuItem

register = template.Library()


def get_items_with_visible_children_ids(items: list[MenuItem], current_item_id: int) -> set[id]:
    for item in items:
        item_children = item.children.all()

        if item.id == current_item_id:
            return {item.id}

        ids = get_items_with_visible_children_ids(item_children, current_item_id)
        if len(ids) != 0:
            ids.add(item.id)
            return ids

    return set()


def render_tree_menu_items(
        items: list[MenuItem],
        items_with_visible_children_ids: set[int],
        current_item_id: int
) -> str:
    html = '<ul>'

    for item in items:
        item_title = item.title
        if item.id == current_item_id:
            item_title = f'<span class="tree-menu-current-item">{item_title}</span>'

        html += f'<li><a href="{item.url}">{item_title}</a>'
        if item.id in items_with_visible_children_ids:
            html += render_tree_menu_items(item.children.all(), items_with_visible_children_ids, current_item_id)
        html += '</li>'

    html += '</ul>'

    return html


@register.simple_tag(takes_context=True)
def tree_menu(context: Context, menu_name: str) -> SafeString:
    items = MenuItem.objects.filter(menu__name=menu_name)
    root_items = items.filter(parent=None)
    url = context['request'].path
    current_item_id = items.get(url=url).id

    items_with_visible_children_ids = get_items_with_visible_children_ids(root_items, current_item_id)
    html = render_tree_menu_items(root_items, items_with_visible_children_ids, current_item_id)
    html = f'<div class="tree-menu"><span class="tree-menu-name">{menu_name}</span>{html}</div>'

    return mark_safe(html)
