from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(
    r"todo-list",
    TodoListView,
    basename="todolist",
)
router.register(
    r"todo",
    TodoView,
    basename="todo",
)

urlpatterns = router.urls
