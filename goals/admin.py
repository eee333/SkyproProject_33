from django.contrib import admin

from goals.models import GoalCategory, Goal, GoalComment


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")
    readonly_fields = ("created", "updated")
    list_filter = ("is_deleted",)


class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "priority", "due_date")
    search_fields = ("title", "user")
    readonly_fields = ("created", "updated")
    list_filter = ("user", "status", "priority")


class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ("goal_id", "text", "user")
    list_display_links = ("text",)
    search_fields = ("text",)
    readonly_fields = ("created", "updated")
    list_filter = ("user", "goal")


admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(GoalComment, GoalCommentAdmin)
admin.site.register(Goal, GoalAdmin)
