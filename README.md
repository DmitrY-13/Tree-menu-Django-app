# Tree menu Django app, UpTrader`s test task
## Using tag
* Load tree menu tag
    ```
    {% load tree_menu_tag %}
    ```
* Render tree menu
    ```
    {% tree_menu 'YOUR_MENU_NAME' %}
    ```
## Admin panel functional
* Tree menu
    * You can create new tree menu.
      When creating it, you need to give it unique name.
    * You can delete tree menu.
      After deletion, all its items will be deleted.
* Menu item
    * You can create new menu item.
      When creating it, you need to specify tree menu, title, url.
      You also can specify parent menu item.
      If you do not specify parent, then menu item will be root.
      Tree menu can have multiple roots.
    * You can delete menu item.
      After deletion, all its children will be deleted.