from django.contrib import admin
from django.db.models import Count

from goals.models import GoalCategory, Goal, GoalComment


class GoalInline(admin.TabularInline):
    model = Goal
    extra = 0
    show_change_link = True

    def _get_form_for_get_fields(self, request, obj=None):
        return self.get_formset(request, obj, fields=("title", "status", "priority", "due_date")).form

    def has_change_permission(self, request, obj=None):
        return False


class GoalCommentInline(admin.TabularInline):
    model = GoalComment
    extra = 0
    # show_change_link = True

    def _get_form_for_get_fields(self, request, obj=None):
        return self.get_formset(request, obj, fields=("text", "user")).form


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "goals_count", "created", "updated")
    search_fields = ("title", "user")
    readonly_fields = ("created", "updated")
    list_filter = ("is_deleted",)
    inlines = (GoalInline,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_goals_count=Count("goals", destinct=True))
        return queryset

    def goals_count(self, obj):
        return obj._goals_count

    goals_count.short_description = "Кол-во целей"


class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "priority", "due_date")
    search_fields = ("title", "user")
    readonly_fields = ("created", "updated")
    list_filter = ("user", "status", "priority")
    inlines = (GoalCommentInline,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_comments_count=Count("goal_comments", destinct=True))
        return queryset

    def comments_count(self, obj):
        return obj._comments_count

    comments_count.short_description = "Кол-во комментариев"


class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ("goal_id", "text", "user")
    list_display_links = ("text",)
    search_fields = ("text",)
    readonly_fields = ("created", "updated")
    list_filter = ("user", "goal")


admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(GoalComment, GoalCommentAdmin)
admin.site.register(Goal, GoalAdmin)
