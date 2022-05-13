from django.db import migrations, transaction
from django.utils import timezone


def create_objects(apps, schema_editor):
    # Для загрузки кода моделей используется специальный метод apps.get_model
    # Он позволяет загрузить ровно то состояние модели, которое было на момент применения этой миграции
    # Импортировать настоящие классы – плохая практика
    # так как в будущем вы можете удалить/переименовать эти модели, и тогда у вас будут ошибки импорта

    User = apps.get_model("core", "User")
    Board = apps.get_model("goals", "Board")
    BoardParticipant = apps.get_model("goals", "BoardParticipant")
    GoalCategory = apps.get_model("goals", "GoalCategory")

    with transaction.atomic():  # Применяем все изменения одной транзакцией
        time_now = timezone.now()
        for user_id in User.objects.values_list("id", flat=True):  # Для каждого пользователя
            new_board = Board.objects.create(
                title="Мои цели",
                created=time_now,  # Проставляем вручную по той же причине, что описана вверху
                updated=time_now
            )
            BoardParticipant.objects.create(
                user_id=user_id,
                board=new_board,
                role=1,  # Владелец, проставляем числом, не импортируем код по той же причине
                created=time_now,
                updated=time_now
            )

            # проставляем всем категориям пользователя его доску
            GoalCategory.objects.filter(user_id=user_id).update(board=new_board)


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0004_board_goalcategory_board_boardparticipant'),
    ]

    operations = [
        migrations.RunPython(create_objects, migrations.RunPython.noop)
    ]
